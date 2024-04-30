from damage_calcs import *
import argparse
import sys
from gooey import Gooey, GooeyParser

class monsterClass:
    def __init__(monster, magic, defence, slash, crush, ranged, cap, name):
        monster.magicLvl = magic
        monster.defenceLvl = defence
        monster.slashDefLvl = slash
        monster.crushDefLvl = crush
        monster.rangedDefLvl = ranged
        monster.cap = cap
        monster.storedDefLvl = defence
        monster.bossName = name

maiden = monsterClass(350, 200, 0, 0, 0, 0, "maiden")
xarpus = monsterClass(220, 250, 0, 0, 160, 0, "xarpus")
sotetseg = monsterClass(250, 200, 70, 70, 150, 100, "sotetseg")

monsters = {
    "maiden": monsterClass(350, 200, 0, 0, 0, 0, "maiden"),
    "xarpus": monsterClass(220, 250, 0, 0, 160, 0, "xarpus"),
    "sotetseg": monsterClass(250, 200, 70, 70, 150, 100, "sotetseg")
}

class Player:
    def __init__(self,role):
        self.role = role
        # HITS
        self.bgs_hits = []
        self.hammer_hits = []
        self.ralos_hits = []
        self.emaul_hits = []
        #STATS
        self.attackLvl = 118
        self.strengthLvl = 118
        self.rangeLvl = 112
        self.magicLvl = 112
        # WEAPON INFO
        self.ralosAttRoll = 30576
        self.ralosMax = 24
        self.bgsAttRoll = 69434
        self.bgsMax = 77
        self.dwhAttRoll = 34048
        self.dwhMax = 82
        self.emaulAttRoll = 35872 * 1.25
        self.emaulMax = 68
        # OTHER
        self.hitStyle = "live" # options: "live", "one_max", "max_minus_one"
        # hit rolls for above hit styles:
        # live: [0,max_hit] | one_max: [1, max_hit] | max_minus_one: [1, (max_hit-1)] 

weapon_dict = {
    4: "hammer_hits",
    15: "bgs_hits",
    72: "ralos_hits",
    102: "emaul_hits",
}

def configure_players_from_text(input_text):
    players = [Player(f"player{i + 1}") for i in range(5)]  # Adjust the range as needed
    lines = input_text.strip().split('\n')

    for line in lines:
        parts = line.split(',')
        player_id_str = parts[0].strip()  # Remove any leading/trailing whitespace
        if player_id_str:  # Check if the string is not empty
            player_id = int(player_id_str[6:]) - 1  # Extract number from the format "Player1", "Player2", etc.
            for part in parts[1:]:
                part = part.strip()  # Strip each part of extra spaces
                if part:  # Check if part is not empty
                    tick_info = part.strip('{}').split(':')
                    tick = int(tick_info[0])
                    weapon_code = int(tick_info[1])
                    weapon_type = weapon_dict.get(weapon_code)
                    if weapon_type:
                        getattr(players[player_id], weapon_type).append(tick)

    return players


def sim_from_json(hit_style, monster_name, input_text):
    monster = monsters[monster_name]
    players = configure_players_from_text(input_text)
    for player in players:
        player.hitStyle = hit_style
        print(f"{player.role}: BGS ticks: {player.bgs_hits}, DWH Ticks: {player.hammer_hits}, Ralos Ticks: {player.ralos_hits}, Elder Maul Ticks: {player.emaul_hits}")

    write_file = False
    num_runs = 25000
    def_levels = []
    wins_0 = 0
    wins_100 = 0
    wins_140 = 0
    fails = 0

    def_levels = []
    for i in range(num_runs):
        monster.defenceLvl = monster.storedDefLvl
        iter_def_lvl = simulate_defence_reduction(players, monster)
        def_levels.append(iter_def_lvl)
        if iter_def_lvl < 1:
            wins_0 += 1
        elif iter_def_lvl < 101:
            wins_100 += 1
            wins_140 += 1  # Include levels below 101 in the wins_140 count
        elif iter_def_lvl < 141:
            wins_140 += 1  # This now correctly includes levels from 101 to 140
        else:
            fails += 1

    print(f"Results from {num_runs} simulations with hit style: {hit_style} using custom setup. ")
    if monster_name == "sotetseg":
        print(f"100 defence: {(wins_100/num_runs)*100}%")
        print(f"140 defence: {(wins_140/num_runs)*100}%")
    else:
        print(f"Zero defence: {(wins_0/num_runs)*100}%")


@Gooey(program_name="Defence Reduction Simulator")
def main():
    parser = GooeyParser(description="Simulate different special attack combinations on bosses.")

    parser.add_argument(
        'hit_style',
        metavar = 'Hit Style',
        help = 'Choose the hit calculation method',
        choices =['live','max_minus_one','one_max'],
        widget = 'Dropdown'
    )

    parser.add_argument(
        'monster_name',
        metavar='Monster Name',
        help='Choose the monster',
        choices=['maiden', 'sotetseg', 'xarpus'],  # You can modify this list as needed
        widget='Dropdown'
    )

    parser.add_argument(
        'input_text',
        metavar='Input Text',
        help='Enter some text',
        widget='Textarea'
    )

    args = parser.parse_args()
    sim_from_json(hit_style=args.hit_style,
                  monster_name=args.monster_name,
                  input_text=args.input_text)
        #parser = argparse.ArgumentParser(description='Run boss fight simulations.')
    #parser.add_argument('hit_style', type=str, help='Hit style for the simulation ("live", "one_max", or "max_minus_one")')
    #parser.add_argument('monster_name', type=str, help='Name of the monster ("maiden" or "xarpus")')
    #parser.add_argument('input_text', type=str, help='Player setup as a string input')
    
    #args = parser.parse_args()

    #sim_from_json(args.hit_style, args.monster_name, args.input_text, num_iter=num_iter)

#if __name__ == '__main__':
#     main()
configure_players_from_text(input_text="""Player1,{1:4},{7:19},
Player2,{1:19},{6:19},
Player3,{7:19},{1:4},
Player4,{1:19},{6:19},""")
print(f"{player.role}: BGS ticks: {player.bgs_hits}, DWH Ticks: {player.hammer_hits}, Ralos Ticks: {player.ralos_hits}, Elder Maul Ticks: {player.emaul_hits}")

# sim_from_json(hit_style="live",
#                   monster_name="sotetseg",
#                   input_text="""
#                   Player1,{6:16},{11:72},{17:16},{11:72},
# Player2,{6:16},{11:72},{17:16},{11:72},
# Player3,{0:46},{0:46},{5:16},{16:19},
# Player4,{0:46},{5:16},{16:19},,
# """)

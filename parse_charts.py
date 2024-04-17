from damage_calcs import *

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

class Player:
    def __init__(self,role):
        self.role = role
        # HITS
        self.bgs_hits = []
        self.dwh_hits = []
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
        self.emaulAttRoll = 35872
        self.emaulMax = 68
        # OTHER
        self.hitStyle = "live" # options: "live", "one_max", "max_minus_one"
        # hit rolls for above hit styles:
        # live: [0,max_hit] | one_max: [1, max_hit] | max_minus_one: [1, (max_hit-1)] 

weapon_dict = {
    4: "dwh_hits",
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


input_text = """
Player1,{1:16},{7:72},{13:16},
Player2,{1:16},{7:72},{13:16},
Player3,{1:16},{6:19},{7:46},{11:19},
Player4,{1:16},{6:4},{7:46},{12:19},
Player5,
"""

players = configure_players_from_text(input_text)

# Example of how to use these players
for player in players:
    print(f"{player.role}: {player.bgs_hits}, {player.dwh_hits}, {player.ralos_hits}, {player.emaul_hits}")

def sim_from_json(hit_style, monster, input_text):
    configure_players_from_text(input_text)
    for player in players:
        player.hitStyle = hit_style

    write_file = False
    num_runs = 500000
    def_levels = []
    wins_0 = 0
    fails = 0

    def_levels = []
    for i in range(num_runs):
        monster.defenceLvl = monster.storedDefLvl
        iter_def_lvl = simulate_boss_fight(players, monster)
        def_levels.append(iter_def_lvl)
        if iter_def_lvl < 1:
            wins_0 += 1
        else:
            fails += 1


    print(f"Results from {num_runs} simulations with hit style: {hit_style} using custom setup. ")
    print(f"Zero defence: {(wins_0/num_runs)*100}%")

sim_from_json(hit_style = "live",
              monster = maiden,
              input_text = """
                            Player1,{1:16},{7:72},{13:16},
                            Player2,{1:16},{7:72},{13:16},
                            Player3,{1:16},{6:19},{7:46},{11:19},
                            Player4,{1:16},{6:4},{7:46},{12:19},
                            Player5,
                            """
              )
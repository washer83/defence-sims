import random
import numpy as np
from damage_calcs import reduce_defence

class Player:
    def __init__(self,role):
        self.role = role
        self.bgs_hits = []
        self.hammer_hits = []
        self.ralos_hits = []
        self.emaul_hits = []
        self.attackLvl = 118
        self.strengthLvl = 118
        self.rangeLvl = 112
        self.magicLvl = 112
        self.hitStyle = "live" # options: "live", "one_max", "max_minus_one"
        # hit rolls for above hit styles:
        # live: [0,max_hit] | one_max: [1, max_hit] | max_minus_one: [1, (max_hit-1)] 

class monsterClass:
    def __init__(monster, magic, defence, slash, crush, ranged, cap):
        monster.magicLvl = magic
        monster.defenceLvl = defence
        monster.slashDefLvl = slash
        monster.crushDefLvl = crush
        monster.rangedDefLvl = ranged
        monster.cap = cap

maiden = monsterClass(350, 200, 0, 0, 0, 0)
xarpus = monsterClass(220, 250, 0, 0, 160, 0)
sote = monsterClass(250, 200, 70, 70, 150, 100)


def simulate_boss_fight(players, monster, max_ticks=21):
    tick = 0
    while tick < max_ticks:
        for player in players:
            reduce_defence(tick, player, monster)  # This updates monster.defenceLvl directly
        monster.defenceLvl = max(monster.defenceLvl, 0)  # Ensure it doesn't drop below 0 after all modifications
        tick += 1
    return monster.defenceLvl


def main(hit_style): #add chart input?
    player1 = Player('player1')
    player1.hitStyle = hit_style
    player2 = Player('player2')
    player2.hitStyle = hit_style
    player3 = Player('player3')
    player3.hitStyle = hit_style
    player4 = Player('player4')
    player4.hitStyle = hit_style

    # 2 hammer 2 ralos test case
    player1.hammer_hits = []
    player1.bgs_hits = []
    player1.ralos_hits = [11]
    player1.emaul_hits = []
    
    player2.hammer_hits = []
    player2.bgs_hits = []
    player2.ralos_hits = [11]
    player2.emaul_hits = []

    player3.hammer_hits = []
    player3.bgs_hits = []
    player3.ralos_hits = []
    player3.emaul_hits = [10]

    player4.hammer_hits = []
    player4.bgs_hits = []
    player4.ralos_hits = []
    player4.emaul_hits = [10]


    # Player 1
    player1.ralosAttRoll = 30576    # void, quiver, ralos
    player1.ralosMax = 24           # sus
    player1.bgsAttRoll = 69434      # slash, max gear
    player1.bgsMax = 77   

    # Player 2
    player2.ralosAttRoll = 30576    # void, quiver, ralos
    player2.ralosMax = 24           # void, quiver, ralos
    player2.bgsAttRoll = 69434      # slash, max gear
    player2.bgsMax = 77   

    # Player 3
    player3.dwhAttRoll = 34048      # crush, accurate, max gear
    player3.dwhMax = 82             # accounts for dmg bonus from spec
    player3.bgsAttRoll = 69434      # slash, max gear
    player3.bgsMax = 77             
    player3.emaulAttRoll = 35872    # crush, accurate, max gear
    player3.emaulMax = 66           # pce dwh

    # Player 4
    player4.dwhAttRoll = 34048      # crush, accurate, max gear
    player4.dwhMax = 82             # accounts for dmg bonus from spec
    player4.bgsAttRoll = 69434      # slash, max gear
    player4.bgsMax = 77             
    player4.emaulAttRoll = 35872    # crush, accurate, max gear
    player4.emaulMax = 68           # pce dwh


    maiden = monsterClass(350, 200, 0, 0, 0, 0)
    players = [player1, player2, player3, player4]
    monster = maiden 
    num_runs = 500000
    def_levels = []
    wins_0 = 0
    wins_15 = 0
    fails = 0
    for i in range(num_runs):
        # Resetting monster's defense level for each simulation
        monster.defenceLvl = 200  # or whatever the initial value should be
        iter_def_lvl = simulate_boss_fight(players, monster)
        def_levels.append(iter_def_lvl)
        if iter_def_lvl < 1:
            wins_0 += 1
            wins_15 += 1
        elif iter_def_lvl < 15:
            wins_15 += 1
        else:
            fails += 0
        

    print(f"Results from {num_runs} simulations with hit style: {player1.hitStyle}")
    print(f"Zero defence: {(wins_0/num_runs)*100}")
    #print(f"Less than 15 defence: {(wins_15/num_runs)*100}")
    #print((wins/num_runs) * 100)
    #def_levels = np.array(def_levels)
    #print(f"Average defence level: {def_levels.mean()}")

        
main("live")
main("max_minus_one")
main("one_max")

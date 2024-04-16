import random
import numpy as np
from damage_calcs import reduce_defence

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
        self.emaulAttRoll = 35872
        self.emaulMax = 68
        # OTHER
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

def simulate_boss_fight(players, monster, max_ticks=25):
    tick = 0
    while tick < max_ticks:
        for player in players:
            reduce_defence(tick, player, monster)  # This updates monster.defenceLvl directly
        monster.defenceLvl = max(monster.defenceLvl, 0)  # Ensure it doesn't drop below 0 after all modifications
        tick += 1
    return monster.defenceLvl

def create_player_setup(setup_name):
    # Initialize empty players
    players = [Player(f"player{i + 1}") for i in range(4)]
    
    # Nomenclautre:
    # players[0] = mage
    # players[1] = mfrz
    # players[2] = rdps
    # players[3] = mdps

    # Configure based on setup name
    # DWH BGS SETUPS
    if setup_name == "2DWH2BGS":
        players[0].bgs_hits = [11]
        players[1].bgs_hits = [11]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]
    
    elif setup_name == "2DWH2BGS1BGS":
        players[0].bgs_hits = [11,17]
        players[1].bgs_hits = [11]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]

    elif setup_name == "2DWH2BGS2BGS":
        players[0].bgs_hits = [11,17]
        players[1].bgs_hits = [11,17]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]

    elif setup_name == "2DWH2BGS3BGS":
        players[0].bgs_hits = [11,17]
        players[1].bgs_hits = [11,17]
        players[2].hammer_hits = [10]
        players[2].bgs_hits = [21]
        players[3].hammer_hits = [10]

    # GLAIVE SETUPS
    elif setup_name == "2DWH2G":
        players[0].ralos_hits = [11]
        players[1].ralos_hits = [11]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]

    elif setup_name == "2DWH2G1G":
        players[0].ralos_hits = [11,17]
        players[1].ralos_hits = [11]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]

    elif setup_name == "2DWH2G1BGS":
        players[0].ralos_hits = [11]
        players[1].ralos_hits = [11]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]
        players[3].bgs_hits = [16]

    elif setup_name == "2DWH2G1G1BGS":
        players[0].ralos_hits = [11,17]
        players[1].ralos_hits = [11]
        players[2].hammer_hits = [10]
        players[3].hammer_hits = [10]
        players[3].bgs_hits = [21]

    # ELDER GLAIVE SETUPS
    elif setup_name == "2EM2G":
        players[0].ralos_hits = [11]
        players[1].ralos_hits = [11]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]
    
    elif setup_name == "2EM2G1BGS":
        players[0].ralos_hits = [11]
        players[1].ralos_hits = [11]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]
        players[3].bgs_hits = [16]
    
    elif setup_name == "2EM2G1G":
        players[0].ralos_hits = [11,17]
        players[1].ralos_hits = [11]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]

    elif setup_name == "2EM2G1G1BGS":
        players[0].ralos_hits = [11,17]
        players[1].ralos_hits = [11]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]
        players[3].bgs_hits = [18]          
    
    # ELDER BGS BU SETUPS
    elif setup_name == "2EM2BGS":
        players[0].bgs_hits = [11]
        players[1].bgs_hits = [11]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]
    
    elif setup_name == "2EM2BGS1BGS":
        players[0].bgs_hits = [11]
        players[1].bgs_hits = [11]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]
        players[3].bgs_hits = [16]

    elif setup_name == "2EM2BGS2BGS":
        players[0].bgs_hits = [11,17]
        players[1].bgs_hits = [11,17]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]

    elif setup_name == "2EM2BGS3BGS":
        players[0].bgs_hits = [11,17]
        players[1].bgs_hits = [11,17]
        players[2].emaul_hits = [10]
        players[3].emaul_hits = [10]
        players[3].bgs_hits = [21]
    
    # DUO SPECS
    elif setup_name == "duo2DWH2BGS":
        players[0].hammer_hits = [6,12]
        players[1].bgs_hits = [16,22]

    elif setup_name == "duo2EM2BGS":
        players[0].emaul_hits = [6,12]
        players[1].bgs_hits = [16,22] 
    
    return players

def main(hit_style, setup_name):
    players = create_player_setup(setup_name)
    for player in players:
        player.hitStyle = hit_style

    monster = monsterClass(350, 200, 0, 0, 0, 0)
    num_runs = 300000
    def_levels = []
    wins_0 = 0
    wins_20 = 0
    wins_35 = 0
    wins_50 = 0
    fails = 0

    for i in range(num_runs):
        monster.defenceLvl = 200
        iter_def_lvl = simulate_boss_fight(players, monster)
        def_levels.append(iter_def_lvl)
        if iter_def_lvl < 1:
            wins_0 += 1
            wins_20 += 1
            wins_35 += 1
            wins_50 += 1
        elif iter_def_lvl < 20:
            wins_20 += 1
            wins_35 += 1
            wins_50 += 1
        elif iter_def_lvl < 35:
            wins_35 += 1
            wins_50 += 1
        elif iter_def_lvl < 50:
            wins_50 += 1
        else:
            fails += 1

    print(f"Results from {num_runs} simulations with hit style: {hit_style} and setup: {setup_name}")
    print(f"Zero defence: {(wins_0/num_runs)*100}%")
    print(f"20 defence: {(wins_20/num_runs)*100}%")
    print(f"35 defence: {(wins_35/num_runs)*100}%")
    print(f"50 defence: {(wins_50/num_runs)*100}%")




    #print(f"Less than 15 defence: {(wins_15/num_runs)*100}%")

# Run simulations for different configurations

elder_bgs_setups = ["2EM2BGS",
                    "2EM2BGS1BGS",
                    "2EM2BGS2BGS",
                    "2EM2BGS3BGS"]

duo_setups = ["duo2DWH2BGS",
              "duo2EM2BGS"]

diff_hit_types = ["live","max_minus_one","one_max"]

for hit_type in diff_hit_types:
    print("=======================================")
    print(f"Hit Style: {hit_type}")
    print("=======================================")
    for setup in duo_setups:
        main(hit_type,setup)
    print("///////////////////////////////////////")
    print()

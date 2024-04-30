import random
import numpy as np
import csv
from damage_calcs import reduce_defence, simulate_defence_reduction
from default_spec_options import create_player_setup

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
        self.emaulAttRoll = 35872 #add 
        self.emaulMax = 68
        # OTHER
        self.hitStyle = "live" # options: "live", "one_max", "max_minus_one", "one_one_max"
        # hit rolls for above hit styles:
        # live: [0,max_hit] | one_max: [1, max_hit] | max_minus_one: [1, (max_hit-1)] 
        # one_one_max: [1,1-max]

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

def main(hit_style, setup_name, monster):
    players = create_player_setup(setup_name)
    for player in players:
        player.hitStyle = hit_style

    write_file = False
    num_runs = 100000
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
    
    results = {}
    # Calculating and writing results after all simulations
    if write_file == True:
        filename = f'./sim_results/{monster.bossName}/{setup_name}_{monster.bossName}_{player.hitStyle}_def_results.csv'
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Boss Defense Range', 'Percentage'])
            for defense_range in range(0, 210, 10):
                count = sum(1 for defense in def_levels if defense <= defense_range)
                percentage = (count / num_runs) * 100
                writer.writerow([f'Less than or equal to {defense_range}', percentage])
        filename=f'./sim_results/{monster.bossName}/sim_results_{setup_name}_{monster.bossName}_{player.hitStyle}_def_results.csv'
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([def_levels])


    if monster == sotetseg:
        #print(f"Results from {num_runs} simulations with hit style: {hit_style} and setup: {setup_name}")
        print(f"100 defence: {(wins_100/num_runs)*100}%")
        #print(f"140 defence: {(wins_140/num_runs)*100}%")
    else:
        print(f"Zero defence: {(wins_0/num_runs)*100}%")

# Run simulations for different configurations

duo_maiden_setups = ["duo2DWH2BGSmaiden",
                    "duo2EM2BGSmaiden"]

duo_xarpus_setups = ["duo2DWH2BGSxarp",
                   "duo3DWH1BGSxarp",
                   "duo2EM2BGSxarp",
                   "duo3EM1BGSxarp"]

maiden_money_glaive_setups = ["2DWH2G",
                              "2DWH2G1BGS",
                              "2DWH2G1G",
                              "2DWH2G1G1BGS",
                              "2EM2G",
                              "2EM2G1BGS",
                              "2EM2G1G",
                              "2EM2G1G1BGS"]

maiden_no_glaive_setups = ["2DWH2BGS",
                           "2DWH2BGS1BGS",
                           "2DWH2BGS2BGS",
                           "2DWH2BGS3BGS",
                           "2EM2BGS",
                           "2EM2BGS1BGS",
                           "2EM2BGS2BGS",
                           "2EM2BGS3BGS"]

sote_specs = ["2DWH",
            "2DWH1H",
            "2DWH1BGS",
            "2DWH1G",
            "2EM",
            "2EM1EM",
            "2EM1BGS",
            "2EM1G"]

xarpus_specs = ["2DWH2BGS",
                "2DWH2BGS1BGS",
                "2DWH2BGS2BGS",
                "2DWH2BGS1G"]

xarpus_3h = ["3DWH1BGS",
             "3DWH1BGS1BGS",
             "3DWH1BGS2BGS",
             "3DWH1BGS1G",
             "3EM1BGS",
             "3EM1BGS1BGS",
             "3EM1BGS2BGS",
             "3EM1BGS1G"]
xarpus_zcb = ["xarpZCB"]

maiden_trio = ["1DWH2G",
               "1DWH2G1BGS",
               "1EM2G",
               "1EM2G1BGS"]
testtt = ["1DWH1G1BGS"]

sote_test =["2DWH1G"]
maiden_Test = ["2EM2G"]
diff_hit_types = ["live","one_one_max"]

for hit_type in diff_hit_types:
    print("=======================================")
    print(f"Hit Style: {hit_type}")
    print("=======================================")
    for setup in testtt:
        print('setup', setup)
        main(hit_type,setup,maiden)
        print ('----------------------')
        
    print("///////////////////////////////////////")
    print()

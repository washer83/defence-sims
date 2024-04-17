import random
import numpy as np
import csv
from damage_calcs import reduce_defence
from default_spec_options import create_player_setup

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


def simulate_boss_fight(players, monster, max_ticks=25):
    tick = 0
    while tick < max_ticks:
        for player in players:
            reduce_defence(tick, player, monster)  # This updates monster.defenceLvl directly
        monster.defenceLvl = max(monster.defenceLvl, 0)  # Ensure it doesn't drop below 0 after all modifications
        tick += 1
    return monster.defenceLvl


def main(hit_style, setup_name, monster):
    players = create_player_setup(setup_name)
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



    print(f"Results from {num_runs} simulations with hit style: {hit_style} and setup: {setup_name}")
    print(f"Zero defence: {(wins_0/num_runs)*100}%")


# Run simulations for different configurations
elder_bgs_setups = ["2EM2BGS",
                    "2EM2BGS1BGS",
                    "2EM2BGS2BGS",
                    "2EM2BGS3BGS"]

duo_maiden_setups = ["duo2DWH2BGSmaiden",
                    "duo2EM2BGSmaiden"]

duo_xarpus_setups = ["duo2DWH2BGSxarp",
                   "duo3DWH1BGSxarp",
                   "duo2EM2BGSxarp",
                   "duo3EM1BGSxarp"]

maiden_money_glaive_setups = ["2DWH2G",
                              "2DWH2G1BGS",
                              "2DWH2G1G",
                              "2DWH2G1G1BGS"]

maiden_money_glaive_elder_setups = ["2EM2G",
                              "2EM2G1BGS",
                              "2EM2G1G",
                              "2EM2G1G1BGS"]

diff_hit_types = ["live","max_minus_one","one_max"]

for hit_type in diff_hit_types:
    print("=======================================")
    print(f"Hit Style: {hit_type}")
    print("=======================================")
    for setup in duo_maiden_setups:
        print('setup', setup)
        main(hit_type,setup,maiden)
        
    print("///////////////////////////////////////")
    print()

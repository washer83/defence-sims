import random

def roll_hit(player,max_hit):
    hit_type = player.hitStyle
    if hit_type == "live":
        hit = random.randint(0, max_hit)
    elif hit_type == "one_max":
        hit = random.randint(1, max_hit)
    elif hit_type == "max_minus_one":
        hit = random.randint(1,(max_hit-1))
    return hit

def reduce_defence(tick, player, monster):
    #print("Tick #: ", tick)
    #print("Starting defence level: ", monster.defenceLvl)
    if tick in player.hammer_hits:
        monster.defenceLvl = apply_dwh(player, monster)
    elif tick in player.bgs_hits:
        monster.defenceLvl = apply_bgs(player, monster)
    elif tick in player.ralos_hits:
        monster.defenceLvl = apply_ralos(player, monster)
    elif tick in player.emaul_hits: 
        monster.defenceLvl = apply_emaul(player,monster)
    #print("End of tick defence level: ", monster.defenceLvl)
    return monster.defenceLvl

def apply_dwh(player, monster):
    max_hit = player.dwhMax
    att_roll = player.dwhAttRoll
    def_roll = max((monster.defenceLvl + 9) * (monster.crushDefLvl + 64), 1)

    if random.randint(0, att_roll) > random.randint(0, def_roll):
        hit = roll_hit(player, max_hit)
        if hit > 0:
            updated_def_lvl = monster.defenceLvl * 0.7
            monster.defenceLvl = max(updated_def_lvl, monster.cap, 0)  # Ensure defense does not drop below zero
    return monster.defenceLvl

def apply_bgs(player, monster):
    max_hit = player.bgsMax
    att_roll = player.bgsAttRoll
    melee_def_roll = max((monster.defenceLvl + 9) * (monster.slashDefLvl + 64), 1)

    if random.randint(0, att_roll) > random.randint(0, melee_def_roll):
        hit = roll_hit(player, max_hit)
        monster.defenceLvl = max(monster.defenceLvl - hit, monster.cap, 0)  # Also prevent defense from going below 0
    return monster.defenceLvl

def apply_ralos(player, monster):
    max_hit = player.ralosMax
    att_roll = player.ralosAttRoll
    defence_lvl = monster.defenceLvl
    def_roll = max((monster.defenceLvl + 9) * (monster.rangedDefLvl + 64), 1)
    hits_to_apply = 2

    for _ in range(hits_to_apply):
        if random.randint(0, att_roll) > random.randint(0, def_roll):
            hit = roll_hit(player, max_hit)
            if hit > 0:
                monster.defenceLvl = max(monster.defenceLvl - 0.1 * monster.magicLvl, 0)  # Check after each hit
    return monster.defenceLvl

def apply_emaul(player, monster):
    max_hit = player.emaulMax
    att_roll = player.emaulAttRoll
    def_roll = max((monster.defenceLvl + 9) * (monster.crushDefLvl + 64), 1)

    if random.randint(0, att_roll) > random.randint(0, def_roll):
        hit = roll_hit(player, max_hit)
        if hit > 0:
            updated_def_lvl = monster.defenceLvl * 0.65
            monster.defenceLvl = max(updated_def_lvl, monster.cap, 0)  # Ensure defense does not drop below zero
    return monster.defenceLvl
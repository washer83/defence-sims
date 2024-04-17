import random
import math

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
    if tick in player.dwh_hits:
        apply_dwh(player, monster)
    elif tick in player.bgs_hits:
        apply_bgs(player, monster)
    elif tick in player.ralos_hits:
        apply_ralos(player, monster)
    elif tick in player.emaul_hits: 
        apply_emaul(player,monster)
    return monster.defenceLvl

def apply_dwh(player, monster):
    max_hit = player.dwhMax
    att_roll = player.dwhAttRoll
    def_roll = max((monster.defenceLvl + 9) * (monster.crushDefLvl + 64), 1)

    if random.randint(0, att_roll) > random.randint(0, def_roll):
        hit = roll_hit(player, max_hit)
        if hit > 0:
            reduction = math.floor(monster.defenceLvl * 0.7)
            updated_def_lvl = (monster.defenceLvl - reduction)
            monster.defenceLvl = max(updated_def_lvl, monster.cap, 0)  # Ensure defense does not drop below zero
    return monster.defenceLvl

def apply_bgs(player, monster):
    max_hit = player.bgsMax
    att_roll = player.bgsAttRoll
    melee_def_roll = max((monster.defenceLvl + 9) * (monster.slashDefLvl + 64), 1)

    if random.randint(0, int(att_roll)) > random.randint(0, int(melee_def_roll)):
        hit = roll_hit(player, max_hit)
        monster.defenceLvl = max(monster.defenceLvl - hit, monster.cap, 0)  # Also prevent defense from going below 0
    return monster.defenceLvl

def apply_ralos(player, monster):
    max_hit = player.ralosMax
    att_roll = player.ralosAttRoll
    hits_to_apply = 2

    for _ in range(hits_to_apply):
        def_roll = max((monster.defenceLvl + 9) * (monster.rangedDefLvl + 64), 1)
        if random.randint(0, att_roll) > random.randint(0, def_roll):
            hit = roll_hit(player, max_hit)
            if hit > 0:
                monster.defenceLvl = math.ceil(monster.defenceLvl - 0.1 * monster.magicLvl)

    return monster.defenceLvl

def apply_emaul(player, monster):
    max_hit = player.emaulMax
    att_roll = player.emaulAttRoll
    def_roll = max((monster.defenceLvl + 9) * (monster.crushDefLvl + 64), 1)

    if random.randint(0, att_roll) > random.randint(0, def_roll):
        hit = roll_hit(player, max_hit)
        if hit > 0:
            reduction = math.floor(monster.defenceLvl * 0.35)
            updated_def_lvl = (monster.defenceLvl - reduction)
            monster.defenceLvl = max(updated_def_lvl, monster.cap, 0)  # Ensure defense does not drop below zero
    return monster.defenceLvl
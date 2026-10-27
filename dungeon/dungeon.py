import random

prices = {"зелье": 10, "факельное_масло": 15, "боевой_эликсир": 40}

enemy_stats = {
    "скелет":        {"hp": 45, "damage": 6, "loot": 25},
    "упырь":         {"hp": 30, "damage": 4, "loot": 15},
    "паук":          {"hp": 20, "damage": 3, "loot": 10},
    "летучая_мышь":  {"hp": 12, "damage": 2, "loot": 5},
}

def hero_hit(strike_n, damage, crit_damage):
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False

def fight(enemy, hero_health, bonus, damage, crit_damage):
    stats = enemy_stats[enemy]
    enemy_hp = float(stats["hp"])
    rounds = []
    round_n = 0
    print(f"Вы спускаетесь по лестнице. Из темноты появляется {enemy}!")
    
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n, damage, crit_damage)
        hit += bonus
        enemy_hp -= hit
        line = f"Раунд {round_n}: герой наносит {hit:.1f}"
        if crit:
            line += " - КРИТИЧЕСКИЙ УДАР!"
            
        if enemy_hp <= 0:
            line += " Враг повержен."
            rounds.append([round_n, hit, 0])
        else:
            blow = stats["damage"]
            hero_health -= blow
            line += f" Здоровье {enemy}: {enemy_hp:.1f}. {enemy.capitalize()} бьет на {blow}."
            rounds.append([round_n, hit, blow])
        print(line)
        
    won = enemy_hp <= 0
    loot = stats["loot"] if won else 0
        
    return rounds, won, hero_health, loot

def buy(price, gold, quantity=1):
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False

if __name__ == "__main__":
    rounds, won, hp, loot = fight("скелет", 100, 0, 20.5, 41.0)
    print(f"self-test: {len(rounds)} раундов, победа={won}, трофеи={loot}")

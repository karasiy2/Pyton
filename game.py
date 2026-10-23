import random

# =====================================================================
# --- ГЛОБАЛЬНЫЕ НАСТРОЙКИ И ПРАВИЛА ИГРЫ -----------------------------
# =====================================================================

title = "КРУТОЕ ПРИКЛЮЧЕНИЕ"
frame = "=" * 20

print(frame)
print(" " + title + " ")
print(frame)
print()

# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()

print(f"Добро пожаловать, {hero_name}!")
print("Ты появляешься на пустом поле.")
print()

# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")

while True:
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        endurance = int(input())
        if health <= 0:
            raise ValueError(f"Здоровье должно быть положительным, а введено {health}")
        if strength < 0 or agility < 0 or endurance < 0:
            raise ValueError("Характеристики не могут быть отрицательными")
        break
    except ValueError:
        print("Ой: одна из строк не число. Введите все четыре снова:")

# --- Расчёт урона и энергии ------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = endurance // agility

# --- Потолки характеристик (Входные максимумы) ----
max_health = health
max_stamina = stamina

# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье: {health} (макс: {max_health})")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Выносливость: {endurance}")
print()

print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Стамина: {stamina:.1f} (макс: {max_stamina})")
print()

# --- Состояние забега -----------------------------
enemies = ["упырь", "скелет", "паук", "летучая_мышь"]
log = []
gold_total = 100  
ability_bonus = 0

prices = {"зелье": 10, "факельное_масло": 15, "боевой_эликсир": 40}
inventory = {}

enemy_stats = {
    "скелет":        {"hp": 45, "damage": 6, "loot": 25},
    "упырь":         {"hp": 30, "damage": 4, "loot": 15},
    "паук":          {"hp": 20, "damage": 3, "loot": 10},
    "летучая_мышь":  {"hp": 12, "damage": 2, "loot": 5},
}

commands = [
    "осмотреться", "идти", "отдохнуть", "слушать", "факел", "тренировка", "спуститься",
    "лидеры", "магазин", "рюкзак", "выпить зелье",
    "купить <предмет> [количество]", "выход"
]

MENU = [
    "Что делаешь? (введи номер или команду; help для справки)",
    "1 - осмотреться (осмотреться)",
    "2 - идти вперёд (идти)",
    "3 - отдохнуть (отдохнуть)",
    "4 - прислушаться (слушать)",
    "5 - зажечь факел (факел)",
    "6 - тренироваться (тренировка)",
    "7 - спуститься глубже (спуститься)",
    "8 - таблица рекордов (лидеры)",
    "9 - зайти в магазин (магазин)",
    "10 - проверить рюкзак (рюкзак)",
    "11 - выпить зелье (выпить)",
    "0 - выйти из подземелья (выход)"
]

num_to_verb = {
    "1": "осмотреться", "2": "идти", "3": "отдохнуть", "4": "слушать",
    "5": "факел", "6": "тренировка", "7": "спуститься", "8": "лидеры",
    "9": "магазин", "10": "рюкзак", "11": "выпить", "0": "выход"
}

# =====================================================================
# --- ОПРЕДЕЛЕНИЯ ФУНКЦИЙ (ОГЛАВЛЕНИЕ) --------------------------------
# =====================================================================

def hero_hit(strike_n):
    """Рассчитывает урон героя в зависимости от номера удара."""
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero_health, bonus=0):
    """Ведет пошаговый автоматический бой с врагом до гибели одного из участников."""
    stats = enemy_stats[enemy]
    enemy_hp = float(stats["hp"])
    rounds = []
    round_n = 0
    print(f"Вы спускаетесь по лестнице. Из темноты появляется {enemy}!")
    
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n)
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
    """Проводит транзакцию покупки предметов за золото."""
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False


def print_leaderboard(log):
    """Выводит на экран три лучших раунда героя по урону и сильнейший удар врага."""
    if not log:
        print("Вы еще не сражались.")
        return
        
    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print("Таблица лидеров (урон героя):")
    for i in range(len(top)):
        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")
        
    worst = max(log, key=lambda r: r[2])
    print(f"Самый сильный удар врага: {worst[2]} (в раунде {worst[0]}).")


def print_run_summary(log):
    """Рассчитывает и выводит суммарный и средний нанесенный героем урон."""
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Нанесено урона: {total:.1f} за {rounds} раундов, в среднем {total / rounds:.1f} за раунд.")
    else:
        print("В этом прохождении не было сражений.")


# =====================================================================
# --- ГЛАВНЫЙ ИГРОВОЙ ЦИКЛ (СЮЖЕТ) -------------------------------------
# =====================================================================

running = True
actions = 0

try:
    while running:
        print("\n".join(MENU))
        print()
        
        line = input()
        cmd = line.strip().lower()
        while cmd == "":
            print("Пустая команда. Введите команду или номер.")
            line = input()
            cmd = line.strip().lower()
            
        words = cmd.split()
        verb = words[0]
        
        if cmd in num_to_verb:
            verb = num_to_verb[cmd]
            
        match verb:
            case "help":
                print("Доступные команды: " + ", ".join(commands) + ".")
                print("Номера 0-11 работают как и прежде.")
                print()
                continue 
                
            case "осмотреться":
                print("Вы осматриваетесь вокруг. Комната пуста, на полу лишь пыль.")
                
            case "идти":
                cost = 2
                if stamina >= cost:
                    stamina -= cost
                    print("Вы осторожно идёте вперёд. Пол скрипит под ногами.")
                else:
                    health -= cost - stamina
                    stamina = 0
                    print("Сил больше нет — вы идёте на одном упорстве.")
                    
            case "отдохнуть":
                stamina = min(stamina + 2, max_stamina)
                print("Вы успешно отдохнули и набрались сил!")
                
            case "слушать":
                print("Вы прислушались. Слышен далёкий шорох и капли воды.")
                
            case "факел":
                stamina = stamina - 7
                print("Вы зажгли факел и осмотрели стены.")
                
            case "тренировка":
                strikes = 5
                total_damage = 0
                crit_count = 0
                print("Вы подходите к дереву.")
                print(f"Наносите {strikes} ударов.")
                for i in range(1, strikes + 1):
                    hit_damage, crit = hero_hit(i)
                    if crit:
                        crit_count += 1
                        print(f"Удар {i}: {hit_damage:.1f} — критический!")
                    else:
                        print(f"Удар {i}: {hit_damage:.1f}")
                    total_damage += hit_damage
                print(f"Всего нанесено урона на тренировке: {total_damage:.1f} (Критов: {crit_count})")
                print()
                
            case "спуститься": 
                if not enemies:
                    print("Вы спускаетесь по лестнице. Но подземелье уже пусто.")
                else:
                    enemy = random.choice(enemies)
                    rounds, won, health, loot = fight(enemy, health, bonus=ability_bonus)
                    
                    for r in rounds:
                        log.append(r)
                        
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        print(f"{enemy.capitalize()} побежден! В подземелье осталось врагов: {len(enemies)}.")
                    print(f"Бой длился: {len(rounds)} раундов.")
                    
            case "лидеры":
                print_leaderboard(log)
                
            case "магазин":
                print("Магазин:")
                for name, price in prices.items():
                    print(f"{name}: {price} золота")
                print()
                continue
                
            case "купить":
                if len(words) > 1 and words[-1].isdigit():
                    qty = int(words[-1])
                    item = "_".join(words[1:-1])
                else:
                    qty = 1
                    item = "_".join(words[1:])
                    
                if item == "":
                    print("Купить что? Пример ввода: купить зелье.")
                    continue
                    
                if item not in prices:
                    print("Такого предмета нет в магазине.")
                    continue
                    
                gold_total, ok = buy(prices[item], gold_total, quantity=qty)
                if ok:
                    inventory[item] = inventory.get(item, 0) + qty
                    print(f"Куплено {qty} шт. '{item}' за {prices[item] * qty} золота. Осталось золота: {gold_total}.")
                else:
                    print(f"Недостаточно золота: требуется {prices[item] * qty}, у вас есть {gold_total}.")
                    
            case "рюкзак":
                if not inventory:
                    print("Рюкзак пуст.")
                else:
                    print("Содержимое рюкзака:")
                    for name, qty in inventory.items():
                        print(f"{name}: {qty} шт.")
                        
            case "выпить":
                item = "_".join(words[1:]) or "зелье"
                if inventory.get(item, 0) == 0:
                    print(f"В рюкзаке нет предмета '{item}'.")
                else:
                    health = min(health + 10, max_health)
                    inventory[item] -= 1
                    if inventory[item] == 0:
                        del inventory[item]
                    print(f"Вы выпили '{item}'. Здоровье: {health}. Осталось в рюкзаке: {inventory.get(item, 0)} шт.")
                    
            case "выход":
                print("Вы поднимаетесь обратно к свету. Подземелье остается позади.")
                running = False
                
            case _:
                # Ветка Блока 4: Вывод исходной (line), а не отформатированной строки
                print(f"Не понимаю команду: '{line.strip()}'. Введите 'help' для справки.")
                continue  # Ошибочный ввод не тратит круг
                
        if health <= 0:
            print(f"{hero_name} падает без сил. Подземелье забирает ещё одного искателя.")
            running = False        
        if running:
            actions += 1

finally:
    print()
    print(frame)
    if health <= 0:
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
        
    print_run_summary(log)
    print(f"Здоровье: {health}/{max_health} Стамина: {stamina}/{max_stamina} Осталось врагов: {len(enemies)} Золото: {gold_total}")
    
    if inventory:
        print("Оставлено в рюкзаке:")
        for name, qty in inventory.items():
            print(f"{name}: {qty} шт.")
    else:
        print("Оставлено в рюкзаке: ничего.")
    print(frame)

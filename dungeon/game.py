import random
import dungeon

try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False

title = "КРУТОЕ ПРИКЛЮЧЕНИЕ"
frame = "=" * 20

print(frame)
print(" " + title + " ")
print(frame)
print()

print("Как зовут героя?")
hero_name = input()

print(f"Добро пожаловать, {hero_name}!")
print("Ты появляешься на пустом поле.")
print()

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

base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = endurance // agility

max_health = health
max_stamina = stamina

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

enemies = ["упырь", "скелет", "паук", "летучая_мышь"]
log = []
gold_total = 100  
ability_bonus = 0

inventory = {}

MAP = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "#", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", "#", "S", ".", "#"],
]

hero_r, hero_c = 4, 2
visited = {(4, 2)}

DIRECTIONS = {"north": (-1, 0), "south": (1, 0), "west": (0, -1), "east": (0, 1)}

LOOT = {(1, 1): "старая_монета", (2, 3): "пыльное_зелье", (3, 3): "амулет_стража"}
found_loot = set()

commands = [
    "осмотреться", "идти [направление]", "отдохнуть", "слушать", "факел", "тренировка", "спуститься",
    "лидеры", "магазин", "рюкзак", "выпить зелье", "карта", "разведка",
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
    "12 - показать карту (карта)",
    "13 - запустить разведку (разведка)",
    "0 - выйти из подземелья (выход)"
]

num_to_verb = {
    "1": "осмотреться", "2": "идти", "3": "отдохнуть", "4": "слушать",
    "5": "факел", "6": "тренировка", "7": "спуститься", "8": "лидеры",
    "9": "магазин", "10": "рюкзак", "11": "выпить", "12": "карта", "13": "разведка", "0": "выход"
}

def print_leaderboard(log):
    if not log:
        print("Вы еще не сражались.")
        return
        
    top = sorted(log, key=lambda r: r, reverse=True)[:3]
    print("Таблица лидеров (урон героя):")
    for i in range(len(top)):
        print(f"{i + 1}. Раунд {top[i]}: {top[i]:.1f}")
        
    worst = max(log, key=lambda r: r)
    print(f"Самый сильный удар врага: {worst} (в раунде {worst}).")

def print_run_summary(log):
    total = sum(r for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Нанесено урона: {total:.1f} за {rounds} раундов, в среднем {total / rounds:.1f} за раунд.")
    else:
        print("В этом прохождении не было сражений.")

def scout(r, c, seen):
    if (r, c) in seen or MAP[r][c] == "#":
        return 0
    seen.add((r, c))
    total = 1
    for dr, dc in DIRECTIONS.values():
        total += scout(r + dr, c + dc, seen)
    return total

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
        verb = words
        
        if cmd in num_to_verb:
            verb = num_to_verb[cmd]
            
        match verb:
            case "help":
                print("Доступные команды: " + ", ".join(commands) + ".")
                print("Номера 0-13 работают как и прежде.")
                print()
                continue
                
            case "осмотреться":
                print("Вы осматриваетесь вокруг. Комната пуста, на полу лишь пыль.")
                
            case "идти":
                if len(words) > 1 and words in DIRECTIONS:
                    dr, dc = DIRECTIONS[words]
                    nr, nc = hero_r + dr, hero_c + dc
                    if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and MAP[nr][nc] != "#":
                        hero_r, hero_c = nr, nc
                        visited.add((hero_r, hero_c))
                        print(f"Ты шагаешь на {words}. Комната ({hero_r}, {hero_c}).")
                        
                        if (hero_r, hero_c) in LOOT:
                            item = LOOT[(hero_r, hero_c)]
                            if item not in found_loot:
                                found_loot.add(item)
                                print(f"Ты находишь предмет: {item}! Уникальный лут: {len(found_loot)}.")
                    else:
                        print(f"Не могу идти на {words}: стена или край карты.")
                else:
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
                    hit_damage, crit = dungeon.hero_hit(i, damage, crit_damage)
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
                    rounds, won, health, loot = dungeon.fight(enemy, health, ability_bonus, damage, crit_damage)
                    
                    for r in rounds:
                        log.append(r)
                        
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        win_msg = f"{enemy.capitalize()} побежден! В подземелье осталось врагов: {len(enemies)}."
                        if COLOR:
                            print(Fore.BLUE + win_msg + Style.RESET_ALL)
                        else:
                            print(win_msg)
                    print(f"Бой длился: {len(rounds)} раундов.")
                    
            case "лидеры":
                print_leaderboard(log)
                
            case "магазин":
                print("Магазин:")
                for name, price in dungeon.prices.items():
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
                    
                if item not in dungeon.prices:
                    print("Такого предмета нет в магазине.")
                    continue
                    
                gold_total, ok = dungeon.buy(dungeon.prices[item], gold_total, quantity=qty)
                if ok:
                    inventory[item] = inventory.get(item, 0) + qty
                    print(f"Куплено {qty} шт. '{item}' за {dungeon.prices[item] * qty} золота. Осталось золота: {gold_total}.")
                else:
                    print(f"Недостаточно золота: требуется {dungeon.prices[item] * qty}, у вас есть {gold_total}.")
                    
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
                    
            case "карта":
                print("Карта:")
                for i in range(len(MAP)):
                    cells = []
                    for j in range(len(MAP[i])):
                        cell = "@" if (i, j) == (hero_r, hero_c) else MAP[i][j]
                        cells.append(cell)
                    print(" ".join(cells))
                print()
                continue
                
            case "разведка":
                seen = set()
                print(f"Разведка: доступно комнат для посещения — {scout(hero_r, hero_c, seen)}.")
                print()
                continue
                
            case "выход":
                print("Вы поднимаетесь обратно к свету. Подземелье остается позади.")
                running = False
                
            case _:
                print(f"Не понимаю команду: '{line.strip()}'. Введите 'help' для справки.")
                continue
                
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
    
    state = f"Здоровье: {health}/{max_health} Стамина: {stamina}/{max_stamina} Осталось врагов: {len(enemies)} Золото: {gold_total}"
    if COLOR:
        print(Fore.GREEN + state + Style.RESET_ALL)
    else:
        print(state)
        
    if inventory:
        print("Оставлено в рюкзаке:")
        for name, qty in inventory.items():
            print(f"{name}: {qty} шт.")
    else:
        print("Оставлено в рюкзаке: ничего.")
    print(frame)

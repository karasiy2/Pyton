import random
# --- Заголовок ------------------------------------

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
# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = endurance // agility

# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Ловкость: {agility}")
print(f"Выносливость: {endurance}")

print()

print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Стамина: {stamina:.1f}")

print()

# --- Блок 1. Список врагов и журнал боя ---
enemies = ["ghoul", "skeleton", "spider", "bat"]
log = []

running = True
actions = 0

try:
    while running:
        # --- Меню действий ---------------------------------
        print("Что делаешь?")

        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - копать")
        print("5 - отжаться")
        print("6 - тренировка")
        print("7 - зайти глубже в лес")
        print("8 - leaderboard")
        print("0 - выйти из подземелья")

        print()
        # --- Выбор героя -----------------------------------
        menu_last = 8
        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Такого пункта нет. Введи номер пункта из меню.")
                continue
            if 0 <= menu_number <= menu_last:
                break
            print("Такого пункта нет. Введи номер пункта из меню.")
        match choice:
            case "1":
                print("Вы осмотрелись. Впереди виден лес.")
            case "2":
                cost = 2
                if stamina >= cost:
                    stamina -= cost
                    print("Вы осторожно идёте вперёд. Пол скрипит под ногами.")
                else:
                    health -= cost - stamina
                    stamina = 0
                    print("Сил больше нет — вы идёте на одном упорстве.")
            case "3":
                stamina = stamina + 2
                print("Вы успешно отдохнули и набрались сил!")
            case "4":
                stamina = stamina - 7
                print("Вы успешно покопали.")
            case "5":
                stamina = stamina - 8
                strength = strength + 2
                print("Вы отжались и стали сильнее!")
            case "6":
                strikes = 1
                total_damage = 0
                crit_count = 0
                print("Вы подходите к дереву.")
                print()
            case "7": 
                print("Вы забираетесь глубже в лес...")
                
                if not enemies:
                    print("...но врагов больше нет.")
                else:
                    enemy = random.choice(enemies)
                    enemy_hp = 45
                    round_n = 0
                    
                    print(f"{enemy} появляется из темноты!")
                    
                    hero_strikes = 0
                    
                    # Цикл боя
                    while enemy_hp > 0 and health > 0:
                        round_n += 1
                        hero_strikes += 1
                        
                        if hero_strikes % 3 == 0:
                            hit = crit_damage
                            is_crit = True
                        else:
                            hit = damage
                            is_crit = False
                            
                        enemy_hp -= hit
                        
                        # Формируем человекочитаемый текст
                        crit_text = " (critical!)" if is_crit else ""
                        
                        if enemy_hp <= 0:
                            # Враг пал, урон врага равен 0
                            line = f"Round {round_n}: hero hits {hit:.1f}{crit_text}. Enemy HP: 0. Enemy falls."
                            log.append([round_n, hit, 0])
                            print(line)
                            break
                        else:
                            blow = random.randint(2, 6)
                            health -= blow
                            line = f"Round {round_n}: hero hits {hit:.1f}{crit_text}, enemy hits {blow}. Enemy health: {enemy_hp:.1f}. {enemy.capitalize()} hits for {blow}."
                            log.append([round_n, hit, blow])
                            print(line)
                    
                    if enemy_hp <= 0:
                        enemies.remove(enemy)
                        print(f"The {enemy} is defeated! {len(enemies)} enemies left in the dungeon.")
                    
                    if log:
                        print(f"Последняя строка боя (в виде чисел из журнала): {log[-1]}")
                        
                    print(f"Combat: {round_n} rounds.")
                    
            case "8":
                if not log:
                    print("Ты еще не сражался")
                else:
                    top = sorted(log, key=lambda r: r, reverse=True)[:3]
                    print("Leaderboard:")
                    for i in range(len(top)):
                        print(f"{i + 1}. Round {top[i]}: {top[i]:.1f}")
                    
                    worst = max(log, key=lambda r: r)
                    print(f"Самый сильный удар по врагу: {worst}.")
                    
            case "0":
                print("Вы решили выйти.")
                running = False

            case _:
                print("Такого действия нет.")
        if health <= 0:
            print(f"{hero_name} падает без сил. Подземелье забирает ещё одного искателя.")
            running = False        
        if running:
            actions += 1

finally:
    print()
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Damage: {total:.1f} across {rounds} rounds, average {total / rounds:.1f}.")
    else:
        print("Вы не дрались в этом прохождении.")

    print()
    print(f"Здоровье: {health} Запас сил: {stamina}")

    # --- Прощание ---
    print(frame)
    if health <= 0:
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    print(frame)

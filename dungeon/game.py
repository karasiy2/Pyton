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
    print("0 - выйти из подземелья")

    print()
    # --- Выбор героя -----------------------------------
    menu_last = 7
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
                        current_damage = crit_damage
                        is_crit = True
                    else:
                        current_damage = damage
                        is_crit = False
                        
                    enemy_hp -= current_damage
                    
                    if enemy_hp <= 0:
                        if is_crit:
                            print(f"Round {round_n}: hero hits {current_damage:.1f} (critical!). Enemy HP: 0. critical! The enemy falls.")
                        else:
                            print(f"Round {round_n}: hero hits {current_damage:.1f}. Enemy HP: 0. The enemy falls.")
                        
                        log.append(f"round {round_n}: hero -{current_damage:.1f}, {enemy} -0")
                        break
                    
                    enemy_damage = random.randint(2, 6)
                    health -= enemy_damage
                    
                    if is_crit:
                        print(f"Round {round_n}: hero hits {current_damage:.1f} (critical!), enemy hits {enemy_damage}. Enemy HP: {enemy_hp:.1f}")
                    else:
                        print(f"Round {round_n}: hero hits {current_damage:.1f}, enemy hits {enemy_damage}. Enemy HP: {enemy_hp:.1f}")
                    
                    log.append(f"round {round_n}: hero -{current_damage:.1f}, {enemy} -{enemy_damage}")
                
                if enemy_hp <= 0:
                    enemies.remove(enemy)
                    print(f"The {enemy} is defeated! {len(enemies)} enemies left in the dungeon.")
                
                if log:
                    print(f"Последняя строка боя: {log[-1]}")
                    
                print(f"Combat: {round_n} rounds.")
                
        case "0":
            print("Вы упали в обморок.")
            running = False

            print(f"Наносите {strikes} ударов.")

            for i in range(1, strikes + 1):
                if i % 3 == 0:
                    hit_damage = crit_damage
                else:
                    hit_damage = damage

                if i % 3 == 0:
                    print(f"Удар {i}: вы нанесли {hit_damage} урона — критический!")
                else:
                    print(f"Удар {i}: вы нанесли {hit_damage} урона")
                    total_damage += hit_damage

        case _:
            print("Такого действия нет.")
    if health <= 0:
        print(f"{hero_name} падает без сил. Подземелье забирает ещё одного искателя.")
        running = False        
    if running:
        actions += 1
print()
print(f"Здоровье: {health} Запас сил: {stamina}")

# --- Прощание ---
frames = "=" * 20

print(frame)
if health <= 0:
    print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
else:
    print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
print(frame)

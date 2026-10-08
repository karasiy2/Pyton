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
enemies = ["ghoul", "skeleton", "spider", "bat"]
log = []
gold_total = 0
ability_bonus = 0

# =====================================================================
# --- ОПРЕДЕЛЕНИЯ ФУНКЦИЙ (ОГЛАВЛЕНИЕ) --------------------------------
# =====================================================================

def hero_hit(strike_n):
    """Рассчитывает урон героя в зависимости от номера удара.
    
    Принимает:
        strike_n (int) — порядковый номер удара.
    Возвращает:
        tuple (float, bool) — пару (урон, признак критического удара).
    Описание:
        Ничего не печатает. Читает глобальные правила игры damage и crit_damage.
    """
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero_health, bonus=0):
    """Ведет пошаговый автоматический бой с врагом до гибели одного из участников.
    
    Принимает:
        enemy (str) — имя врага.
        hero_health (int) — текущее здоровье героя на момент начала боя.
        bonus (int/float, по умолчанию 0) — постоянная надбавка к урону (без эликсира = 0).
    Возвращает:
        tuple (list, bool, int, int) — кортеж из четырех элементов по именам:
            - rounds (list): таблица раундов боя для журнала.
            - won (bool): True, если враг пал, иначе False.
            - hero_health (int): обновленное здоровье героя после боя.
            - loot (int): количество добытого золота (трофеи за победу).
    Описание:
        Активно печатает ход сражения по раундам в консоль через f-строки.
        Переменная bonus прибавляется после расчета критического удара.
        Глобальные переменные не меняет, отдавая результаты через return.
    """
    enemy_hp = 45.0
    rounds = []
    round_n = 0
    print(f"You descend the stairs. Out of the darkness comes {enemy}!")
    
    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n)
        hit += bonus
        enemy_hp -= hit
        line = f"Round {round_n}: hero deals {hit:.1f}"
        if crit:
            line += " - critical!"
            
        if enemy_hp <= 0:
            line += " Enemy falls."
            rounds.append([round_n, hit, 0])
        else:
            blow = random.randint(2, 6)
            hero_health -= blow
            line += f" {enemy} health: {enemy_hp:.1f}. {enemy.capitalize()} hits for {blow}."
            rounds.append([round_n, hit, blow])
        print(line)
        
    won = enemy_hp <= 0
    if won:
        loot = 10 + 5 * round_n
    else:
        loot = 0
        
    return rounds, won, hero_health, loot


def buy(price, gold, quantity=1):
    """Проводит транзакцию покупки предметов за золото.
    
    Принимает:
        price (int) — цена одной штуки товара.
        gold (int) — текущий запас золота у героя.
        quantity (int, по умолчанию 1) — количество покупаемого товара.
    Возвращает:
        tuple (int, bool) — пару (gold_left, ok): остаток золота и признак успешности покупки.
    Описание:
        Ничего не печатает. Чек и сообщения об ошибках выводятся вызывающей веткой меню.
    """
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False


def print_leaderboard(log):
    """Выводит на экран три лучших раунда героя по урону и сильнейший удар врага.
    
    Принимает:
        log (list) — глобальный журнал таблицы чисел всех раундов.
    Возвращает:
        None — контракт функции подразумевает исключительно вывод текста в консоль.
    Описание:
        Безопасно прерывает работу через пустой return, если журнал пуст.
        Выполняет устойчивую сортировку и поиск максимума по ключам через lambda.
    """
    if not log:
        print("You haven't fought yet.")
        return
        
    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print("Leaderboard (hero damage):")
    for i in range(len(top)):
        print(f"{i + 1}. Round {top[i][0]}: {top[i][1]:.1f}")
        
    worst = max(log, key=lambda r: r[2])
    print(f"Strongest enemy hit: {worst[2]} (round {worst[0]}).")


def print_run_summary(log):
    """Рассчитывает и выводит суммарный и средний нанесенный героем урон за весь забег.
    
    Принимает:
        log (list) — глобальный журнал таблицы чисел всех раундов.
    Возвращает:
        None — контракт функции подразумевает только вывод текста.
    Описание:
        Безопасна на пустом журнале: защищена ветвлением от ZeroDivisionError.
        Вынимает колонку урона героя напрямую через генератор в функцию sum().
    """
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Damage: {total:.1f} across {rounds} rounds, average {total / rounds:.1f}.")
    else:
        print("No battles this run.")


# =====================================================================
# --- ГЛАВНЫЙ ИГРОВОЙ ЦИКЛ (СЮЖЕТ) -------------------------------------
# =====================================================================

running = True
actions = 0

try:
    while running:
        print("What do you do?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - копать")
        print("5 - отжаться")
        print("6 - тренировка")
        print("7 - зайти глубже в лес")
        print("8 - leaderboard")
        print("9 - shop")
        print("0 - выйти из подземелья")
        print()
        
        menu_last = 9
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
                stamina = min(stamina + 2, max_stamina)
                print("Вы успешно отдохнули и набрались сил!")
            case "4":
                stamina = stamina - 7
                print("Вы успешно покопали.")
            case "5":
                stamina = stamina - 8
                strength = strength + 2
                print("Вы отжались и стали сильнее!")
            case "6":
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
            case "7": 
                if not enemies:
                    print("You descend the stairs. But the dungeon is empty.")
                else:
                    enemy = random.choice(enemies)
                    rounds, won, health, loot = fight(enemy, health, bonus=ability_bonus)
                    
                    for r in rounds:
                        log.append(r)
                        
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        print(f"{enemy.capitalize()} defeated! {len(enemies)} enemies left in the dungeon.")
                    print(f"Battle: {len(rounds)} rounds.")
                    
            case "8":
                print_leaderboard(log)
                
            case "9":
                print("Shop:")
                print("1 - potion (+10 health): 10 gold")
                print("2 - torch oil (+5 stamina): 15 gold")
                print("3 - war elixir (+2 damage for the run): 40 gold")
                print("Item number (0 - not buying):")
                item = input()
                prices = (10, 15, 40)
                names = ("potion", "torch oil", "war elixir")
                if item in ("1", "2", "3"):
                    price = prices[int(item) - 1]
                    name = names[int(item) - 1]
                    print("Quantity (Enter for one):")
                    qty_line = input()
                    if qty_line == "":
                        qty = 1
                        gold_total, ok = buy(price, gold_total)
                    else:
                        qty = int(qty_line)
                        gold_total, ok = buy(price, gold_total, quantity=qty)
                    
                    if ok:
                        if item == "1":
                            health = min(health + 10 * qty, max_health)
                        elif item == "2":
                            stamina = min(stamina + 5 * qty, max_stamina)
                        else:
                            ability_bonus += 2 * qty
                        print(f"Bought {qty} {name} for {price * qty} gold. Gold left: {gold_total}.")
                    else:
                        print(f"Not enough gold: need {price * qty}, have {gold_total}.")
                elif item != "0":
                    print("No such item in the shop.")
                    
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
    print(frame)
    if health <= 0:
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
        
    print_run_summary(log)
    print(f"Health: {health}/{max_health} Stamina: {stamina}/{max_stamina} Enemies left: {len(enemies)} Gold: {gold_total}")
    print(frame)

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
# --- Меню действий ---------------------------------
print("Что делаешь?")

print("1 - осмотреться")
print("2 - идти вперёд")
print("3 - отдохнуть")
print("4 - копать")
print("5 - отжаться")

print()
# --- Выбор героя -----------------------------------

choice = input()
print()

# --- Прощание ---
titles = f"Прощай, {hero_name}!"
frames = "=" * 20

print(frames)
print(" " + titles + " ")
print(frames)

# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")
health = int(input())
strength = int(input())
agility = int(input())
endurance = int(input())

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
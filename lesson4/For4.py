price = float(input())

for kg in range(1, 11):
    cost = kg * price
    print(f"Стоимость {kg} кг: {cost:.2f}")

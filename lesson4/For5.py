price = float(input())

for i in range(1, 11):
    kg = i / 10
    cost = kg * price
    print(f"Стоимость {kg:.1f} кг: {cost:.2f}")

price = float(input())

for i in range(6, 11):
    kg = i * 0.2
    cost = kg * price
    print(f"Стоимость {kg:.1f} кг: {cost:.2f}")

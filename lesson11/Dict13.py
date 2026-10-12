n = int(input("Введите N: "))
warehouse = {}

for _ in range(n):
    name, price, quantity = input("Введите название, цену и количество: ").split()
    warehouse[name] = [float(price), int(quantity)]

total_cost = 0.0
most_expensive_item = None
max_item_cost = float('-inf')

for name, (price, quantity) in warehouse.items():
    item_total_cost = price * quantity
    total_cost += item_total_cost
    
    if item_total_cost > max_item_cost:
        max_item_cost = item_total_cost
        most_expensive_item = name

print("Суммарная стоимость склада:", total_cost)
print("Самый дорогой по общей стоимости предмет:", most_expensive_item)

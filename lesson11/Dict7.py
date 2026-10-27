n = int(input("Введите N: "))
my_dict = {}
for _ in range(n):
    key, value = input("Введите пару: ").split()
    my_dict[key] = float(value)

max_key = None
max_value = float('-inf')

for key, value in my_dict.items():
    if value > max_value:
        max_value = value
        max_key = key

print("Ключ с наибольшим значением:", max_key)

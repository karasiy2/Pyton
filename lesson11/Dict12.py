n = int(input("Введите N: "))
my_dict = {}
for _ in range(n):
    key, value = input("Введите пару: ").split()
    my_dict[key] = value

reversed_dict = {}
for key, value in my_dict.items():
    reversed_dict[value] = key

print("Обращенный словарь:")
for value, key in reversed_dict.items():
    print(f"{value}: {key}")

n = int(input("Введите N: "))
my_dict = {}

for _ in range(n):
    key, value = input("Введите пару: ").split()
    my_dict[key] = float(value)

v = float(input("Введите число V: "))

keys_to_remove = []
for key, value in my_dict.items():
    if value < v:
        keys_to_remove.append(key)

for key in keys_to_remove:
    del my_dict[key]

print("Размер словаря после удаления:", len(my_dict))

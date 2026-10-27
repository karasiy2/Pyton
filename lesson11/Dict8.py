n = int(input("Введите N: "))
my_dict = {}
for _ in range(n):
    key, value = input("Введите пару: ").split()
    my_dict[key] = int(value)

v = int(input("Введите число V: "))

print(v in my_dict.values())

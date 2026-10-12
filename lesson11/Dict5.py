n = int(input("Введите N: "))
my_dict = {}
for _ in range(n):
    key, value = input("Введите пару: ").split()
    my_dict[key] = value

k = input("Введите ключ K: ")

my_dict.pop(k, None)

print("Размер словаря:", len(my_dict))

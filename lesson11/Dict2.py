n = int(input("Введите N: "))

my_dict = {}
for _ in range(n):
    key, value = input("Введите пару: ").split()
    my_dict[key] = value

k = input("Введите ключ K: ")

if k in my_dict:
    print(my_dict[k])
else:
    print("нет такого ключа")

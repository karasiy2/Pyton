n = int(input("Введите N: "))
my_dict = {}
for _ in range(n):
    key, value = input("Введите пару: ").split()
    my_dict[key] = int(value) 

k = input("Введите K: ")

print(my_dict.get(k, 0))

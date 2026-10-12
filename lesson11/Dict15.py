n = int(input("Введите количество пар первого словаря (N): "))
dict1 = {}
for _ in range(n):
    key, value = input("Словарь 1 - введите ключ и значение через пробел: ").split()
    dict1[key] = value

m = int(input("Введите количество пар второго словаря (M): "))
dict2 = {}
for _ in range(m):
    key, value = input("Словарь 2 - введите ключ и значение через пробел: ").split()
    dict2[key] = value

ignored_count = 0

for key, value in dict2.items():
    if key not in dict1:
        dict1[key] = value
    else:
        ignored_count += 1

print("Размер результирующего словаря:", len(dict1))
print("Число проигнорированных пар:", ignored_count)

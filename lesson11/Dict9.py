n = int(input("Введите N: "))
dict1 = {}
for _ in range(n):
    key, value = input("Словарь 1, пара: ").split()
    dict1[key] = value

m = int(input("Введите M: "))
dict2 = {}
for _ in range(m):
    key, value = input("Словарь 2, пара: ").split()
    dict2[key] = value

common_key = None
for key in dict1:
    if key in dict2:
        common_key = key
        break

dict1.update(dict2)

print("Размер результата:", len(dict1))
print(f"Значение общего ключа '{common_key}':", dict1[common_key])

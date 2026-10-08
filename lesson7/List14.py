A = [5, 3, 7, 3, 8]
D = 3

count_D = A.count(D)

if D in A:
    first_index = A.index(D)
else:
    first_index = -1

print(f"Число вхождений {D}: {count_D}")
print(f"Индекс первого вхождения: {first_index}")

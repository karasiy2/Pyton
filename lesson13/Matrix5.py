M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
D = float(input("Введите число D: "))
print(f"Введите {M} чисел для первого столбца:")
initial_col = [float(input()) for _ in range(M)]

matrix = []
for i in range(M):
    row = []
    start_value = initial_col[i]
    for j in range(N):
        row.append(start_value + j * D)
    matrix.append(row)

print("\nРезультирующая матрица:")
for row in matrix:
    print(*(f"{x:g}" for x in row))

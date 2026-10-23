M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
Q = float(input("Введите число Q: "))
print(f"Введите {N} чисел для первой строки через пробел:")
first_row = list(map(float, input().split()))

matrix = []
for i in range(M):
    row = [val * (Q ** i) for val in first_row]
    matrix.append(row)

print("\nРезультирующая матрица:")
for row in matrix:
    print(*(f"{x:g}" for x in row))

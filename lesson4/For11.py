N = int(input())

total_sum = 0

for i in range(N, 2 * N + 1):
    total_sum += i ** 2

print(f"Сумма квадратов от {N} до {2*N} равна: {total_sum}")

N = int(input())

total_sum = 0.0
sign = 1.0

for i in range(1, N + 1):
    term = 1.0 + i * 0.1
    total_sum += sign * term
    sign = -sign 

print(f"Значение выражения: {total_sum:.6f}")

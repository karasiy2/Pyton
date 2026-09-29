N = int(input())

product = 1

for i in range(1, N + 1):
    factor = 1 + i * 0.1
    product *= factor

print(f"Произведение {N} сомножителей равно: {product:.6f}")

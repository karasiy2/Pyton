A = float(input("Введите вещественное число A: "))
N = int(input("Введите целое число N (> 0): "))

result = 1.0

for _ in range(N):
    result *= A

print(f"Число {A} в степени {N} равно: {result:.6f}")

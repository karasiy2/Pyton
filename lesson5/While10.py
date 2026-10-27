N = int(input())

K = 0
power = 1

# Проверяем, будет ли СЛЕДУЮЩАЯ степень меньше N
while power * 3 < N:
    power *= 3
    K += 1

print(f"Наибольшее число K = {K}")

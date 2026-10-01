N = int(input())

K = 1
power = 3

while power <= N:
    power *= 3
    K += 1

print(f"Наименьшее число K = {K}")

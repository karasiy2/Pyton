N = int(input())

K = 0

while N > 1:
    N = N // 2
    K += 1

print(f"Показатель степени K = {K}")

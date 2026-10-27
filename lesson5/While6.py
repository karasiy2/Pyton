N = int(input())

result = 1.0

while N > 0:
    result = result * N 
    N = N - 2

print(f"Двойной факториал: {result}")

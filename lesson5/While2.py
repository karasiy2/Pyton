A = float(input())
B = float(input())

count = 0

while A >= B:
    A -= B
    count += 1

print(f"Количество размещенных отрезков B: {count}")

A = float(input())

K = 0
current_sum = 0

while current_sum <= A:
    K += 1
    current_sum += 1 / K

print(f"Наименьшее число K: {K}")
print(f"Полученная сумма: {current_sum}")

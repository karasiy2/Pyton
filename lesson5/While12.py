N = int(input())

K = 0
current_sum = 0

while current_sum + (K + 1) <= N:
    K += 1
    current_sum += K

print(f"Наибольшее число K: {K}")
print(f"Полученная сумма: {current_sum}")

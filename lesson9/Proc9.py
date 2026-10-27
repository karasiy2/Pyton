def add_left_digit(d, k):
    return int(str(d) + str(k))

K = 452
D1, D2 = 1, 8

print(f"Исходное число: {K}")
K = add_left_digit(D1, K)
print(f"Шаг 1 (приписали {D1} слева): {K}")
K = add_left_digit(D2, K)
print(f"Шаг 2 (приписали {D2} слева): {K}")

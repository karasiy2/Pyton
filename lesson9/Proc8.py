def add_right_digit(d, k):
    return k * 10 + d

K = 452
D1, D2 = 7, 9

print(f"Исходное число: {K}")
K = add_right_digit(D1, K)
print(f"Шаг 1 (приписали {D1}): {K}")
K = add_right_digit(D2, K)
print(f"Шаг 2 (приписали {D2}): {K}")

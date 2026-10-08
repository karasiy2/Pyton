def sum_range(a, b):
    if a > b:
        return 0
    return sum(range(a, b + 1))

A, B, C = 5, 10, 15
print(f"Сумма от {A} до {B}:", sum_range(A, B))
print(f"Сумма от {B} до {C}:", sum_range(B, C))

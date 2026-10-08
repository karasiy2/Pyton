def is_power_n(k, n):
    if k <= 0 or n <= 1: return False
    while k % n == 0:
        k //= n
    return k == 1

n = 3
numbers = [1, 3, 6, 9, 12, 27, 30, 81, 2, 5]
count = sum(1 for x in numbers if is_power_n(x, n))

print(f"Количество степеней числа {n} в наборе:", count)

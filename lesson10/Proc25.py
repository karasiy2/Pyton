import math

def is_square(k):
    if k <= 0: return False
    root = int(math.isqrt(k))
    return root * root == k

numbers = [4, 5, 9, 10, 16, 20, 25, 30, 36, 100]
squares_count = sum(1 for x in numbers if is_square(x))

print("Количество полных квадратов в наборе:", squares_count)

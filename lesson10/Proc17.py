def roots_count(a, b, c):
    D = b**2 - 4 * a * c
    if D > 0:
        return 2
    elif D == 0:
        return 1
    else:
        return 0

equations = [(1, -3, 2), (1, 2, 1), (1, 1, 5)]
for a, b, c in equations:
    print(f"Для {a}x^2 + ({b})x + ({c}) = 0 корней:", roots_count(a, b, c))

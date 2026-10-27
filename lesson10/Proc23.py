def quarter(x, y):
    if x > 0 and y > 0: return 1
    if x < 0 and y > 0: return 2
    if x < 0 and y < 0: return 3
    if x > 0 and y < 0: return 4

points = [(2, 3), (-4, 5), (1, -2)]
for x, y in points:
    print(f"Точка ({x}, {y}) находится в четверти:", quarter(x, y))

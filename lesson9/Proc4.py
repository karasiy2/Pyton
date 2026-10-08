import math

def triangle_ps(a):
    P = 3 * a
    S = (a**2 * math.sqrt(3)) / 4
    return P, S

sides = [4, 6, 10]
for side in sides:
    perim, area = triangle_ps(side)
    print(f"Сторона {side}: Периметр = {perim:.2f}, Площадь = {area:.2f}")

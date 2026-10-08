def rect_ps(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    P = 2 * (width + height)
    S = width * height
    return P, S

rectangles = [
    (0, 0, 4, 3),
    (-1, -1, 2, 5),
    (10, 5, 5, 15)
]

for coords in rectangles:
    perim, area = rect_ps(*coords)
    print(f"Прямоугольник {coords}: Периметр = {perim}, Площадь = {area}")

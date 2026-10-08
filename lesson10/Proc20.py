import math

def triangle_p(a, h):
    b = math.sqrt((a / 2)**2 + h**2)
    return a + 2 * b

triangles = [(6, 4), (10, 12), (3, 5)]
for a, h in triangles:
    print(f"Периметр треугольника ({a}, {h}): {triangle_p(a, h):.2f}")

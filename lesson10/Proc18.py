def circle_s(r):
    return 3.14 * (r**2)

radii = [2, 5, 1.5]
for r in radii:
    print(f"Площадь круга радиуса {r}:", circle_s(r))

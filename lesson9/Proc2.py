def power_a234(a):
    return a**2, a**3, a**4

numbers = [2, 3, 5, 10, 1.5]
for n in numbers:
    p2, p3, p4 = power_a234(n)
    print(f"Число {n}: квадрат = {p2}, куб = {p3}, 4-я степень = {p4}")

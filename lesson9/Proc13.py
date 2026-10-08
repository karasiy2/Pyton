def sort_dec3(a, b, c):
    return tuple(sorted([a, b, c], reverse=True))

nabor1 = (10, 5, 20)
nabor2 = (-3, 0, -1)

print("Набор 1 по убыванию:", sort_dec3(*nabor1))
print("Набор 2 по убыванию:", sort_dec3(*nabor2))

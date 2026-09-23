a = float(input())
b = float(input())

if a != 0 and b != 0:
    print()
else:
    print("Число должно быть не 0!")


a2 = a**2
b2 = b**2

summ = a2 + b2
raz = a2 - b2
proiz = a2 * b2
chast = a2 / b2

print(abs(summ))
print(abs(raz))
print(abs(proiz))
print(abs(chast))
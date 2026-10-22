S = input("Введите строку S: ")
N = int(input("Введите количество звездочек: "))

stars = '*' * N
print(stars.join(S))

A = int(input("Введите число A: "))
B = int(input("Введите число B (больше A): "))

N = B - A + 1

print("Числа между A и B:")
for i in range(A, B + 1):
    print(i, end=" ")

print(f"Количество чисел N = {N}")

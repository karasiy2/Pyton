A = int(input())
B = int(input())

total_sum = 0

for i in range(A, B + 1):
    total_sum += i ** 2 

print(f"Сумма квадратов чисел от {A} до {B} равна: {total_sum}")

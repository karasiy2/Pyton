A = int(input())
B = int(input())

product = 1

for i in range(A, B + 1):
    product *= i

print(f"Произведение чисел от {A} до {B} равно: {product}")

A = [2, 3, 4, 5, 6]

total_sum = sum(A)

even_index_elements = A[0::2] 

total_prod = 1
for x in even_index_elements:
    total_prod *= x

print(f"Сумма всех элементов: {total_sum}")
print(f"Произведение элементов с чётными индексами: {total_prod}")

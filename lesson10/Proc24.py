def even(k):
    return k % 2 == 0

numbers = [1, 2, 3, 4, 10, 15, 22, 33, 44, 55]
even_count = sum(1 for x in numbers if even(x))

print("Количество чётных чисел в наборе:", even_count)

A = [1, 2, 3, 4, 5, 15]

average = sum(A) / len(A)
above_average = [x for x in A if x > average]

print("Среднее значение:", average)
print("Элементы больше среднего:", above_average)

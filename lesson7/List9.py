A = [1, 2, 3, 4, 5]

average = sum(A) / len(A)
greater_avg = [x for x in A if x > average]

print(f"Среднее арифметическое: {average}")
print(f"Элементы больше среднего: {greater_avg}")
print(f"Их количество: {len(greater_avg)}")

matrix = [
    [12, 22, 32, 42]
]
M = len(matrix)
N = len(matrix[0])

print("Элементы нечетных столбцов (1, 3, ...):")
for j in range(0, N, 2): 
    for i in range(M):
        print(matrix[i][j])

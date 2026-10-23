M = 4
N = 3
numbers = [10, 20, 30, 40]

matrix = [[numbers[i]] * N for i in range(M)]

for row in matrix:
    print(row)

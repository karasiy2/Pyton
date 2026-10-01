N = int(input())

while N > 1 and N % 3 == 0:
    N = N // 3

if N == 1:
    print("True")
else:
    print("False")

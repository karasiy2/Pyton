N = int(input())
result = "".join(chr(ord('A') + i) for i in range(N))
print(result)

N = int(input())
result = "".join(chr(ord('z') - i) for i in range(N))
print(result)

S = input("Введите строку: ")
count = sum(1 for char in S if 'A' <= char <= 'Z')
print("Количество прописных латинских букв:", count)

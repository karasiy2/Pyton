try:
    s = input()
    index = int(input())
    print(s[index])
except IndexError:
    print("Нет такого символа")

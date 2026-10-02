try:
    s = input()
    try:
        index = int(input())
    except ValueError:
        print("Ошибка ввода")
        raise SystemExit
    
    print(s[index])
except IndexError:
    print("Нет такого символа")

while True:
    try:
        num = int(input())
        print(num)
        break
    except ValueError:
        print("Это не число. Попробуй ещё:")

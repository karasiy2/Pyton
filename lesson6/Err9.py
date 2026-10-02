try:
    age = int(input())
    if age < 0 or age > 120:
        raise ValueError("Возраст вне допустимого диапазона")
    print(f"Принято")
except ValueError as e:
    print(f"Отклонено")

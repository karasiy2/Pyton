def invert_digits(k):
    return int(str(k)[::-1])

data = [123, 4502, 9, 87654, 100]
for num in data:
    inverted = invert_digits(num)
    print(f"Исходное: {num} -> Перевернутое: {inverted}")

def digit_count(k):
    if k <= 0: return 0
    return len(str(k))

numbers = [7, 45, 123, 9999, 123456]
for num in numbers:
    print(f"В числе {num} цифр:", digit_count(num))

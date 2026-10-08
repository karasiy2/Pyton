strings = ["яблоко", "банан", "арбуз", "груша", "ананас"]
letter = "а"

filtered = [s for s in strings if s.lower().startswith(letter.lower())]

print(f"Строки на букву '{letter}':", filtered)

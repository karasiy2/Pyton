strings = ["яблоко", "киви", "арбуз", "банан", "груша"]

sorted_strings = sorted(strings, key=len)
print("Строки по возрастанию длины:", sorted_strings)

longest_string = max(strings, key=len)
print("Самая длинная строка:", longest_string)

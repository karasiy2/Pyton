S = input("Введите строку: ")

count = 0
for char in S:
    is_latin_lower = 'a' <= char <= 'z'
    is_cyrillic_lower = ('а' <= char <= 'я') or (char == 'ё')
    
    if is_latin_lower or is_cyrillic_lower:
        count += 1

print("Общее количество строчных букв:", count)

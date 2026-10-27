import os

def count_existing_files(file1: str, file2: str, file3: str, file4: str) -> int:
    filenames = [file1, file2, file3, file4]
    count = 0
    
    for name in filenames:
        if os.path.exists(name) and os.path.isfile(name):
            count += 1
            
    return count

f1 = input("Введите имя 1-го файла: ")
f2 = input("Введите имя 2-го файла: ")
f3 = input("Введите имя 3-го файла: ")
f4 = input("Введите имя 4-го файла: ")

existing_count = count_existing_files(f1, f2, f3, f4)
print(f"Количество существующих файлов: {existing_count}")

import os

def process_unknown_order(path1: str, path2: str):
    if os.path.exists(path1) and os.path.isfile(path1) and os.path.getsize(path1) > 0:
        existing_file = path1
        missing_file = path2
    elif os.path.exists(path2) and os.path.isfile(path2) and os.path.getsize(path2) > 0:
        existing_file = path2
        missing_file = path1
    else:
        print("Ошибка: Условия задачи не выполнены (должен быть один непустой файл и один отсутствующий).")
        return

    try:
        with open(existing_file, 'r', encoding='utf-8') as f:
            elements = f.read().split()
            
        if not elements:
            print(f"Файл {existing_file} оказался пуст после считывания.")
            return
            
        first_elem = elements[0]
        last_elem = elements[-1]
        
        with open(missing_file, 'w', encoding='utf-8') as f:
            f.write(f"{last_elem} {first_elem}\n")
            
        print(f"Успешно! Извлечено из '{existing_file}' и записано в новый файл '{missing_file}'.")
        
    except OSError as e:
        print(f"Ошибка при работе с файловой системой: {e}")

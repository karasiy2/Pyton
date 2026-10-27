def copy_edges(file_in: str, file_out: str):
    try:
        with open(file_in, 'r', encoding='utf-8') as f:
            elements = f.read().split()
        
        if not elements:
            print("Первый файл пуст!")
            return
        
        first_elem = elements[0]
        last_elem = elements[-1]

        with open(file_out, 'w', encoding='utf-8') as f:
            f.write(f"{first_elem} {last_elem}\n")
            
        print(f"Файл {file_out} успешно создан.")
        
    except OSError as e:
        print(f"Произошла ошибка при работе с файлами: {e}")


def write_progression(filename: str, A: float, D: float):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for i in range(10):
                term = A + i * D
                f.write(f"{term}\n")
        print("Файл успешно записан.")
    except OSError as e:
        print(f"Ошибка при работе с файлом: {e}")

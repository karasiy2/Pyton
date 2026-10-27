import os

def check_and_create_file(S: str) -> bool:
    try:
        with open(S, 'w', encoding='utf-8') as f:
            pass
        return True
    except (OSError, ValueError):
        return False

S = input("Введите имя файла: ")
result = check_and_create_file(S)
print(result)

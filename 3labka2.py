def single_permutation(text, key):
    # Длина ключа определяет количество столбцов в матрице
    num_cols = len(key)
    num_rows = -(-len(text) // num_cols)  # округление вверх
    
    # Дополнение текста пробелами, чтобы он заполнил всю матрицу
    padded_text = text.ljust(num_cols * num_rows)
    
    # Создание таблицы для перестановки
    table = [padded_text[i * num_cols:(i + 1) * num_cols] for i in range(num_rows)]
    
    # Сортировка столбцов на основе ключа
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    
    # Применение перестановки по столбцам
    encrypted_text = ''.join([''.join(row[i] for row in table) for i in sorted_key_indices])
    
    return encrypted_text

def double_permutation(text, key1, key2):
    # Первая перестановка с ключом key1
    first_permutation = single_permutation(text, key1)
    
    # Вторая перестановка с ключом key2
    second_permutation = single_permutation(first_permutation, key2)
    
    return second_permutation

# Ввод текста и ключей от пользователя
text = input("Введите текст для шифрования: ")
key1 = input("Введите первый ключ (числа без пробелов, например, 31452): ")
key2 = input("Введите второй ключ (числа без пробелов, например, 54321): ")

# Шифрование текста
encrypted_text = double_permutation(text, key1, key2)
print("Зашифрованный текст:", encrypted_text)

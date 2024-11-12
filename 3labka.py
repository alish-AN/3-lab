def vigenere_cipher(text, key, mode='encrypt'):
    result = []
    key = key.lower()
    key_length = len(key)
    key_indices = [ord(i) - ord('a') for i in key]
    
    for i, char in enumerate(text):
        if char.isalpha():  
            offset = ord('a') if char.islower() else ord('A')
            key_shift = key_indices[i % key_length]
            
            
            if mode == 'encrypt':
                new_char = chr((ord(char) - offset + key_shift) % 26 + offset)
            elif mode == 'decrypt':
                new_char = chr((ord(char) - offset - key_shift) % 26 + offset)
                
            result.append(new_char)
        else:
            result.append(char)  

    return ''.join(result)

def read_input_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    if len(lines) < 2:
        raise ValueError("Файл должен содержать текст на первой строке и ключ на второй строке")
    return lines[0].strip(), lines[1].strip()

def write_output_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    
    try:
       
        text, key = read_input_file(input_filename)
        
       
        mode = input("Введите режим ('encrypt' для шифрования или 'decrypt' для дешифрования): ").strip().lower()
        
        if mode not in ['encrypt', 'decrypt']:
            print("Ошибка: Некорректный режим. Используйте 'encrypt' или 'decrypt'.")
            return
        
       
        result_text = vigenere_cipher(text, key, mode=mode)
        
        
        write_output_file(output_filename, result_text)
        
        print(f"Текст успешно {('зашифрован' if mode == 'encrypt' else 'дешифрован')} и сохранен в '{output_filename}'")
        
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()

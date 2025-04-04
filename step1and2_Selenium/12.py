def caesar_cipher(text, key, alphabet):
    """Шифрует или расшифровывает текст с помощью шифра Цезаря с учётом регистра, сдвига и выбранного алфавита"""
    encrypted = ''
    for i in text:
        if i.isalpha() and i in alphabet.lower():  # Для строчных букв
            encrypted += alphabet.lower()[(alphabet.lower().find(i) + key) % len(alphabet.lower())]
        elif i.isalpha() and i in alphabet.upper():  # Для прописных букв
            encrypted += alphabet.upper()[(alphabet.upper().find(i) + key) % len(alphabet.upper())]
        else:
            encrypted += i  # Если символ не буква, не изменяем
    return encrypted

# Пример использования:

# Задание алфавита
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Ввод текста и сдвига
text = input("Введите текст для шифрования/расшифрования: ")
shift = int(input("Введите сдвиг: "))

# Выбор алфавита
language_choice = input("Выберите язык (русский/английский): ").lower()

# Выбор соответствующего алфавита
if language_choice == "русский":
    alphabet = russian_alphabet
elif language_choice == "английский":
    alphabet = english_alphabet
else:
    print("Неизвестный выбор языка.")
    exit()

# Шифруем или расшифровываем текст в зависимости от сдвига
encrypted_text = caesar_cipher(text, shift, alphabet)

print("Результат: ", encrypted_text)


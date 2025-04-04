import random


def is_valid(s, n):
    """Проверяет, является ли введенное значение числом в пределах от 1 до n."""
    return s.isdigit() and 1 <= int(s) <= n


def get_number(n):
    """Запрашивает у пользователя число, пока не будет введено корректное значение."""
    while True:
        s = input()
        if is_valid(s, n):
            return int(s)
        else:
            print(f'А может быть все-таки введем целое число от 1 до {n}?')


def play_game():
    """Основная логика игры"""
    print('Добро пожаловать в числовую угадайку!')

    while True:
        # Запрашиваем правую границу
        print('Введите правую границу диапазона:')
        upper_limit = get_number(1000)  # Ограничим разумным числом

        num = random.randint(1, upper_limit)  # Генерируем число
        attempts = 0  # Счетчик попыток

        print(f'Компьютер загадал число от 1 до {upper_limit}. Попробуйте угадать!')

        while True:
            guess = get_number(upper_limit)
            attempts += 1

            if guess < num:
                print('Ваше число меньше загаданного, попробуйте еще разок.')
            elif guess > num:
                print('Ваше число больше загаданного, попробуйте еще разок.')
            else:
                print(f'Вы угадали! Поздравляем! 🎉 Количество попыток: {attempts}')
                break

        # Предложение сыграть снова
        print('Хотите сыграть еще раз? (да/нет)')
        if input().strip().lower() != 'да':
            print('Спасибо за игру! До новых встреч!')
            break


# Запускаем игру
play_game()

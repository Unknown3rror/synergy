import random


def play_game():
    print("=== ИГРА 'УГАДАЙ ЧИСЛО' ===")
    print("Я загадал число от 1 до 100. У тебя 10 попыток.\n")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Попытка {attempts + 1}/{max_attempts}. Введите ваше число: "))

            if not 1 <= guess <= 100:
                print("Число должно быть от 1 до 100!")
                continue

            attempts += 1

            if guess < secret_number:
                print("Слишком маленькое число!")
            elif guess > secret_number:
                print("Слишком большое число!")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
                return True

        except ValueError:
            print("Ошибка: введите целое число!")
            continue

    print(f"Игра окончена. Вы не угадали. Загаданное число было: {secret_number}")
    return False


def main():
    while True:
        play_game()
        again = input("\nХотите сыграть ещё раз? (да/нет): ").strip().lower()
        if again not in ['да', 'yes', 'y']:
            print("Спасибо за игру! До свидания!")
            break


if __name__ == "__main__":
    main()
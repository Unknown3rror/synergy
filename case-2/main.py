import math


def parse_positive_integer(raw_value: str) -> int:
    value = int(raw_value)

    if value < 0:
        raise ValueError

    return value


def read_positive_integer() -> int:
    while True:
        try:
            return parse_positive_integer(input("Введите положительное целое число: "))
        except ValueError:
            print("Ошибка: нужно ввести положительное целое число.")


def calculate_factorial(number: int) -> int:
    return math.factorial(number)


def main() -> None:
    number = read_positive_integer()
    factorial_value = calculate_factorial(number)
    print(f"Факториал числа {number}: {factorial_value}")


if __name__ == "__main__":
    main()
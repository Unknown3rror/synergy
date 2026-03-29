import math


def parse_positive_integer(raw_value: str) -> int:
    value = int(raw_value)
    if value < 0:
        raise ValueError("Число должно быть положительным!")
    return value


def read_positive_integer() -> int:
    while True:
        try:
            user_input = input("Введите положительное целое число для вычисления факториала: ").strip()
            return parse_positive_integer(user_input)
        except ValueError as e:
            if "Число должно быть положительным" in str(e):
                print("Ошибка: введено отрицательное число. Факториал определён только для положительных чисел.")
            else:
                print("Ошибка: введено нечисловое значение! Пожалуйста, введите целое положительное число.")


def calculate_factorial(number: int) -> int:
    return math.factorial(number)


def main() -> None:
    print("=== Программа вычисления факториала ===\n")
    number = read_positive_integer()
    factorial_value = calculate_factorial(number)
    print(f"\nФакториал числа {number} равен: {factorial_value}")


if __name__ == "__main__":
    main()
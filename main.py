from half_division_method import half_division_method
from golden_section_method import golden_section
from Fibonacci_method import Fibonacci_method
from contextlib import redirect_stdout


def my_function(x):
    return (x ** 3) - 3 * (x ** 2) - 24 * x + 10


def main():
    with open('output.txt', 'w', encoding='utf-8') as f, redirect_stdout(f):
        print('Метод половинного деления')
        half_division_method(my_function, 3, 5, 0.2)
        print('\n\nМетод «золотого» сечения')
        golden_section(my_function, 3, 5, 0.2)
        print('\n\nМетод чисел Фибоначчи')
        Fibonacci_method(my_function, 3, 5, 0.2)


if __name__ == '__main__':
    main()

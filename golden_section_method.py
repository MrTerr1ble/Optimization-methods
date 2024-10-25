from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


def golden_section(function, a, b, e):
    # Настройка графика
    x_vals = np.linspace(a - 1, b + 1, 500)
    y_vals = function(x_vals)
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)

    # Шаг 1
    print(
        f'Начальный интервал неопределенности L0[{a};{b}]'
        '\nТребуемая точность e = {e}')

    # Шаг 2
    k = 0

    PHI = (3 - sqrt(5)) / 2  # Вынес как константу

    while abs(a - b) > e:

        # Шаг 3
        y = a + PHI * (b - a)
        z = a + b - y
        print(
            f'\nИтерация {k + 1}:'
            f'\nЗначение y0 = {y}; Значение z0 = {z}'
        )

        # Шаг 4
        f_y = function(y)
        f_z = function(z)
        print(
            f'Значение f(y): {f_y}; Значение f(z): {f_z}'
        )

        # Отображение текущего интервала на графике
        plt.plot([a, b], [function(a), function(b)], 'ro-')

        # Шаг 5(a)
        if f_y <= f_z:
            b = z
            z = y
            y = a + b - y
            f_y = function(y)

        # Шаг 5(б)
        elif f_y > f_z:
            a = y
            y = z
            z = a + b - z

        # Шаг 6(б)
        k += 1

    X = (a + b) / 2
    print(
        f'\nПриближенный корень x* = {X},'
        f'F(x*) = {function(X)}, количество итераций = {k}'
    )
    plt.scatter(X, function(X), color='green', label='Приближенный корень')
    plt.legend()
    plt.show()
    return X


def my_function(x):
    return (x ** 3) - 3 * (x ** 2) - 24 * x + 10


def main():
    golden_section(my_function, 3, 5, 0.2)


if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt
import numpy as np


# Шаг 2
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def Fibonacci_method(function, a, b, e):
    # Настройка графика
    x_vals = np.linspace(a - 1, b + 1, 500)
    y_vals = function(x_vals)
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)

    # Шаг 1
    print(
        f'Начальный интервал неопределенности L0[{a};{b}]'
        '\nТребуемая точность e = {e}')

    # Шаг 3
    k = 0

    while fibonacci(k) < (b - a) / e:

        # Шаг 7(а)
        k += 1

    for i in range(1, k):

        # Шаг 4
        y = a + (fibonacci(k - 2) / fibonacci(k)) * (b - a)
        z = a + (fibonacci(k - 1) / fibonacci(k)) * (b - a)
        print(
            f'\nЗначение y0 = {y}; Значение z0 = {z}'
        )

        # Шаг 5
        f_y = function(y)
        f_z = function(z)
        print(
            f'Значение f(y): {f_y}; Значение f(z): {f_z}'
        )

        # Отображение текущего интервала на графике
        plt.plot([a, b], [function(a), function(b)], 'r.-', alpha=0.6)

        # Шаг 6(а)
        if f_y <= f_z:
            b = z
            z = y
            y = a + (fibonacci(k - i - 2) / fibonacci(k - i)) * (b - a)

        # Шаг 6(б)
        elif f_y > f_z:
            a = y
            y = z
            z = a + (fibonacci(k - i - 1) / fibonacci(k - i)) * (b - a)

    # Шаг 7(б)
    X = (a + b) / 2

    print(
        f'\nПриближенный корень x* = {X},'
        f'F(x*) = {function(X)}, количество итераций = {k}'
    )
    plt.plot(X, function(X), 'go', label='Приближенный корень', markersize=5)
    plt.legend()
    plt.show()

import matplotlib.pyplot as plt
import numpy as np


def half_division_method(function, a, b, e):
    # Настройка графика
    x = np.linspace(2, 6, 1000)
    y = function(x)
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)

    # Шаг 1
    print(
        f'Начальный интервал неопределенности L0[{a};{b}]'
        '\nТребуемая точность e = {e}')

    # Шаг 2
    k = 0
    while (b - a) / 2 > e:
        # Шаг 3
        Xkc = (a + b) / 2
        L = abs(b - a)
        F_xkc = function(Xkc)
        print(
            f'\nИтерация {k + 1}:'
            f'\nСредняя точка Xkc = {Xkc}'
            f'\nДлина интервала L = {L}'
            f'\nЗначение функции в средней точке F(Xkc) = {F_xkc}'
        )

        # Шаг 4
        y_k = a + L / 4
        z_k = b - L / 4
        F_y = function(y_k)
        F_z = function(z_k)
        print(f'Точки y_k = {y_k}, z_k = {z_k}\nЗначения функций: F(y_k) = {F_y}, F(z_k) = {F_z}')

        # Шаг 5(а)
        if F_y < F_xkc:
            b = Xkc
            print(f'Выбрано новое значение b = Xkc = {Xkc}')

        # Шаг 5(б)
        elif F_y > F_xkc:

            # Шаг 6(а)
            if F_z < F_xkc:
                a = Xkc
                print(f'Выбрано новое значение a = Xkc = {Xkc}')

            # Шаг 6(б)
            else:
                a = y_k
                b = z_k
                print(f'Новый интервал: [{a}, {b}]')

        # Отображение текущего интервала на графике
        plt.plot([a, b], [function(a), function(b)], 'ro-')

        # Шаг 7(б)
        k += 1

    # Шаг 7(a)
    X = (a + b) / 2
    print(
        f'\nПриближенный корень x* = {X},'
        f'F(x*) = {function(X)}, количество итераций = {k}'
    )
    plt.scatter(X, function(X), color='green', label='Приближенный корень')
    plt.legend()
    plt.show()
    return X

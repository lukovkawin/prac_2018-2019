from scipy.optimize import linprog
from fractions import Fraction
import matplotlib.pyplot as plt
import pylab


def multiply_matrix(matrix, num):
    for i in range(len(matrix)):
        if type(matrix[0]) == list:
            for j in range(len(matrix[0])):
                matrix[i][j] *= num
        else:
            matrix[i] *= num
    return matrix


def transpose_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix.append([])
        for j in range(len(matrix)):
            new_matrix[i].append(matrix[j][i])
    return new_matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        if type(matrix[0]) == list:
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=' | ')
            print()
        else:
            print(matrix[i], end=' | ')
    print()


def graph_str(strategy, player):
    x = []
    for ind in range(len(strategy)):
        x.append(ind + 1)
    pylab.xlim([0, len(strategy) + 1])
    pylab.ylim([0, max(strategy) * 1.25])
    plt.stem(x, strategy, '--')
    if player == 1:
        plt.title('Оптимальная стратегия первого игрока')
    else:
        plt.title('Оптимальная стратегия второго игрока')
    plt.show()


def print_solution(cost, str1, str2):
    if cost:
        print('Значение игры = ', cost)
        print('Опт. стратегия первого игрока: ')
        print_matrix(str1)
        print('Опт. стратегия второго игрока: ')
        print_matrix(str2)
        graph_str(str1, 1)
        graph_str(str2, 2)
    else:
        return


def read_matrix(file):
    mas = []
    f = open(file, 'r')
    for line in f:
        mas.append([int(x) for x in line.split()])
    f.close()
    return mas


def fraction_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        if type(matrix[0]) == list:
            new_matrix.append([])
            for j in range(len(matrix[0])):
                new_matrix[i].append(Fraction(matrix[i][j]).limit_denominator())
        else:
            new_matrix.append(Fraction(matrix[i]).limit_denominator())
    return new_matrix


def nash_equilibrium(matrix):
    m = len(matrix)
    n = len(matrix[0])
    # print('Рамзер матрицы: %d x %d' % (m, n))
    # print('Матрица:')
    # print_matrix(matrix)

    c = m * [1]
    b = n * [-1]
    a = multiply_matrix(transpose_matrix(matrix), -1)
    first_res = linprog(c, a, b)

    c = n * [-1]
    b = m * [1]
    a = matrix
    second_res = linprog(c, a, b)

    if first_res.success and second_res.success:
        first_str = list(first_res.x)
        second_str = list(second_res.x)
    else:
        print('Нет решения')
        return None

    v1 = Fraction(1 / sum(first_str)).limit_denominator()
    v2 = Fraction(1 / sum(second_str)).limit_denominator()
    if v1 == v2:
        v_res = v1
    else:
        print('Значения игры разные')
        return None

    first_str = fraction_matrix(multiply_matrix(first_str, v_res))
    second_str = fraction_matrix(multiply_matrix(second_str, v_res))

    return v_res, first_str, second_str


# print('Какой пример решить?')
# ex = str(input())
# game_matrix = read_matrix('input' + ex)
# v, first_opt_str, second_opt_str = nash_equilibrium(game_matrix)
# print_solution(v, first_opt_str, second_opt_str)

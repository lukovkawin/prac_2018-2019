import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot
def nash_equilibrium(A):
    tmp = np.amin(A)
    if tmp <= 0:
        A = A - tmp + 1
    rows = A.shape[0]
    clm = A.shape[1]
    
    # приводим задачу из вида (c, x)->max к виду (-c, x)=(c, -x)->min т.к. linprog минимизирует целевую функцию
    c = -np.ones(clm)
    
    # неравенство ограничений делим на цену игры => задаём вектор ограничений, состоящим из единиц
    # при этом вероятности выбора каждой стратегии делятся на цену игры
    # A*x<b
    b = np.ones(rows)

    player2 = linprog(c, A_ub = A, b_ub = b)
    game_price = -1 / player2.fun #не забываем домножить на (-1) т.к. нашли стратегию (-x)
    strategy2 = player2.x * game_price
    
    #приводим ограничения из вида xA>1 к виду -(А)^T * x < -1 
    A = -np.transpose(A)
    b = -np.ones(clm)
    c = np.ones(rows)
    player1 = linprog(c, A_ub = A, b_ub = b)
    strategy1 = player1.x * game_price
    
    game_price = game_price + tmp - 1
    
    print("Цена игры: ", game_price)
    print("Стратегия первого игрока: ", strategy1)
    print("Стратегия второго игрока: ", strategy2)
    
    return game_price, strategy1, strategy2

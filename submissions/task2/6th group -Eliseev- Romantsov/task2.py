from scipy.optimize import linprog
import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt
def plot(p,q):
    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    ax1.stem(range(1, len(p) + 1), p)
    ax2.stem(range(1, len(q) + 1), q)

def frac(cost1, p1, q1):
    p = []
    q = []
    for i in p1:
        p.append(Fraction(*i.as_integer_ratio()).limit_denominator())
    for i in q1:
        q.append(Fraction(*i.as_integer_ratio()).limit_denominator())
    cost = Fraction(*cost1.as_integer_ratio()).limit_denominator()
    return (cost, p, q)


def nash_equilibrium(A):
    str, col = A.shape
    minimum = A.min()
    check = 0
    if (minimum <= 0):
        A = A - minimum + 1
        check = 1
    c = np.array([-1] * col)
    b = np.array([1] * str)
    res = linprog(c, A, b)
    str2 = res.x
    game = 1 / str2.sum()
    str2 = str2 * game

    B = -A.transpose()
    c = np.array([1] * str)
    b = np.array([-1] * col)
    res = linprog(c, B, b)
    str1 = res.x * game
    if (check):
        game = game + minimum - 1
    return (game, str1, str2)

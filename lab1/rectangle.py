from sympy import *
import random
import matplotlib.pyplot as plt
import const_integral

S_points = []
delta_points = []

def f(x):
    return (x* const_integral.A/32767 + x/2)


def rectangle_method(num_rectangles, left_limit=1, right_limit=3, S=0):

    h = (right_limit-left_limit)/num_rectangles

    for i in range(num_rectangles):
        x = left_limit+i*h
        S = S + f(x)

    S = S*h
    S_points.append(S)
    delta_i = abs(S - const_integral.const_integrated)
    delta_points.append(delta_i)
    print("Площа з кількістю прямокутниів", num_rectangles, ":", round(S, 7))
    print("Похибка", round(delta_i, 7))

    return S


def draw_plot():
    plt.plot([1, 100, 1000, 5000, 10000, 50000, 100000], delta_points, "ro")
    plt.ylabel("Похибка")
    plt.xlabel("Кількість прямокутників")
    plt.show()

import random
import const_integral
import matplotlib.pyplot as plt

delta_points = []


def rnd(a, b):
    return a+(b-a)*random.randint(0, 32767)/32767


def f(x):
    return (x*const_integral.A/32767 + x/2)


def monteCarlo_method(num_rectangles, left_limit=1, right_limit=3, S=0):

    for i in range(num_rectangles):
        x = rnd(left_limit, right_limit)
        S = S + f(x)

    S = S*(right_limit - left_limit)/num_rectangles
    delta_i = abs(S - const_integral.const_integrated)
    delta_points.append(delta_i)
    print("Похибка", round(delta_i, 7))
    print("Площа", S)
    return S


def draw_plot():
    print(delta_points)
    plt.plot([1, 100, 1000, 5000, 10000, 50000, 100000], delta_points, "bo")
    plt.ylabel("Area")
    plt.xlabel("Number of points")
    plt.show()

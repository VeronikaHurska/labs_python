from sympy import *
import matplotlib.pyplot as plt
import monteCarlo
import rectangle


def main():

    monteCarlo.monteCarlo_method(1)
    monteCarlo.monteCarlo_method(100)
    monteCarlo.monteCarlo_method(1000)
    monteCarlo.monteCarlo_method(5000)
    monteCarlo.monteCarlo_method(10000)
    monteCarlo.monteCarlo_method(50000)
    monteCarlo.monteCarlo_method(100000)
    monteCarlo.draw_plot()
    print("-----------------------------------------------------------")

    rectangle.rectangle_method(1)
    rectangle.rectangle_method(100)
    rectangle.rectangle_method(1000)
    rectangle.rectangle_method(5000)
    rectangle.rectangle_method(10000)
    rectangle.rectangle_method(50000)
    rectangle.rectangle_method(100000)
    rectangle.draw_plot()


if __name__ == "__main__":
    main()

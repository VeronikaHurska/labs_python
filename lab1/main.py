from sympy import *
import matplotlib.pyplot as plt
import monteCarlo
import rectangle 


def main():
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

import random
from sympy import *

A = random.randint(0, 32767)
print("Рандомне число: ", A)

x = symbols('x')
const_integrated = float(integrate(x*A/32768 + x/2, (x, 1, 3)))
print("Еталонний результат:", round(const_integrated, 5))

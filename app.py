import numpy as np
import matplotlib.pyplot as plt

# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

a, b, c, e, k = -12, -18, 5, 10, -30
x = np.arange(-100, 100, 0.001)
x_cut = np.arange(-58, -54, 0.001)
def func(x):
    function = a*np.sin(np.cos(x))*x**4 + b*x**3 + c*x**2 + e*x + k
    return function

root = -58
for i in np.arange(-58, -54, 0.001):
    if np.absolute(func(root))>np.absolute(func(i)):
        root = i

min_func = min(func(x_cut))
def extr_func(x, min_func):
    extremum_function = a*np.sin(np.cos(x))*x**4 + b*x**3 + c*x**2 + e*x + k - min_func
    return  extremum_function

extr_x_cut = -58
for i in np.arange(-58, -54, 0.001):
    if np.absolute(extr_func(extr_x_cut, min_func))>np.absolute(extr_func(i, min_func)):
        extr_x_cut = i

x_range_down = np.arange(-58, extr_x_cut, 0.001)
x_range_up = np.arange(extr_x_cut, -54, 0.001)
plt.title(f'Корень функции на участке (-58; -54): {round(root, 2)}')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid()
plt.plot(x, func(x), 'g')
plt.plot(x_range_down, func(x_range_down), 'r', label="Убывание")
plt.plot(x_range_up, func(x_range_up), 'b', label="Возрастание")
plt.text(extr_x_cut, func(extr_x_cut) + 30, f'Вершина функции x = {round(extr_x_cut, 2)}')
plt.legend()
plt.show()

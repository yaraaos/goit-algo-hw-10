import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Аналітичне обчислення інтеграла
result, error = spi.quad(f, a, b)
print("Аналітичний інтеграл:", result)

# Метод Монте-Карло для обчислення інтеграла
N = 100000  # кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = f(x_random)
integral_mc = (b - a) * np.mean(y_random)
print("Інтеграл методом Монте-Карло:", integral_mc)

#Графік
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

# Обл. під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Графік
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def x2(x):
    return 3*(x-5)**2+6

x = np.linspace(-10,10, 100)

plt.plot(x, x2(x), label=r'$x^2$')
plt.legend()
plt.xlabel(r'$\frac{1}{T}\,/\,\unit{\per\kelvin}$')
plt.ylabel(r'$p\,/\,\unit{\pascal}$')
plt.savefig('build/plot.pdf')
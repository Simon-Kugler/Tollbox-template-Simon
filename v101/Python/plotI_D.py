#denk an die 5 fache schwingungsdauer
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

a, T = np.genfromtxt("../Messwerte/Traegheitsmoment.txt", unpack=True)
T = T / 5
x = np.linspace(0, 0.1, 1000)

T2 = T**2
a2 = a**2

plt.plot(a2, T2, "x", label="Messwerte")

def fit(x, A, B):
    return A * x + B

params, covariance_matrix = curve_fit(fit, a2, T2)
errors = np.sqrt(np.diag(covariance_matrix))

plt.plot(x, fit(x, *params), label="Lineare Regression")
plt.grid()
plt.legend(loc='best')
plt.xlabel(r'$a^2 \,/\, \mathrm{m}^2$')
plt.ylabel(r'$T^2 \,/\, \mathrm{s}^2$')

for name, value, error in zip('AB', params, errors):
        print(f'{name} = {value:.6f} ± {error:.6f}')

plt.show()
plt.savefig("plotI_D.pdf")
print("T = ",  T)
print("T^2 = ", T2)
print("a^2 = ", a2)
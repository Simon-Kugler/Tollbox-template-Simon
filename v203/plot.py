import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x, y = np.genfromtxt("Messdaten1_203.txt", unpack=True)
y2, x2 = np.genfromtxt("Messdaten2_203.txt", unpack=True)
y *= 100

plt.plot(x, y, "bx", label="Messwerte1")
plt.yscale("log")
plt.xlabel("$T$ [K]")
plt.ylabel("$p$ [mbar]")

R = 8.314472
p = 3000

def fit(x, L):
   return p * np.exp(- L / (x * R))


params, covariance = curve_fit(fit, x, y)
errors = np.sqrt(np.diag(covariance))
print(params)


for name, value, error in zip('L', params, errors):
    print(f'{name} = {value:.6f} ± {error:.6f}')

x_t = np.linspace(293.15, 373.15, 1000)
plt.plot(x_t, fit(x_t, *params), label="Ausgleichsgerade")


plt.legend()
plt.grid()

plt.show()
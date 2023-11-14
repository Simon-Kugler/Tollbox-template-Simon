import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x, y = np.genfromtxt("Messdaten1_203.txt" , unpack=True)
y2, x2 =np.genfromtxt("Messdaten2_203.txt",unpack=True)

plt.plot(x, y, "bx", label="Messwerte1")
plt.yscale("log")
plt.xlabel("$T$ [K]")
plt.ylabel("$p$ [mbar]")
plt.legend()
plt.grid()


R = 8.314472
p = 996
def fit (x, L):
    return p * np.exp(- (1/x) * L/R)

params, covariance = curve_fit(fit, x, y)
errors = np.sqrt(np.diag(covariance))
print(errors)

for name, value, error in zip('LR', params, errors):
        print(f'{name} = {value:.6f} ± {error:.6f}')

x_t = np.linspace(293.15, 373.15, 1000)
plt.plot(x_t, fit(x_t, *params), label="Ausgleichsgerade")

plt.show()

plt.savefig("build/plot.pdf")
plt.clf()

plt.plot(x2, y2, "bx", label="Messwerte2")
plt.yscale("log")
plt.xlabel("$T$ [K]")
plt.ylabel("$p$ [bar]")
plt.legend()
plt.grid()

plt.show()
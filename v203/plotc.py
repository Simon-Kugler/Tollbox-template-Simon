import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy.constants as const
from uncertainties import ufloat

T, p = np.genfromtxt("Messdaten1_203.txt", unpack=True)
T1, p1 = np.genfromtxt("Messdaten1.1_203.txt", unpack=True)
x = np.linspace(280, 380, 1000)

p *= 100 # um von mbar auf Pa zu kommen
p1 *= 100
#Aufgabe Log des Drucks gegen 1/T
T = 1/T
p = np.log(p)
T1 = 1/T1
p1 = np.log(p1)
x = 1/x

#plt.plot(T, p, "bx", label="Messwerte1")
fig, ax = plt.subplots(1,layout="constrained")
ax.plot(T, p, "rx", label="Messwerte")

#der Fit
def fit(T, L, b):
   return L * T + b

params, cov = curve_fit(fit, T, p)
errors = errors = np.sqrt(np.diag(cov))

print(params)
print(errors)
L = - params[0]
print("L = ", L, "±", errors[0])

ax.plot(x, fit(x, *params), "b-", label="Ausgleichsgerade")

ax.set_xlabel(r"$1/T$ ")
ax.set_ylabel(r"$\ln\left(\frac{p}{p_0}\right)$")
ax.grid()
ax.legend()
fig.savefig("plotc.pdf")
fig.show()
L1=ufloat(L,errors[0])*const.R
print("L1=",L1,)
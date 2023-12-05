import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy.constants as const
from uncertainties import ufloat

T, p = np.genfromtxt("Messdaten1_203.txt", unpack=True)
T1, p1 = np.genfromtxt("Messdaten1.1_203.txt", unpack=True)
x = np.linspace(280, 380, 1000)

# p *= 1000 # um von mbar auf Pa zu kommen
# p1 *= 100
#Aufgabe Log des Drucks gegen 1/T
T = 1/T
p = np.log(p/1000)
T1 = 1/T1
p1 = np.log(p1/1000)
x = 1/x

#plt.plot(T, p, "bx", label="Messwerte1")
fig, ax = plt.subplots(1,layout="constrained")
ax.plot(T1, p1, "rx", label="Messwerte")

#der Fit
def fit(T1, L, b):
   return L * T1 + b

params, cov = curve_fit(fit, T1, p1)
errors = errors = np.sqrt(np.diag(cov))

print(params)
print(errors)
L = - params[0]
print("L = ", L, "±", errors[0])
print("b = ", params[1], "±", errors[1])

ax.plot(x, fit(x, *params), "b-", label="Ausgleichsgerade")

ax.set_xlabel(r"$1/T$ ")
ax.set_ylabel(r"$\ln\left(\frac{p}{p_0}\right)$")
ax.grid()
ax.legend()
fig.savefig("plotc.pdf")

L1=ufloat(L,errors[0])*const.R
print("L1=",L1,)
# print("b=",b=ufloat(b, params[0]))
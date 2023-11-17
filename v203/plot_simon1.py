import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
import numpy as np

x = np.linspace(250,380,100000)
T, p = np.genfromtxt("Messdaten1_203.txt", unpack=True)

fig, ax = plt.subplots(1,layout="constrained")
# ax.cla()
ax.plot(T[2:], p[2:], "r.", label="data")
# ax.plot(x, 101300*np.exp(-(1/x)*(1522/8.1344)))
#Passende exp-Funktion finden
# def func(p,L,R):
#     return p*(np.exp(-(1/T)*(L/R)))
# params, covariance_matrix = curve_fit(func, T, p)
# uncertainties = np.sqrt(np.diag(covariance_matrix))

# for name, value, uncertainty in zip("LR"):
#     print(f"{name} = {value:8.3f} ± {uncertainty:.3f}")

ax.set_xlabel("T / K")
ax.set_ylabel("p / Pa")
ax.set_xlim(270,400)

# ax.set_ylim(0,100000)
ax.set_yscale("log")
ax.grid()
ax.legend()
# print(f"Y=1013.25*e^(-(1/T)*(1522/8.13448))+{40}")
fig.savefig("plot_simon1.pdf")
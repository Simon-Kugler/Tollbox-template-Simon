import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

T, p = np.genfromtxt("../Messdaten1_203.txt", unpack=True)

p *= 100 # um von mbar auf Pa zu kommen
#Aufgabe Log des Drucks gegen 1/T
T = 1/T
p = np.log(p)

plt.plot(T, p/1000, "r.", label="Messwerte")

plt.xlabel(r"$\frac{1}{T}\,/\,\frac{1}{K}$ ")
plt.ylabel(r"$ln\left(\frac{p}{p_0}\right)$")
plt.grid()
plt.legend()

plt.savefig("plota.pdf")
plt.show()
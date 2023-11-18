import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

T, p = np.genfromtxt("../Messdaten2_203.txt", unpack=True)

p *= 100 # um von mbar auf Pa zu kommen
#Aufgabe Log des Drucks gegen 1/T
T = 1/T
p = np.log(p)

plt.plot(T, p, "bx", label="Messwerte1")

plt.xlabel("$1/T$ ")
plt.ylabel("$ln(p)$")
plt.grid()
plt.legend()

plt.savefig("plotb.pdf")
plt.show()
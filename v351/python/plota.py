import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

f, L = np.genfromtxt("Messdaten_Bilder/Messdaten1.1.txt",unpack=True)
x_f=np.linspace(0.005,400,1000)
def power_law(x_f, a, b):
    return a*x_f**b
#curve_fit
params, covariance_matrix = curve_fit(power_law, f, L)

#Fehlerrechnung
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.3f} ± {error:.3f}")

# Extrahieren der gefitteten Parameter
a_fit, b = params

# Generieren der Werte für die gefittete Funktion
y_fit = power_law(x_f, a_fit, b)

fig, ax = plt.subplots(1,layout="constrained")

ax.plot(f, L, "rx", markersize=10, label="Messdaten")
plt.plot(x_f, y_fit, "b", label="Fit")
plt.ylim(0,100)

ax.set_xlabel(r"$\nu$ / kHz")
ax.set_ylabel("U / V")

ax.grid()
ax.legend()

fig.savefig("plota.pdf")


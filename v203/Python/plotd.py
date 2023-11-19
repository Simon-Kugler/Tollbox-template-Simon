import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

T, p = np.genfromtxt("../Messdaten2_203.txt", unpack=True)

# Fit a polynomial of degree 4, return covariance matrix
params, covariance_matrix = np.polyfit(T, p, deg=3, cov=True)
# Fehllerrechnung
errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip("abcd", params, errors):
    print(f"{name} = {value:.15f} ± {error:.15f}")

fig, ax = plt.subplots(1,1,layout="constrained")

x_p=np.linspace(390,466,10000)
ax.plot(T, p, "r.", label="Messdaten")
ax.plot(
    x_p,
    params[0]*x_p**3+params[1]*x_p**2+params[2]*x_p**1+params[3],
    label="Regression"
)
ax.set_ylabel("T / K")
ax.set_xlabel("p / Pa")
ax.grid()
ax.legend()

fig.savefig("plotd.pdf")
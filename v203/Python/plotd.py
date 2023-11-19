import matplotlib.pyplot as plt
import numpy as np

p, T = np.genfromtxt("../Messdaten2_203.txt", unpack=True)

# Fit a polynomial of degree 1, return covariance matrix
params, covariance_matrix = np.polyfit(p, T, deg=4, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip("abcde", params, errors):
    print(f"{name} = {value:.15f} ± {error:.15f}")

fig, ax = plt.subplots(1, layout="constrained")

x_T=np.linspace(390,466,10000)
ax.plot(p, T, "r", label="Messdaten")
ax.plot(
    x_T,
    params[0]*p**4+params[1]*p**3+params[2]*p**2+params[3]*p+params[4],
    label="Regression"
)
ax.grid()
ax.legend()

fig.savefig("plotd.pdf")
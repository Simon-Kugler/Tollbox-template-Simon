import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams["figure.figsize"]=(10,8)
# plt.rcParams["font.size"]=16

x,y = np.genfromtxt("Messwerte.txt", unpack=True)

fig, ax = plt.subplots(1,1, layout="constrained")

ax.plot(x,y, "k.", label = "Messdaten Hook")

params, covariance_matrix = np.polyfit(x,y,deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip("ab", params, errors):
    print(f"{name}={value:.3f}+-{error:.3f}")

x_plot = np.linspace(0,0.5,1000)
fig, ax = plt.subplots(1,1,layout="constrained")

ax.plot(x,y,".", label="Messwerte")
# ax.set_yscale(0,3)
ax.plot(
    x_plot,
    params[0]*x_plot+params[1],
    label="Lineare Regression",
    linewidth=1
)
ax.set_xlabel(r"$\Delta x$[m]")
ax.set_ylabel(r"$F$[N]")
ax.legend()
fig.savefig("Linreg.pdf")
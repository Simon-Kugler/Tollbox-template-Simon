import matplotlib.pyplot as plt 
# import scipy.optimize
import numpy as np

x = np.linspace(250,380,100000)
T, p = np.genfromtxt("Messdaten1_203.txt", unpack=True)

fig, ax = plt.subplots(1,layout="constrained")
# ax.cla()
ax.plot(T, p, "r.", label="data")
ax.plot(x, 101300*np.exp(-(1/x)*(1522/8.1344)))

ax.set_xlim(0,400)
ax.set_ylim(0,100000)
ax.set_ysclae("log")
ax.legend()
# print(f"Y=1013.25*e^(-(1/T)*(1522/8.13448))+{40}")
fig.savefig("plot_simon1.pdf")
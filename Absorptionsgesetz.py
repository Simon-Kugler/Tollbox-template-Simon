import matplotlib.pyplot as plt 
import numpy as np 

# data_x = np.linspace(0,10)
# data_y = 10 * np.exp(-data_x)
# np.savetxt("Messdaten.txt",np.column_stack([data_x,data_y]), header = "x y")

fig, (ax1,ax2) = plt.subplots(1,2,layout="constrained")

data_x, data_y = np.genfromtxt("Messdaten.txt", unpack=True)

ax1.plot(data_x, data_y, "x")
ax1.set_xlabel(r"$d[cm]$")
ax1.set_ylabel(r"$N[1/60s]$")

ax2.plot(data_x, data_y, "+")
ax2.set_xlabel(r"$d[cm]$")
ax2.set_ylabel(r"$N[1/60s]$")
ax2.set_yscale("log")
fig.savefig("Absorptionsgesetz.pdf")
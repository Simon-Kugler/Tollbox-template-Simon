import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat
from scipy.optimize import curve_fit
from uncertainties import ufloat

f, U_G, U_C2, a, b, b2= np.genfromtxt("messdaten/messdaten2.txt", unpack=True)
x_t=np.linspace(0,5000, 1000)
phi=a/b*np.pi
print(phi)
def x2(f, tau):
    w=2*np.pi*f
    return np.arctan(tau*w )


# Plotten Messdaten
fig, ax = plt.subplots(1,layout="constrained")
ax.plot(f, phi, "rx", label="Messdaten")

#Plotten Fit
# U_C1[U_C1 <= 0] = 1e-10

params, covariance_matrix = curve_fit(x2, f, phi, p0 = [0.52e-3])

print('fit tau', *params, 'pm', covariance_matrix)
ax.plot(x_t, x2(x_t, *params), label = 'Fit')

ax.plot(x_t, x2(x_t, 0.52e-3), label="Theoriekurve")
ax.set_xlabel(r"$f$ / Hz")
ax.set_ylabel(r"$\varphi(\omega)$ / rad")
ax.grid()
ax.legend()
fig.savefig("build/plotc.pdf")
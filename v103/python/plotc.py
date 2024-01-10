import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat
from scipy.optimize import curve_fit
from uncertainties import ufloat

#Messwerte importen
xlR2, xrR2, D_R2l, D_R2r, D_R2Ml, D_R2Mr, e5, e6 = np.genfromtxt("messdaten/rund2.txt", unpack=True)
#def's und anpassungen einheiten
L=0.515
xlR2=xlR2*0.01
x_x=np.linspace(0,L,1000)
xlR2=(4*xlR2**3-12*L*xlR2**2+9*L**2*xlR2-L**3)
e5=e5*0.001

#fit
params, covariance_matrix = np.polyfit(xlR2, e5, deg=1, cov=True)
#Fehler
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.5f} ± {error:.5f}")

fig, ax = plt.subplots(1,layout="constrained")

ax.plot(xlR2, e5,"rx", label="Messdaten")
ax.plot(x_x, params[0]*x_x+params[1], label="lineare Regression")
ax.set_xlabel(r"$(4x^3-12Lx^2+9L^2x-L^3)\,\,/\,\,m^3$")
ax.set_ylabel(r"$D$ / m")
ax.set_xlim(0.02,0.15)
ax.set_ylim(0.0001,0.00037)
ax.legend()
ax.grid()
fig.savefig("build/plotc.pdf")
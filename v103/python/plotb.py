import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Messwerte importen
xlR2, xrR2, D_R2l, D_R2r, D_R2Ml, D_R2Mr, e5, e6 = np.genfromtxt("../messdaten/rund2.txt", unpack=True)

#def's und anpassungen einheiten
L=0.549
xrR2=xrR2*0.01
x_x=np.linspace(0.05,0.2,1000)
xrR2=(3*L**2*xrR2-4*xrR2**3)
e6=e6*0.001

#fit
params, covariance_matrix = np.polyfit(xrR2, e6, deg=1, cov=True)
#Fehler
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.5f} ± {error:.5f}")

fig, ax = plt.subplots(1,layout="constrained")

ax.plot(xrR2, e6,"rx", label="Messdaten")
ax.plot(x_x, params[0]*x_x+params[1], label="lineare Regression")
# ax.set_xscale(0.515*xR1**2-xR1**3/3)
# ax.plot(x_x,0.5*x_x**2-x_x**3/3)
ax.set_xlabel(r"$(3L^2x-4x^3)\,\,/\,\,m^3$")
ax.set_ylabel(r"$D$ / m")
ax.set_xlim(0.065,0.17)
# ax.set_ylim(0,0.003)
ax.legend()
ax.grid()
fig.savefig("../build/plotb.pdf")
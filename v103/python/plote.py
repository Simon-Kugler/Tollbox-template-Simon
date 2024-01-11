import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Messwerte importen
xlQ2, xrQ2, D_Q2l, D_Q2r, D_Q2Ml, D_Q2Mr, e3, e4, e4n, e3n = np.genfromtxt("messdaten/quadr2.txt", unpack=True)

#def's und anpassungen einheiten
L=0.549
xrQ2=xrQ2*0.01
x_x=np.linspace(0,0.2,1000)
xrQ2=(3*L**2*xrQ2-4*xrQ2**3)
e4n=e4n*0.001

#fit
params, covariance_matrix = np.polyfit(xrQ2, e4n, deg=1, cov=True)
#Fehler
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.5f} ± {error:.5f}")

fig, ax = plt.subplots(1,layout="constrained")

ax.plot(xrQ2, e4n,"rx", label="Messdaten")
ax.plot(x_x, params[0]*x_x+params[1], label="lineare Regression")
ax.set_xlabel(r"$(3L^2x-4x^3)\,\,/\,\,m^3$")
ax.set_ylabel(r"$D$ / m")
ax.set_xlim(0.05,0.17)
# ax.set_ylim(0,0.003)
ax.legend()
ax.grid()
fig.savefig("build/plote.pdf")
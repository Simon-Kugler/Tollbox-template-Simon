import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat
from scipy.optimize import curve_fit
from uncertainties import ufloat

#Messwerte importen
xlQ2, xrQ2, D_Q2l, D_Q2r, D_Q2Ml, D_Q2Mr, e3, e4, e4n, e3n = np.genfromtxt("messdaten/quadr2.txt", unpack=True)
#def's und anpassungen einheiten
L=0.549
xlQ2=xlQ2*0.01
x_x=np.linspace(0,0.2,1000)
xlQ2=(4*xlQ2**3-12*L*xlQ2**2+9*L**2*xlQ2-L**3)
e3n=e3n*0.001

#fit
params, covariance_matrix = np.polyfit(xlQ2, e3n, deg=1, cov=True)
#Fehler
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.5f} ± {error:.5f}")

fig, ax = plt.subplots(1,layout="constrained")

ax.plot(xlQ2, e3n,"rx", label="Messdaten")
ax.plot(x_x, params[0]*x_x+params[1], label="lineare Regression")
ax.set_xlabel(r"$(4x^3-12Lx^2+9L^2x-L^3)\,\,/\,\,m^3$")
ax.set_ylabel(r"$D$ / m")
ax.set_xlim(0.05,0.175)
# ax.set_ylim(0.0000,0.0001)
ax.legend()
ax.grid()
fig.savefig("build/plotf.pdf")
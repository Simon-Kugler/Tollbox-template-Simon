import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Messwerte importen
xR1, D_R1, D_RM1, e1 = np.genfromtxt("messdaten/rund1.txt", unpack=True)

#def's und anpassungen einheiten
L=0.515
x_x=np.linspace(0,L,1000)
xR1=xR1*0.01
xR1=L*xR1**2-xR1**3/3
e1=e1*0.001

#fit
params, covariance_matrix = np.polyfit(xR1, e1, deg=1, cov=True)
# xR1=0.515*xR1**2-xR1**3/3
#Fehler
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.5f} ± {error:.5f}")

fig, ax = plt.subplots(1,layout="constrained")

ax.plot(xR1, e1,"rx", label="Messdaten")
ax.plot(x_x, params[0]*x_x+params[1], label="lineare Regression")
# ax.set_xscale(0.515*xR1**2-xR1**3/3)
# ax.plot(x_x,0.5*x_x**2-x_x**3/3)
ax.set_xlabel(r"$(Lx^2-x^3/3)\,\,/\,\,m^3$")
ax.set_ylabel(r"$D$ / m")
ax.set_xlim(0,0.081)
ax.set_ylim(0,0.003)
ax.legend()
ax.grid()
fig.savefig("build/plota.pdf")

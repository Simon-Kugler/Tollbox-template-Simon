import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Messwerte importen
xQ1, D_Q1, D_QM1, e2 = np.genfromtxt("../messdaten/quadr1.txt", unpack=True)
#Berechnung der Dichte etc.
m=ufloat(0.5357,0.0001)
l=ufloat(0.6,0.0001)
d=ufloat(0.01,0.00005)
#Volumen
V=d**2*l 
#Dichte
rho=m/V 
print("Volumen quadratischer Stab: ",V,"m^3")
print("Dichte quadratischer Stab: ",rho,"kg/m^3")
#def's und anpassungen einheiten
L=0.515
x_x=np.linspace(0,L,1000)
xQ1=xQ1*0.01
xQ1=L*xQ1**2-xQ1**3/3
e2=e2*0.001

#fit
params, covariance_matrix = np.polyfit(xQ1, e2, deg=1, cov=True)
#Fehler
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip("ab", params, errors):
    print(f"{name} = {value:.5f} ± {error:.5f}")

fig, ax = plt.subplots(1,layout="constrained")

ax.plot(xQ1, e2,"rx", label="Messdaten")
ax.plot(x_x, params[0]*x_x+params[1], label="lineare Regression")
ax.set_xlabel(r"$(Lx^2-x^3/3)\,\,/\,\,m^3$")
ax.set_ylabel(r"$D$ / m")
ax.set_xlim(0,0.1)
ax.set_ylim(0,0.003)
ax.legend()
ax.grid()
fig.savefig("../build/plotd.pdf")

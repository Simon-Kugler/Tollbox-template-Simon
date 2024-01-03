import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Daten importieren
t, U_C1 = np.genfromtxt("messdaten/messdaten1.txt", unpack=True)
x_t=np.linspace(0,1.5)

#Anpassen der Position der Kurve
t=t+1.3
U_C1=U_C1+3.5
U_0=3.5+3.5

U_C1[U_C1 <= 0] = 1e-10  # Set small positive value for zero or negative entries

#Fit
params, covariance_matrix = np.polyfit(t,np.log(U_C1/U_0), deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip("ab", params, errors):    
    print(f"{name} = {value:.3f} ± {error:.3f}")

#Berechnen von RC
RC=1/ufloat(params[0],errors[0])
print("RC=",RC)
#Plotten Messdaten
fig, ax = plt.subplots(1,layout="constrained")
ax.plot(t, np.log(U_C1/U_0), "rx", label="Messdaten")
#Plotten Fit
ax.plot(x_t, x_t*params[0]+params[1], label="Lineare Regression")
ax.set_xlabel(r"$t$ / ms")
ax.set_ylabel(r"$\ln\left(\frac{U_C}{U_0}\right)$ / V")
ax.grid()
ax.legend()
fig.savefig("build/plota.pdf")
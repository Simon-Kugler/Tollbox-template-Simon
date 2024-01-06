import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Daten importieren
f, U_G, U_C2, a, b, phi = np.genfromtxt("messdaten/messdaten2.txt", unpack=True)
x_t=np.linspace(0,5000)


# U_C1[U_C1 <= 0] = 1e-10  # Set small positive value for zero or negative entries

#Fit
def x1(f,R):
    # U_0=4
    w=2*np.pi*f
    return 1/(np.sqrt(1+w**2*R**2))

params, covariance_matrix = curve_fit(x1,f, U_C2/4)
errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip("R", params, errors):    
    print(f"{name} = {value:.6f} ± {error:.6f}")

#Berechnen von RC
R=params[0]
RC=ufloat(params[0],errors[0])*10**3
print("RC=",RC)
#Plotten Messdaten
fig, ax = plt.subplots(1,layout="constrained")
ax.plot(f, U_C2/4, "rx", label="Messdaten")
#Plotten Fit
ax.plot(x_t, x1(x_t,R),label="Regression")
w=2*np.pi*f
ax.set_xlabel(r"$f$ / Hz")
ax.set_ylabel(r"$\frac{A(\omega)}{U_0}$")
ax.grid()
ax.legend()
fig.savefig("build/plotb.pdf")
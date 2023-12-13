import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import curve_fit
from uncertainties import ufloat
#fits definieren
def x21(x,a,b,c):
    return a*x**2+b*x+c
def x22(x,a,b,c):
    return a*x**2+b*x+c

x_t=np.linspace(1,21,1000)
t, T_b, p_b, T_a, p_a, A = np.genfromtxt("../messdaten/Messdaten.txt", unpack=True)
#Koeffizienten und Fehler berechnen
params1, cov = curve_fit(x21, t, T_b)
errors1 = errors = np.sqrt(np.diag(cov))
params2, cov = curve_fit(x22, t, T_a)
errors2 = errors = np.sqrt(np.diag(cov))
#Koeffizienten und Fehler ausgeben
for name, value, error in zip("a1b1c1", params1, errors1):
    print(f"{name} = {value:.3f} ± {error:.3f}")
print("")
for name, value, error in zip("a2b2c2", params2, errors2):
    print(f"{name} = {value:.3f} ± {error:.3f}")


fig, ax = plt.subplots(1,layout="constrained")

#Messdaten plotten
ax.plot(t, T_b, "rx")
ax.plot(t, T_a, "rx")
#fits plotten
ax.plot(x_t, x21(x_t,*params1))
ax.plot(x_t, x22(x_t,*params2))
ax.set_xlabel(r"$t\,/\,\text{min}$")
ax.set_ylabel(r"$T\,/\,\text{K}$")
ax.set_xlim(0,23)
ax.grid()
ax.legend()
fig.savefig("../build/plota.pdf")

#Ableitung: 2At+B
print("")
print("Differenzenqutient 1 bei t=5")
print(2*params1[0]*5+params1[1])
print("Differenzenqutient 1 bei t=10")
print(2*params1[0]*10+params1[1])
print("Differenzenqutient 1 bei t=15")
print(2*params1[0]*15+params1[1])
print("Differenzenqutient 1 bei t=20")
print(2*params1[0]*20+params1[1])

print("")
print("Differenzenqutient 2 bei t=5")
print(2*params2[0]*5+params2[1])
print("Differenzenqutient 2 bei t=10")
print(2*params2[0]*10+params2[1])
print("Differenzenqutient 2 bei t=15")
print(2*params2[0]*15+params2[1])
print("Differenzenqutient 2 bei t=20")
print(2*params2[0]*20+params2[1])
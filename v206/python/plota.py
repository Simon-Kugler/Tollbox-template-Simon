import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import curve_fit
from uncertainties import ufloat
#fits definieren
def x21(x,a,b,c):
    return a*x**2+b*x+c
def x22(x,a,b,c):
    return a*x**2+b*x+c

x_t=np.linspace(0,25,1000)
t, T_b, p_b, T_a, p_a, A = np.genfromtxt("../messdaten/Messdaten.txt", unpack=True)

params1, cov = curve_fit(x21, t, T_b)
errors1 = errors = np.sqrt(np.diag(cov))
params2, cov = curve_fit(x22, t, T_a)
errors2 = errors = np.sqrt(np.diag(cov))

print(params1, "+-", errors1)
print(params2, "+-", errors2)
fig, ax = plt.subplots(1,layout="constrained")
#Messdaten plotten
ax.plot(t, T_b, "rx")
ax.plot(t, T_a, "rx")
#fits plotten
ax.plot(x_t, x21(x_t,*params1))
ax.plot(x_t, x22(x_t,*params2))

fig.savefig("../build/plota.pdf")
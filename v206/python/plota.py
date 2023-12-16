import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import curve_fit
from uncertainties import ufloat
#fits definieren
def x21(x,a,b,c):
    return a*x**2+b*x+c
def x22(x,a,b,c):
    return a*x**2+b*x+c

x_t=np.linspace(1,1300,1000)
t, T_b, p_b, T_a, p_a, A = np.genfromtxt("../messdaten/Messdaten.txt", unpack=True)
t = t * 60
#T_a = T_a + 273.15
#T_b = T_b + 273.15
#Koeffizienten und Fehler berechnen
params1, cov1 = curve_fit(x21, t, T_b)
errors1 = errors = np.sqrt(np.diag(cov1))
params2, cov2 = curve_fit(x22, t, T_a)
errors2 = errors = np.sqrt(np.diag(cov2))
#params2 = params2 * 1000000
#params1 = params1 * 1000000
#errors1 = errors1 * 1000000
#errors2 = errors2 * 1000000
#Koeffizienten und Fehler ausgeben
for name, value, error in zip("abc", params1, errors1):
    print(f"{name} = {value:.3f} ± {error:.3f}")
print("")
for name, value, error in zip("abc", params2, errors2):
    print(f"{name} = {value:.3f} ± {error:.3f}")


fig, ax = plt.subplots(1, layout="constrained")

#Messdaten plotten
ax.plot(t, T_b, "rx", label="Messdaten $T_1$")
ax.plot(t, T_a, "cx", label="Messdaten $T_2$")
#fits plotten
ax.plot(x_t, x21(x_t,*params1), label="Ausgleichsgerade $T_1$")
ax.plot(x_t, x22(x_t,*params2), label="Ausgleichsgerade $T_2$")
ax.set_xlabel(r"$t\,/\,\text{s}$")
ax.set_ylabel(r"$T\,/\,\text{K}$")
#ax.set_xlim(0,23)
ax.grid()
ax.legend()
fig.savefig("../build/plota.pdf")

#Ableitung: 2At+B
print("")
print("Differenzenqutient 1 bei t=5")
print(2*params1[0]*5*60+params1[1], "+/-", 2*errors1[0]*5*60+errors1[1])
print("Differenzenqutient 1 bei t=10")
print(2*params1[0]*10*60+params1[1], "+/-", 2*errors1[0]*10*60+errors1[1])
print("Differenzenqutient 1 bei t=15")
print(2*params1[0]*15*60+params1[1], "+/-", 2*errors1[0]*15*60+errors1[1])
print("Differenzenqutient 1 bei t=20")
print(2*params1[0]*20*60+params1[1], "+/-", 2*errors1[0]*20*60+errors1[1])

print("")
print("Differenzenqutient 2 bei t=5")
print(2*params2[0]*5*60+params2[1], "+/-", 2*errors2[0]*5*60+errors2[1])
print("Differenzenqutient 2 bei t=10")
print(2*params2[0]*10*60+params2[1], "+/-", 2*errors2[0]*10*60+errors2[1])
print("Differenzenqutient 2 bei t=15")
print(2*params2[0]*15*60+params2[1], "+/-", 2*errors2[0]*15*60+errors2[1])
print("Differenzenqutient 2 bei t=20")
print(2*params2[0]*20*60+params2[1], "+/-", 2*errors2[0]*20*60+errors2[1])


dT1dt = [0, 0, 0, 0]
dT2dt = [0, 0, 0, 0]
dT1dte = [0, 0, 0, 0]
dT2dte = [0, 0, 0, 0]
for i in range (0, 4, 1):
    dT1dt[i] = 2*params1[0]*i*60+params1[1]

for i in range (0, 4, 1):
    dT2dt[i] = 2*params2[0]*i*60+params2[1]

for i in range (0, 4, 1):
    dT1dte = 2*errors1[0]*i*60+errors1[1]

for i in range (0, 4, 1):
    dT2dte = 2*errors2[0]*i*60+errors2[1]


v_real = [0, 0, 0, 0]
N = [200.0, 206.0, 210.0, 205.0]
m_1 = m_2 = 3.0
mc_k = 750.0
c_w = 4200.0

#print("T1 reale Gueteziffer")
#for i in range (0, 4, 1):
#    #v_real[i] = (1/N[i]) * (m_1 * c_w + mc_k) * dT1dt
#    print(v_real[i])
#print("T2 reale Gueteziffer")
#for i in range (0, 4, 1):
#    #v_real[i] = 1/N[i] * (m_1 * c_w + mc_k) * dT2dt
#    print(v_real[i])

v_ideal = [0, 0, 0, 0, 0]

print("ideale Gueteziffer:")
for i in range (1, 5, 1):
    v_ideal[i] = (T_b[5*i])/(T_b[5*i] - T_a[5*i])
    print(5*i, v_ideal[i])


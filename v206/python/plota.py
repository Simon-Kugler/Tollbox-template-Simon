import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import curve_fit
from uncertainties import ufloat
#fits definieren
def x21(x,a,b,c):
    return a*x**2+b*x+c
def x22(x,a,b,c):
    return a*x**2+b*x+c

x_t=np.linspace(-5,1300,1000)
t, T_b, p_b, T_a, p_a, A = np.genfromtxt("messdaten/Messdaten.txt", unpack=True)
t = t * 60
#T_a = T_a + 273.15
#T_b = T_b + 273.15
#Koeffizienten und Fehler berechnen
params1, cov = curve_fit(x21, t, T_b)
errors1 = errors = np.sqrt(np.diag(cov))
params2, cov = curve_fit(x22, t, T_a)
errors2 = errors = np.sqrt(np.diag(cov))
#Koeffizienten und Fehler ausgeben
print("1. Fit")
for name, value, error in zip("abc", params1, errors1):
    print(f"{name} = {value:.10f} ± {error:.10f}")
print("2. Fit")
for name, value, error in zip("abc", params2, errors2):
    print(f"{name} = {value:.10f} ± {error:.10f}")


fig, ax = plt.subplots(1,layout="constrained")

#Messdaten plotten
ax.plot(t, T_b, "rx")
ax.plot(t, T_a, "rx")
#fits plotten
ax.plot(x_t, x21(x_t,*params1))
ax.plot(x_t, x22(x_t,*params2))
ax.set_xlabel(r"$t\,\,/\,\,\text{s}$")
ax.set_ylabel(r"$T\,\,/\,\,\text{K}$")
ax.set_xlim(-10,1300)
ax.grid()
ax.legend()
fig.savefig("build/plota.pdf")

#Ableitung: 2At+B
print("")
print("Differenzenqutient 1 bei t=5")
dT_11dt=2*params1[0]*5*60+params1[1]
print(dT_11dt)
print("Differenzenqutient 1 bei t=10")
dT_12dt=2*params1[0]*10*60+params1[1]
print(dT_12dt)
print("Differenzenqutient 1 bei t=15")
dT_13dt=2*params1[0]*15*60+params1[1]
print(dT_13dt)
print("Differenzenqutient 1 bei t=20")
dT_14dt=2*params1[0]*20*60+params1[1]
print(dT_14dt)

dT1dt=np.array([dT_11dt,dT_12dt,dT_13dt,dT_14dt])
print("")
print("Differenzenqutient 2 bei t=5")
dT_21dt=2*params2[0]*5*60+params2[1]
print(dT_21dt)
print("Differenzenqutient 2 bei t=10")
dT_22dt=2*params2[0]*10*60+params2[1]
print(dT_22dt)
print("Differenzenqutient 2 bei t=15")
dT_23dt=2*params2[0]*15*60+params2[1]
print(dT_23dt)
print("Differenzenqutient 2 bei t=20")
dT_24dt=2*params2[0]*20*60+params2[1]
print(dT_24dt)

dT2dt=np.array([dT_21dt,dT_22dt,dT_23dt,dT_24dt])

# dT1dt = [0, 0, 0, 0, 0]
# dT2dt = [0, 0, 0, 0, 0]
# dT1dte = [0, 0, 0, 0, 0]
# dT2dte = [0, 0, 0, 0, 0]
# for i in range (1, 5, 1):
    # dT1dt[i] = 2*params1[0]*i*5*60+params1[1]
    # print(5*i)
# 
# for i in range (1, 5, 1):
    # dT2dt[i] = 2*params2[0]*i*5*60+params2[1]
# 
# for i in range (1, 5, 1):
    # dT1dte[i] = 2*errors1[0]*i*5*60+errors1[1]
# 
# for i in range (1, 5, 1):
    # dT2dte[i] = 2*errors2[0]*i*5*60+errors2[1]


v_real = [0, 0, 0, 0]
N = [200.0, 206.0, 210.0, 205.0]
m_1 = m_2 = 3.0
mc_k = 750.0
c_w = 4200.0
# print("dT1dt", dT1dt)
# print("dT1dte", dT1dte)
# print("dT2dt", dT2dt)
# print("dT2dte", dT2dte)

print("T1 reale Gueteziffer")
for i in range (0, 4, 1):
   v_real[i] = (1/N[i]) * (m_1 * c_w + mc_k) * dT1dt
   print(v_real[i])
print("T2 reale Gueteziffer")
for i in range (0, 4, 1):
   v_real[i] = 1/N[i] * (m_1 * c_w + mc_k) * dT2dt
   print(v_real[i])

v_ideal = [0, 0, 0, 0, 0]

print("ideale Gueteziffer:")
for i in range (1, 5, 1):
    v_ideal[i] = (T_a[5*i]+273.15)/(T_a[5*i]+273.15 - T_b[5*i]-273.15)
    print(5*i, v_ideal[i])

m =ufloat(2726.2816288047175,179.00481892007065)
b =ufloat(4.1229755871964695,0.5793950001616602)
L2=ufloat(22700,1500)
#L Einheit umrechnen von J/mol in g/mol
L2=L2/120.913
#Massendurchsatz bestimmen
#dQ_2/dt=(m_1c_w+m_kc_k)dT_1/dT
Qt1=(m_1*c_w+mc_k)*dT_21dt/L2
Qt2=(m_1*c_w+mc_k)*dT_22dt/L2
Qt3=(m_1*c_w+mc_k)*dT_23dt/L2
Qt4=(m_1*c_w+mc_k)*dT_24dt/L2
print("Qt1", Qt1)
print("Qt2", Qt2)
print("Qt3", Qt3)
print("Qt4", Qt4)

#Mechanische Leistung
k=1.14
rho_0=5.51
T_0=273.15
#Messdaten und Einheiten ändern in Pascal sowie Kelvin 
p_a1=2.1*10**5 
p_a2=2.2*10**5 
p_a3=2.3*10**5
p_a4=2.2*10**5
p_b1=7.5*10**5 
p_b2=9.4*10**5 
p_b3=11.0*10**5
p_b4=12.5*10**5
T_21=17.4+273.15
T_22=9.0+273.15
T_23=3.4+273.15
T_24=0.9+273.15
#Einheit Massendurchsatz ändern
Qt11=Qt1*10**(-3)
Qt12=Qt2*10**(-3)
Qt13=Qt3*10**(-3)
Qt14=Qt4*10**(-3)
#Formel für rho
# rho=(rho_0*T_0*p_a)/(T_21*p_a)
#1
rho1=(rho_0*T_0*p_a1)/(T_21*p_a1)
print(rho1)
#2
rho2=(rho_0*T_0*p_a2)/(T_22*p_a2)
print(rho2)
#3
rho3=(rho_0*T_0*p_a3)/(T_23*p_a3)
print(rho3)
#4
rho4=(rho_0*T_0*p_a4)/(T_24*p_a4)
print(rho4)
#Formel für mechanische Leistung
#1
N1=1/(k-1)*(p_b1*((p_a1/p_b1)**(1/1.14))-p_a1)*1/rho1*(Qt11)
#2
N2=1/(k-1)*(p_b2*((p_a2/p_b2)**(1/1.14))-p_a2)*1/rho2*(Qt12)
#3
N3=1/(k-1)*(p_b3*((p_a3/p_b3)**(1/1.14))-p_a3)*1/rho3*(Qt13)
#4
N4=1/(k-1)*(p_b4*((p_a4/p_b4)**(1/1.14))-p_a4)*1/rho4*(Qt14)
print("N1=",N1)
print("N2=",N2)
print("N3=",N3)
print("N4=",N4)
# python 3.x
# import numpy as npobject
# 
# a = 9
# n = 2
# result = npobject.power(a, (1 / n))
# print(f"The {n}th root of value = {a} is:", r
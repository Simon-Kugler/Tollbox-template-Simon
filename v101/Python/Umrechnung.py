import numpy as np
from uncertainties import ufloat
from sympy import *

# K, Z = np.genfromtxt("../Messwerte/Kugel_Zylinder.txt",unpack=True)

# K1=K/5
# Z1=Z/5
# for i in range(0,10):
#     print(K1[i])
# print("pause")
# for i in range(0,10):
#     print(Z1[i])

# avg_K=np.average(K1)
# print("avg_K=",avg_K)
# std_K=np.std(K1)
# print("std_K=",std_K)
#Puppe Abmessungen Durchmesser
B=np.array([13.04, 13.24, 14.32, 16.58, 17.00, 16.00, 16.78, 19.42, 18.54, 16.68])
A=np.array([11.84, 11.18, 12.46, 14.42, 14.52, 13.04, 12.88, 13.24, 14.32, 13.14])
T=np.array([32.96,  37.56,  38.74,  33.34,  25.10,  26.08,31.08,36.08,39.22,40.37])
K=np.array([22.56,27.36,28.44,27.86,24.82])
#Durchmesser zu Radius
B=B/2
T=T/2
K=K/2
A=A/2
#Höhen
H_A=133.12
H_B=136.58
H_T=99.02
H_K=42.02
#Radien mit Fehler initialisieren
r_A=ufloat(np.average(A),np.std(A))
r_B=ufloat(np.average(B),np.std(B))
r_T=ufloat(np.average(T),np.std(T))
r_K=ufloat(np.average(K),np.std(K))
#Radien ausgeben
print("r_A=",r_A)
print("r_B=",r_B)
print("r_T=",r_T)
print("r_K=",r_K)
#Volumina
V_A=r_A**2*np.pi*H_A
V_B=r_B**2*np.pi*H_B
V_T=r_T**2*np.pi*H_T
V_K=r_K**2*np.pi*H_K
#Volumina ausgeben
print("V_A=",V_A)
print("V_B=",V_B)
print("V_T=",V_T)
print("V_K=",V_K)

V_Ges=2*V_A+2*V_B+V_T+V_K
print("V_Ges=",V_Ges)

#Massen berechnen
M=167.2
V=205295.5
m_A=(V_A/V_Ges)*M
m_B=(V_B/V_Ges)*M
m_T=(V_T/V_Ges)*M
m_K=(V_K/V_Ges)*M
#Massen ausgeben
print("m_A=",m_A)
print("m_B=",m_B)
print("m_T=",m_T)
print("m_K=",m_K)

#Gauß die zweite
m_A=(V_A/V_Ges)*M
m_B=(V_B/V_Ges)*M
m_T=(V_T/V_Ges)*M
m_K=(V_K/V_Ges)*M

print("V_Ges=",2*V_A + 2*V_B + V_T + V_K)

#Trägheitsmoment 1
I_A1=m_A*((r_A**2)/4+((r_T*0.5*H_A)**2)/12)
I_2B1=m_B**2*r_B**2
I_T1=(m_T*r_T**2)/2
I_K1=(m_K*r_K**2)/2

I_A=I_A1*10**(-9)
I_2B=I_2B1*10**(-9)
I_T=I_T1*10**(-9)
I_K=I_K1*10**(-9)

print("I_A=" ,'{:1.10f}'.format(I_A1))
print("I_2B=",'{:1.10f}'.format(I_2B1))
print("I_T=" ,'{:1.10f}'.format(I_T1))
print("I_K=" ,'{:1.10f}'.format(I_K1))
#Gesamtträgheitsmoment 1
I_G1=2*I_A1+2*I_2B1+I_K1+I_T1
I_G=2*I_A+2*I_2B+I_K+I_T
print("I_G1=",'{:1.10f}'.format(I_G1))
print("I_THEORIE_1=",'{:1.10f}'.format(I_G))

#Schwingunsdauern 1
D=ufloat(0019.97,0.00466)

phi_90=np.array([3.06, 3.28, 2.72, 3.06, 3.16,2.88, 2.87, 2.87, 2.84, 2.90])

phi_1=phi_90/5

Phi_1=ufloat(np.average(phi_1),np.std(phi_1))
I_1e=Phi_1**2/(2*np.pi)*D
print("I_1e=",I_1e)

#Trägheitsmoment 2
I_2B2=2*m_B*((2*r_B)**2/4+(r_T*0.5*H_B)**2/12)
print("I_2B2=",I_2B2)
I_G2=I_2B2+2*I_A+I_T+I_K
I_G2=I_G2*10**(-9)
print("I_THEORIE2=",I_G2)

#Schwingungsdauern 2
phi1_90=np.array([4.84, 4.87, 4.72, 4.93, 4.79,4.85, 4.94, 4.90, 4.97, 4.94])

phi_2=phi1_90/5

Phi_2=ufloat(np.average(phi_2),np.std(phi_2))

I_2e=Phi_2**2/(2*np.pi)*D
print("I_2e=",I_2e)




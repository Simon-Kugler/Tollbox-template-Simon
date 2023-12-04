import numpy as np
from uncertainties import ufloat
from sympy import *

K, Z = np.genfromtxt("../Messwerte/Kugel_Zylinder.txt",unpack=True)

K1=K/5
Z1=Z/5
for i in range(0,10):
    print(K1[i])
print("pause")
for i in range(0,10):
    print(Z1[i])

avg_K=np.average(K1)
print("avg_K=",avg_K)
std_K=np.std(K1)
print("std_K=",std_K)
B=np.array([13.04, 13.24, 14.32, 16.58, 17.00, 16.00, 16.78, 19.42, 18.54, 16.68])
A=np.array([
11.84, 
11.18, 
12.46, 
14.42, 
14.52, 
13.04,
12.88,
13.24,
14.32,
13.14,
])
T=np.array([
32.96,  
37.56,  
38.74,  
33.34,  
25.10,  
26.08,
31.08,
36.08,
39.22,
40.37,
])
K=np.array([
22.56,
27.36,
28.44,
27.86,
24.82,
])
B=B/2
T=T/2
K=K/2
A=A/2
print("A=",ufloat(np.average(A),np.std(A)))
print("B=",ufloat(np.average(B),np.std(B)))
print("T=",ufloat(np.average(T),np.std(T)))
print("K=",ufloat(np.average(K),np.std(K)))

#Gaußscher Fehler
x_A=np.sqrt(((2*np.pi*6.6*133.12)**2)*(0.5)**2+(np.pi*(6.6)**2)*(0.05)**2)
x_B=np.sqrt((2*np.pi*8.1*136.58)**2*(1)**2+(np.pi*(8.1)**2)*(0.05)**2)
x_T=np.sqrt((2*np.pi*17.0*99.02)**2*(2.5)**2+(np.pi*(17.0)**2)*(0.05)**2)
x_K=np.sqrt((2*np.pi*13.1*42.02)**2*(1.1)**2+(np.pi*(13.1)**2)*(0.05)**2)
print("V_A=",ufloat(6.6**2*np.pi*133.12,x_A))
print("V_B=",ufloat(8.1**2*np.pi*136.58,x_B))
print("V_T=",ufloat(17.0**2*np.pi*99.02,x_T))
print("V_K=",ufloat(13.1**2*np.pi*42.02,x_K))
x_Ges=np.sqrt(2*(0.28)**2+2*(0.7)**2+2*(2.6)**2+2*(0.4)**2)
V_Ges=2*(6.6**2*np.pi*133.12)+2*(8.1**2*np.pi*136.58)+(17.0**2*np.pi*99.02)+(13.1**2*np.pi*42.02)
print("V_Ges=",ufloat(V_Ges,x_Ges))
print(x_Ges)
print(V_Ges)

M=167.2
V=205295.5
m_A=((6.6**2*np.pi*133.12)/V)*M
m_B=((8.1**2*np.pi*136.58)/V)*M
m_T=((17.0**2*np.pi*99.02)/V)*M
m_K=((13.1**2*np.pi*42.02)/V)*M
print("m_A=",m_A)
print("m_B=",m_B)
print("m_T=",m_T)
print("m_K=",m_K)

#Gauß die zweite


V_A=ufloat(6.6**2*np.pi*133.12,x_A)
V_B=ufloat(8.1**2*np.pi*136.58,x_B)
V_T=ufloat(17.0**2*np.pi*99.02,x_T)
V_K=ufloat(13.1**2*np.pi*42.02,x_K)
V_Ges1=ufloat(V_Ges,x_Ges)
m_A=(V_A/V_Ges1)*M
m_B=(V_B/V_Ges1)*M
m_T=(V_T/V_Ges1)*M
m_K=(V_K/V_Ges1)*M

print("m_A=",m_A)
print("m_B=",m_B)
print("m_T=",m_T)
print("m_K=",m_K)

print("V_Ges=",2*V_A + 2*V_B + V_T + V_K)
#  print("x_A=",x_A)
# print("V_A=",0.0066**2*np.pi*0.04202)
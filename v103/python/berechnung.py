import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat
from scipy.optimize import curve_fit
from uncertainties import ufloat

# Rund Messung 1
xR1, D_R1, D_RM1, e1 = np.genfromtxt("../messdaten/rund1.txt", unpack=True)
dD_R1=D_R1-D_RM1
for i in range(0,16):
    print(dD_R1[i])
print("")
print("")
#Quadratisch Messung 1
xQ1, D_Q1, D_QM1, e2 = np.genfromtxt("../messdaten/quadr1.txt", unpack=True)
dD_Q1=D_Q1-D_QM1
for i in range(0,16):
    print(dD_Q1[i])
print("")
print("")
#Quadratische Messung 2
xlR2, xrR2, D_R2l, D_R2r, D_R2Ml, D_R2Mr, e3, e4 = np.genfromtxt("../messdaten/rund2.txt", unpack=True)
#links
dD_R2l=D_R2l-D_R2Ml
#rechts
dD_R2r=D_R2r-D_R2Mr
for i in range(0,11):
    print(dD_R2l[i])
print("")
print("")
for i in range(0,11):
    print(dD_R2r[i])
print("")
print("")
#Runde Messung 2
xlQ2, xrQ2, D_Q2l, D_Q2r, D_Q2Ml, D_Q2Mr, e5, e6 = np.genfromtxt("../messdaten/quadr2.txt", unpack=True)
#links
dD_Q2l=D_Q2l-D_Q2Ml
#rechts
dD_Q2r=D_Q2r-D_Q2Mr
for i in range(0,10):
    print(dD_Q2l[i])
print("")
print("")
for i in range(0,10):
    print(dD_Q2r[i])
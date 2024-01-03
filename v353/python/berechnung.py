import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat
from scipy.optimize import curve_fit
from uncertainties import ufloat
#wt+phi=pi/2

f, U_G, U_C2, a, b, phi, b2 = np.genfromtxt("../messdaten/messdaten2.txt", unpack=True)

w=2*np.pi*f
b1=1/f
print (b1)
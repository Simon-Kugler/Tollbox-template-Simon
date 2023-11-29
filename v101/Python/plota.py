import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

phi, F = np.genfromtxt("../Messwerte/Winkelrichtgroesse.txt", unpack=True)

phil = len(phi)
Fl = len(F)

#Mittelwerte bestimmen
Fx = 0
phix = 0
for x in range(0,len(phi)):
    phix += phi[x]

for y in range(0,len(F)):
    Fx += F[y]

print("Mittelwert von Phi =", phix/phil)
print("Mittelwert von F = ", Fx/Fl)
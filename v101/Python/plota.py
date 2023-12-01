import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

Phi, F = np.genfromtxt("../Messwerte/Winkelrichtgroesse.txt", unpack=True)
D = np.zeros(10)
# phi in rad
Phin = Phi * np.pi / 180

Phil = len(Phin)
Fl = len(F)
Dl = len(D)

#Mittelwerte bestimmen
Fx = 0
Phix = 0
Dx = 0

D = np.zeros(10)
for f, phi, i in zip(F, Phin, range(0, Phil)):
    D[i] = f * 0.2 / phi

for x in range(0, Phil):
    Phix += Phin[x]

for y in range(0, Fl):
    Fx += F[y]

for d in range(0, Dl):
    Dx += D[d]
print("Mittelwert von Phi =", Phix/Phil)
print("Mittelwert von F = ", Fx/Fl)
print("Mittelwert von D = ", Dx/Dl)





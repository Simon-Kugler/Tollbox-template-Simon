import numpy as np

K, Z = np.genfromtxt("../Messwerte/Kugel_Zylinder.txt", unpack=True)

Z = Z / 5
print("Z = ", Z)

print("Standartabweichung von T_Z = ", np.std(Z))
print("Mittelwert von T_Z = ", np.mean(Z))

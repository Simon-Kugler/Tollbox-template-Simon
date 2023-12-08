import numpy as np
import matplotlib.pyplot as plt 

#Daten importieren
f, U_Br = np.genfromtxt("../Messdaten/Frequenzabhängigkeit.txt",unpack=True)
#Umrechnung in Volt
U_Br=U_Br*10**(-3)
#Omega berechnen
x = f/241
#y-Achse
y = (U_Br/0.5)**2
#Messwerte plotten
plt.plot(x, y, "rx", label='Messwerte')
#Theoriekurve
plt.plot(x, (1)/(9) * ((x**2 -1)**2)/(((1-x**2)**2)+9*x**2),"b", label='Theoriekurve')

plt.xlabel(r'$\Omega = \frac{\nu}{\nu_0}$')
plt.xscale('log')
plt.ylabel(r'$\left(\frac{U_{Br}}{U_s}\right)^2$')
plt.grid()
plt.legend(loc='best')

plt.savefig("fit.pdf")
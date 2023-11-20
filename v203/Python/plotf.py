import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

T=np.linspace(390,466,10000)
a = 0.020709167025828
b = -24.652993974197063
c = 9879.126807499247661
d = -1330791.268963911104947
fig, ax = plt.subplots(1,layout="constrained")

ax.plot(T, (T/(a*T**3+b*T**2+c*T+d))*-((8.31448*T)/2+(np.sqrt(((8.31448**2*T**2)/4)-0.9*(a*T**3+b*T**2+c*T+d))))*(3*a*T**2+2*b*T+c), 
label="Negative Lösung für $L$")
ax.set_xlabel("T / K")
ax.set_ylabel("L ")
ax.grid()
ax.legend()

fig.savefig("plotf.pdf")
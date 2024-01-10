import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Formel für Flächenträgheitsmomente
#rund I_r=pi*d^4/64
#quadrat I_q=b^4/12

#runder Stab beidseitig
m_2=1
d=ufloat(0.01,0.00005)
g=9.806
F=m_2*g 
I_r=np.pi*d**4/64
print(I_r)
#links
a_b=ufloat(0.002,0.0004)
E_b=F/(48*a_b*I_r)*10**(-9)
print("E_b: ",E_b)
#rechts
a_c=ufloat(0.0016,0.00029)
E_c=F/(48*a_c*I_r)*10**(-9)
print("E_c: ",E_c)
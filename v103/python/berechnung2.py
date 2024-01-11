import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Formel für Flächenträgheitsmomente
#rund I_r=pi*d^4/64
#quadrat I_q=b^4/12
m_1=0.5
g=9.806
F_1=m_1*g 
d=ufloat(0.01,0.00005)
I_r=np.pi*d**4/64
#runder Stab einseitig
a_a=ufloat(0.034,0.0019)
E_a=F_1/(2*a_a*I_r)*10**(-9)
print("E_a: ",E_a)
#runder Stab beidseitig
m_2=1
F_2=m_2*g 
print(I_r)
#links
a_b=ufloat(0.002,0.0004)
E_b=F_2/(48*a_b*I_r)*10**(-9)
print("E_b: ",E_b)
#rechts
a_c=ufloat(0.0016,0.00029)
E_c=F_2/(48*a_c*I_r)*10**(-9)
print("E_c: ",E_c)

#quadratischer stab einseitig
I_q=d**4/12
a_d=ufloat(0.026,0.0003)
E_d=F_1/(2*a_d*I_q)*10**(-9)
print("E_d: ",E_d)
#beidseitig
#links
a_e=ufloat(0.00053,0.00012)
E_e=F_2/(48*a_e*I_q)*10**(-9)
print("E_e: ",E_e)
#rechts
a_f=ufloat(0.00062,0.0006)
E_f=F_2/(48*a_f*I_q)*10**(-9)
print("E_f: ",E_f)
print("Flächenträgheitsmoment rund: ", I_r)
print("Flächenträgheitsmoment quadratisch: ",I_q)
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import scipy.constants as const
from uncertainties import ufloat

t, T_b, p_b, T_a, p_a, A = np.genfromtxt("../messdaten/Messdaten.txt", unpack=True)
t = t * 60
x = np.linspace(290, 330, 1000)

T_b = T_b + 273.15
T_a = T_a + 273.15
T_b = 1/T_b
p_b = np.log(p_b/1001)
T_a = 1/T_a
p_a = np.log(p_a/1001)
x = 1/x

fig, ax = plt.subplots(1,layout="constrained")
#ax.plot(T_a, p_a, "rx", label="Messwertea")
ax.plot(T_b, p_b, "bx", label="Messwerteb")

#der Fit
def fit(T1, L, b):
   return L * T1 + b

#params, cov = curve_fit(fit, T_a, p_a)
#errors = errors = np.sqrt(np.diag(cov))
paramsb, covb = curve_fit(fit, T_b, p_b)
errors2b = errorsb = np.sqrt(np.diag(covb))

#print("aparams", params)
#print("aerrors", errors)
print("bparams", paramsb)
print("berrors", errorsb)
#ma = - params[0]
mb = - paramsb[0]
print("m = ", mb, "±", errorsb[0])
print("b = ", paramsb[1], "±", errorsb[1])

ax.plot(x, fit(x, *paramsb), "b-", label="Ausgleichsgerade")

ax.set_xlabel(r"$1/T$ ")
ax.set_ylabel(r"$\ln\left(\frac{p}{p_0}\right)$")
ax.grid()
ax.legend()
fig.savefig("../build/Verdampfungswärme.pdf")

#L1=ufloat(ma,errors[0])*const.R
L2=ufloat(mb, errorsb[0])*const.R
#print("L1=",L1,)
print("L2=",L2,)
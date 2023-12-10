from uncertainties import ufloat
import numpy as np
#Wheatonsche Brückenschaltung R_x = R_2*R_3/R_4
#Wert 10
print("Wheatonsche Brückenschaltung")
R_12=664
R_13=290
R_14=710
R_11=R_12*(R_13/R_14)
R_11=ufloat(R_11,(R_11*0.005))
print("R_11 =",R_11)
R10=239
print("Abweichung: ",(R_11-R10)/R10*100,"%")
#Wert 12
R_22=664
R_23=327
R_24=673
R_21=R_12*(R_23/R_24)
R_21=ufloat(R_21,(R_21*0.005))
R12=390.4
print("R_21 =",R_21)
print("Abweichung: ",(R_21-R12)/R12*100,"%")
print("")
print("Kapazitätsmessbrücke")
#Kapazitätsmessbrücke
#R Wert 12, C Wert 1
C_32=399
R_32=664
R_33=372
R_34=628 
R_31=R_32*(R_33/R_34)
R_31=ufloat(R_31,0.005*R_31)
C1=660
print("R_31 =",R_31)
print("Abweichung R: ",(R_31-R12)/R12*100,"%")
C_31 = C_32*R_34/R_33
C_31=ufloat(C_31,0.005*C_31)
print("C_31 =",C_31)
print("Abweichung C:  ",(C_31-C1)/C1*100,"%")
#C_x= 2*Wert 3
C_42=399
R_42=664
R_43=358
R_44=642
R_41=R_42*R_43/R_44
R_41=ufloat(R_41,0.005*R_41)
print("R_41 =",R_41)
print("Abweichung R: ",(R_41-R12)/R12*100,"%")
C_41 = C_42*R_44/R_43
C_41=ufloat(C_41,0.005*C_41)
C3=839.89
print("C_41 =",C_41)
print("Abweichung C: ",(C_41-C3)/C3*100,"%")
print("")
print("Induktivitätsmessbrücke")
#Induktivitätsmessbrücke
#L_x=L_2*R_3/R_4
#L, R Wert 19
L_52=27.5
R_52=664
R_53=191
R_54=809
R_51=R_52*R_53/R_54
R19=108.7
R_51=ufloat(R_51,0.005*R_51)
print("R_51 =",R_51)
print("Abweichung R: ",(R_51-R19)/R19*100,"%")
L_51=L_52*R_53/R_54
L_51=ufloat(L_51,0.005*L_51)
L19=26.96
print("L_51 = ",L_51)
print("Abweichung L: ",(L_51-L19)/L19*100,"%")
print("")
#Maxwellbrücke
# L, R Wert19 
# L_x=R_2*R_3*C_4
print("Maxwellbrücke")
R_62=664
R_63=ufloat(37,37*0.03)
R_64=ufloat(395,395*0.03)
C_64=399*10**(-9)
R_61=R_62*R_63/R_64
print("R_61 =",R_61)
print("Abweichung R: ",(R_61-R19)/R19*100,"%")
L_61=R_62*R_63*C_64
print("L_61 =",L_61*10**3)
print("Abweichung L: ",(L_61-L19)/L19*100,"%")

#Klirrfaktor
U_S=0.5
f_2=np.sqrt((1/9)*((2**2-1)**2)/((1-2**2)**2+9*2**2))
U_Br=np.sqrt(0.5/f_2)
U_2=U_Br/f_2
print(U_Br)
print(U_Br/f_2)
k=U_2/0.5
print(k)
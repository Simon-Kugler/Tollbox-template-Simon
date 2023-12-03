import numpy as np

K, Z = np.genfromtxt("../Messwerte/Kugel_Zylinder.txt",unpack=True)

K1=K/5
Z1=Z/5
for i in range(0,10):
    print(K1[i])
print("pause")
for i in range(0,10):
    print(Z1[i])

avg_K=np.average(K1)
print("avg_K=",avg_K)
std_K=np.std(K1)
print("std_K=",std_K)
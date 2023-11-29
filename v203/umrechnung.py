import matplotlib.pyplot as plt
import numpy as np

T, p = np.genfromtxt("Messdaten1_203.txt", unpack=True)

for x in T:
    x=T-273.15

for i in range(20,100):
    print(i)
import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
data = np.loadtxt("gauss.dat")

x = np.linspace(data.min(), data.max(), 1000)
y = np.exp(-x**2/2)/np.sqrt(2.0*np.pi)

_ = plt.hist(data, bins=30, density=True, label='Metropolis-Hastings')
plt.plot(x, y, label='Gaussiana')

plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("gaussian_metropolis.png")
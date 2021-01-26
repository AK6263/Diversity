from matplotlib import pyplot as plt
import pandas as pd 
import numpy as np
import random
from scipy.optimize import curve_fit

df = pd.read_csv("Trees.csv", nrows=10000) # We will only read first 10000 values
cols = ['Unnamed: 0', 'tag', 'mnem', 'gx', 'gy']

Trees = df['mnem'].tolist()
N = len(Trees)

K1 = [i for i in range(100,3000,500)]
K2 = [i for i in range(3000,6000,1000)]
K3 = [i for i in range(6000,10001,1500)]

K = K1 + K2 + K3
k = len(K)
ns = 10

output = np.zeros((k,ns))

for i in range(k):
    for j in range(ns):
        rows = random.sample(Trees, K[i])
        output[i,j] = len(set(rows))


means = []
for samples in output:
    means.append(np.mean(samples))

plt.scatter(K, means, c="orange")

# FITTING THE CURVE 
def f(x,a,c):
    return c * np.log10(x*a)

X = np.linspace(100, 10001, num = 5000)
popt,pcov = curve_fit(f, K, means, maxfev= 2000)
Y = f(X, *popt)
plt.plot(X,Y) 
plt.title("Species Abbundance Plot")
plt.xlabel("Samples")
plt.ylabel("Unique Individuals")
plt.show()





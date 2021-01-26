import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import random

df = pd.read_csv("bird_diversity_data.csv")
name = df["Name"].to_list()
no = df["No"].to_list()

# Creating New Data Frame
individuals = []
for i,n in enumerate(no):
    for k in range(n):
        individuals.append(name[i])

random.shuffle(individuals)
N = len(individuals)

# A vector of numbers of birds that will be used for sampling 
K = np.linspace(5,N,num=10,endpoint=True)
k = len(K)

ns = 100 # Number of times to sample

# This is the output/results matrix.
# The number of rows is the number of different sample sizes
# The number of columns is the number of times we simulate a given sample size
output = np.zeros((k,ns))
for i in range(k):
    for j in range(ns):
        rows = random.sample(individuals, int(K[i]))
        output[i,j] = len(set(rows))

means = []
for samples in output:
    means.append(np.mean(samples))

plt.scatter(K, means, c="orange")

# FITTING THE CURVE 
def f(x,a,k):
    return 32*(1 - a*np.exp(-x/k))

X = np.linspace(K[0], K[-1] + 1, num = 500)
popt,pcov = curve_fit(f, K, means, maxfev= 100)
Y = f(X, *popt)
plt.plot(X,Y) 
plt.title("Species Abbundance Plot")
plt.xlabel("Samples")
plt.ylabel("Unique Individuals")
plt.show()
# plt.savefig("Bird_species_abundance_curve.png")
import pandas as pd 
from matplotlib import pyplot as plt

df = pd.read_csv("modified_df.csv") # We will only read first 10000 values

df =df.sort_values(by=['counts'],ascending = False)
print(df.head())

X = df['mnem']
Y = df['counts']
plt.figure(figsize=(20,10))
plt.title("Species Abundance")
plt.xlabel("Species")
plt.ylabel("counts")
plt.xticks([i for i in range(len(X))], X, rotation="vertical")
plt.bar(X,Y)
plt.show()
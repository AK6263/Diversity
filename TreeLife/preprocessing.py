import pandas as pd 
from matplotlib import pyplot as plt

df = pd.read_csv("Trees.csv", nrows=10000) # We will only read first 10000 values
cols = ['Unnamed: 0', 'tag', 'mnem', 'gx', 'gy']

mnem = df['mnem'].unique().tolist()
k = []
for i in mnem:
    k.append((df['mnem'] == i).sum())
# print(k)

newdf = pd.DataFrame()
newdf['mnem'] = mnem
newdf['counts'] = k
newdf =newdf.sort_values(by=['counts'],ascending = False)

newdf.to_csv("modified_df.csv")
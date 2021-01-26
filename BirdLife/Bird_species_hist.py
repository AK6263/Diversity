import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("bird_diversity_data.csv")
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
name = df["Name"].to_list()
no = df["No"].to_list()
plt.bar(name, no)
plt.ylabel('Number')
plt.title('Species Abundance')
plt.xticks(name, rotation="vertical")
plt.subplots_adjust(bottom=0.6)
plt.show()
# plt.savefig("Bird_species_hist.png")
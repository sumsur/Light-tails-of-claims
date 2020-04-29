# ANALYSIS OF TAIL OF DISTRIBUTION IN PYTHON

import pandas as pd 
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
asd = pd.read_excel(r'C:\Users\asd.xlsx', sheet_name='Sheet1')
asdd = pd.DataFrame(asd, columns= ['Mesec','Broj zahteva poslednjeg dana u mesecu'])

fig = plt.figure()
fig.subplots_adjust(top=0.8)
ax1 = fig.add_subplot(211)
ax1.set_ylabel('claims')
ax1.set_title('Insurance company - received claims over 2007-2017')

line= ax1.plot(asdd)

# Fixing random state for reproducibility
np.random.seed(19680801)

ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
n, bins, patches = ax2.hist(np.random.randn(1000), 50)
ax2.set_xlabel('January  February   March   April   May   June   July   August   September   October   November   December')

plt.show()

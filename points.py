import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import copy


a = []
b = []
total_a = []
total_b = []
csv=pd.read_csv("color.csv",header=None).values
count = 1
for index,(num , x , y) in enumerate(csv):
    
    #for i in range(int(num)):
        #a = []
        #b = []
        if num == count :
            a.append(x)
            b.append(y)
        
        else:
            count += 1
            total_a.append(a)
            total_b.append(b)
            a = []
            b = []
        #total_a.append(a)
        #total_b.append(b)
#cmap = get_cmap(len(total_a))
for j in range(len(total_a)):
    x = total_a[:][j]
    y = total_b[:][j]
    plt.plot(x,y, '-' , markersize=2)
    #scatter()
plt.show()
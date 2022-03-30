import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import copy
from collections import Counter
import matplotlib.cm as cm

a = []
b = []
c = []
d = []
total_a = []
total_b = []
total_c = []

number = 1
i = 0
# aa = []
# csv1=pd.read_csv("./1~43s/1s.csv",header = None).values
csv1 = pd.read_csv("ssC.csv", header=None).values
# print(csv1)
for index, (num, x, y) in enumerate(csv1):  # 把每筆資料的編號按順序放進total_c
    total_c.append(num)
result = Counter((total_c))
result1 = sorted(result)  # 按照編號順序排序

for index, (num, x, y) in enumerate(csv1):  # 針對每個編號去取得對應資料
    # for i in range(len(result1)):
    if num == result1[i]:               #Please Sort the data by ID from small to big, then round x after flout point to 2
        if num == result1[len(result1) - 1]:  # 做最後一個編號的資料
            c.append(x)
            d.append(y)

        else:
            a.append(x)
            b.append(y)

    # c.append(num)

    else:
        i += 1
        total_a.append(a)
        total_b.append(b)
        a = []
        b = []

        a.append(x)
        b.append(y)
    # total_c.append(c)
total_a.append(c)
total_b.append(d)
# c = []
# print(total_c)
# total_c_plus = copy.copy(total_c)
# result = Counter((total_c_plus))
# result1 = sorted(result)
# print(total_c.index(45))
for j in range(len(total_a)):
    x = total_a[:][j]
    y = total_b[:][j]
    # z = total_c[:][j]
    plt.xlim(-20, 50)
    plt.ylim(-10, 2000)
    plt.plot(x, y, '-', markersize=4)
    # for i in range(len(result1)):
plt.legend(result1)

# plt.title('1s')
# plt.savefig('1s.jpg')
plt.show()
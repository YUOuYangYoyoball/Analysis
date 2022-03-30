import csv
import matplotlib.pyplot as plt
import math
import pandas as pd
import datetime
import random
import numpy as np
#設置Error級別通知
plt.set_loglevel('ERROR')
Route_x = []
Route_y = []
ID_T = []
RGB=[]
ToR=[]
Color = []
#plt.close()
#呼叫Csv檔取出相關資訊
with open('ss.csv', newline='') as csvFile:
    rows = csv.reader(csvFile, delimiter=',')
    ID = [row[0] for row in rows]
    print(len(ID))
with open('ss.csv', newline='') as csvFile:
    rows = csv.reader(csvFile, delimiter=',')
    distance = [row[1] for row in rows]

with open('ss.csv', newline='') as csvFile:
    rows = csv.reader(csvFile, delimiter=',')
    Angle = [row[2] for row in rows]
    #print(Angle)
    #print(len(Angle))
with open('ss.csv', newline='') as csvFile:
    rows = csv.reader(csvFile, delimiter=',')
    frame = [row[3] for row in rows]
    #print(Angle)
#顏色定義
def get_cmap(n, name='hsv'):
    return plt.cm.get_cmap(name, n)

def search_ID():
    Target = input()
    print(Target)

def main():
    #search_ID()
    for i in range(len(ID)):
        direction = float(Angle[i]) / 1920 * 360
        #direction = float(Angle[i]) / 1920 * 180
        # print(direction)
        x = 10 + (float(distance[i]) * math.cos(math.radians(direction)))
        y = 10 + (float(distance[i]) * math.sin(math.radians(direction)))
        #print(x,y,x1,y1)
        h = ID[i]
        Route_x.insert(1, x)
        Route_y.insert(1, y)
        ID_T.insert(1, h)
        ToR.insert(1,str(ID[i])+','+str(x)+','+str(y)+','+str(frame[i]))
        DF = pd.DataFrame(ToR)
        DF.to_csv('2.csv',index=False)
        c = [int(ID[i]) / int(len(ID)), int(ID[i]) / int(len(ID)), int(ID[i]) / int(len(ID)), 1]
        Color.insert(1,c)
    plt.rcParams["figure.figsize"] = (10, 10)
    p1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    p2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    plt.figure('Draw')
    plt.plot(p1, p2, 'wo')
    plt.plot(10, 10, 'ko')
    plt.plot(Route_x, Route_y, '.',c=Color[i])
    plt.show()  # 顯示繪圖
    # 每15秒輸出一個影片
    # if t>1:
    # plt.plot([Route_x[t],Route_x[t-2]],[Route_y[t],Route_y[t-2]],color='r')
    # plt.plot(Route_x,Route_y, c = color)

    # 目標：分析更多時段路徑
if __name__=='__main__':
    main()
import pandas as pd
import math
import numpy as np
import csv
import matplotlib.pyplot as plt
from pynput.keyboard import Key, Listener, Controller
import keyboard
keyboard1 = Controller()
Route_x = []
Route_y = []
Export = []
def Search_ID(a):
    df = pd.read_csv('Dadaochen_Temple.csv', header=None)
    df.columns = ["ID", "Distance", "Angle", "Frame"]
    print(df)
    #print(df["ID"] == a)
    Route = (df["ID"]==a)
    D=df["Distance"][Route].tolist()
    A=df["Angle"][Route].tolist()
    F=df["Frame"][Route].tolist()
    print(A)
    print(len(D))
    #10ec 7367
    for i in range(len(D)):
        direction = float(A[i]) / 1920 * 360
        x = 10 + (float(D[i]) * -math.sin(math.radians(direction)))
        y = 10 + (float(D[i]) * math.cos(math.radians(direction)))
        Route_x.insert(1, x)
        Route_y.insert(1, y)
    plt.rcParams["figure.figsize"] = (10, 10)
    p1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    p2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    plt.figure('Draw')
    plt.plot(p1, p2, 'wo')
    plt.plot(10, 10, 'ko')
    plt.plot(Route_x, Route_y, '.')
    plt.show()  # 顯示繪圖
    #direction = float(A) / 1920 * 360
    #x = 10 + (float(D[Route]) * math.cos(math.radians(direction)))
    #print(x)
def ExportData():
    with open('bus1.csv', newline='') as csvFile:
        rows = csv.reader(csvFile, delimiter=',')
        ID = [row[0] for row in rows]
        print(len(ID))
    with open('bus1.csv', newline='') as csvFile:
        rows = csv.reader(csvFile, delimiter=',')
        distance = [row[1] for row in rows]
    with open('bus1.csv', newline='') as csvFile:
        rows = csv.reader(csvFile, delimiter=',')
        Angle = [row[2] for row in rows]
    with open('bus1.csv', newline='') as csvFile:
        rows = csv.reader(csvFile, delimiter=',')
        frame = [row[3] for row in rows]
    for i in range(len(ID)):
        direction = float(Angle[i]) / 1920 * 360
        x = 10 + (float(distance[i]) * math.cos(math.radians(direction)))
        y = 10 + (float(distance[i]) * math.sin(math.radians(direction)))
        Route_x.insert(1, x)
        Route_y.insert(1, y)
        Export.insert(1, str(ID[i]) + ',' + str(x) + ',' + str(y) + ',' + str(frame[i]))
        DF = pd.DataFrame(Export)
        DF.to_csv('Dadaochen_Temple_EX.csv', index=False)
    plt.show()  # 顯示繪圖
def main():
    #df = pd.read_csv('Roof.csv')
    #df.columns = ["ID", "Distance", "Angle", "Frame"]
    #print(df.head(10164))
    t = input("請輸入一個要查詢的ID:")
    Search_ID(int(t))
    #ExportData()
if __name__=='__main__':
    main()
#def on_press(key):
    #while keyboard.is_pressed('enter'):
        #print('{0} pressed'.format(key))
        #break
    #if key == Key.esc:
        #return False
#with Listener(on_press=on_press,draw_pos=draw_pos) as listener:
    #listener.join()
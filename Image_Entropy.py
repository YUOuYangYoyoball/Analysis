from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2
import math
def main():
    tmp = []
    for i in range(256):
        tmp.append(0)
    #print(tmp)
    val = 0
    k = 0
    res = 0
    image = cv2.imread('s1.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Entropy',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    img = np.array(image)
    #print(len(img))
    for i in range(len(img)):
        for j in range(len(img[i])):
            val = img[i][j]
            tmp[val] = float(tmp[val] + 1) #像素灰度級
            k = float(k + 1)
        # i = width , j = height
    for i in range(len(tmp)):
        tmp[i] = float(tmp[i] / k)
        #每一個像素點的機率
    for i in range(len(tmp)):
        if (tmp[i] == 0):
            res = res
        else:
            res = float(res - tmp[i] * (math.log(tmp[i]) / math.log(2.0)))
    print(res)

if __name__=='__main__':
    main()

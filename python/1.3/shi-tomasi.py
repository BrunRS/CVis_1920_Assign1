import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def shi_tomasi(img_dir):  
    img = cv.imread(img_dir)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    corners = cv.goodFeaturesToTrack(gray,25,0.01,10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv.circle(img,(x,y),3,(0,0,255),-1)

    plt.figure("Shi-tomasi detector")
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title("Shi-tomasi")
    plt.xticks([]), plt.yticks([])
    plt.savefig('Shi-Tomasi', bbox_inches='tight')
    plt.show()

    # cv.imwrite('shi-tomasi.png',img)
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def fast(img_dir):
    img = cv.imread(img_dir)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    fast = cv.FastFeatureDetector_create()
    
    keypoints = fast.detect(gray,None)
    img2 = cv.drawKeypoints(img, keypoints, None, color=(0,0,255))

    plt.figure("FAST detector")
    plt.imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB)), plt.title("FAST")
    plt.xticks([]), plt.yticks([])
    plt.savefig('FAST', bbox_inches='tight')
    plt.show()

    # cv.imwrite('fast.png',img2)
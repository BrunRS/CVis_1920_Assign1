import cv2
import numpy as np
from matplotlib import pyplot as plt

def prewitt(img_dir):
    img = cv2.imread(img_dir)    # Carrega a imagem
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

    kernelx = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    kernely = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
    
    prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
    prewitty = cv2.filter2D(img_gaussian, -1, kernely)

    prewitt = prewittx + prewitty
    
    plt.figure("Prewitt operator")
    plt.subplot(141), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(142),plt.imshow(cv2.cvtColor(prewittx, cv2.COLOR_BGR2RGB)), plt.title('Prewitt X')
    plt.xticks([]), plt.yticks([])
    plt.subplot(143),plt.imshow(cv2.cvtColor(prewitty, cv2.COLOR_BGR2RGB)), plt.title('Prewitt Y')
    plt.xticks([]), plt.yticks([])
    plt.subplot(144),plt.imshow(cv2.cvtColor(prewitt, cv2.COLOR_BGR2RGB)), plt.title('Prewitt')
    plt.xticks([]), plt.yticks([])
    plt.savefig('%s_image_prewitt'%(img_dir[5:11]), bbox_inches='tight')
    # plt.show()
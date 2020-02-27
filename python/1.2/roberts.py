import cv2
import numpy as np
from matplotlib import pyplot as plt

def roberts(img_dir):
    img = cv2.imread(img_dir)    # Carrega a imagem
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

    kernelx = np.array([[1,0],[0,-1]])
    kernely = np.array([[0,1],[-1,0]])
    robertsx = cv2.filter2D(img_gaussian, -1, kernelx)
    robertsy = cv2.filter2D(img_gaussian, -1, kernely)

    roberts = robertsx + robertsy

    plt.figure("Roberts operator")
    plt.subplot(141), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(142),plt.imshow(cv2.cvtColor(robertsx, cv2.COLOR_BGR2RGB)), plt.title('Roberts X')
    plt.xticks([]), plt.yticks([])
    plt.subplot(143),plt.imshow(cv2.cvtColor(robertsy, cv2.COLOR_BGR2RGB)), plt.title('Roberts Y')
    plt.xticks([]), plt.yticks([])
    plt.subplot(144),plt.imshow(cv2.cvtColor(roberts, cv2.COLOR_BGR2RGB)), plt.title('Roberts')
    plt.xticks([]), plt.yticks([])
    plt.savefig('%s_image_roberts'%(img_dir[5:11]), bbox_inches='tight')
    # plt.show()

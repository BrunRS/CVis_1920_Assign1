import cv2
import numpy as np
from matplotlib import pyplot as plt

def sobel(img_dir,s_ksize):
    #TODO: Meter cores como deve ser
    img = cv2.imread(img_dir)    # Carrega a imagem
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

    sobelx = cv2.Sobel(img_gaussian, cv2.CV_64F, 1, 0, s_ksize)  # Horizontal
    sobely = cv2.Sobel(img_gaussian, cv2.CV_64F, 0, 1, s_ksize)  # Vertical

    sobel = np.sqrt(sobelx**2 + sobely**2)

    plt.figure("Sobel operator")
    plt.subplot(141), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(142),plt.imshow(sobelx, cmap = 'gray'), plt.title('Sobel X')
    plt.xticks([]), plt.yticks([])
    plt.subplot(143),plt.imshow(sobely, cmap = 'gray'), plt.title('Sobel Y')
    plt.xticks([]), plt.yticks([])
    plt.subplot(144),plt.imshow(sobel, cmap = 'gray'), plt.title('Sobel')
    plt.xticks([]), plt.yticks([])
    plt.savefig('%s_image_sobel_ksize-%s'%(img_dir[5:11],s_ksize), bbox_inches='tight')
    
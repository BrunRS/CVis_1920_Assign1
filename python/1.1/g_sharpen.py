import cv2
import numpy as np
from matplotlib import pyplot as plt

def g_sharpen(img_dir,g_ksize,g_sigma):
    img = cv2.imread(img_dir)    # Carrega a imagem
    img_gaussian = cv2.GaussianBlur(img,(g_ksize,g_ksize),g_sigma)
    matrix = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    sharpen = cv2.filter2D(img_gaussian, -1, matrix)
    
    plt.figure('Gausian sharpen filter')
    plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Image with noise')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(cv2.cvtColor(sharpen, cv2.COLOR_BGR2RGB)), plt.title('Gausian sharpen')
    plt.xticks([]), plt.yticks([])
    plt.savefig('%s_sharpen_ksize-%s_sigma-%s'%(img_dir[5:10],g_ksize,g_sigma), bbox_inches='tight')
    plt.show()
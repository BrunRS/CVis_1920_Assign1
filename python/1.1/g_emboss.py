import cv2
import numpy as np
from matplotlib import pyplot as plt

def g_emboss(img_dir,g_ksize,g_sigma):
    img = cv2.imread(img_dir)    # Carrega a imagem
    img_gaussian = cv2.GaussianBlur(img,(g_ksize,g_ksize),g_sigma)
    matrix = np.array([[-2,-1,0],[-1,1,1],[0,1,2]])
    emboss = cv2.filter2D(img_gaussian, -1, matrix)
    
    plt.figure('Gausian emboss filter')
    plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Image with noise')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(cv2.cvtColor(emboss, cv2.COLOR_BGR2RGB)), plt.title('Gausian emboss')
    plt.xticks([]), plt.yticks([])
    plt.savefig('%s_emboss_ksize-%s_sigma-%s'%(img_dir[5:10],g_ksize,g_sigma), bbox_inches='tight')
    plt.show()
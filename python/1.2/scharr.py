import cv2
import numpy as np
from matplotlib import pyplot as plt

def scharr(img_dir):
    img = cv2.imread(img_dir)    # Carrega a imagem
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
    scharrx = cv2.Scharr(img_gaussian, cv2.CV_64F, 1, 0)
    scharry = cv2.Scharr(img_gaussian, cv2.CV_64F, 0, 1)

    scharr = np.sqrt(scharrx**2 + scharry**2)

    plt.figure("Scharr operator")
    plt.subplot(141), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(142),plt.imshow(scharrx, cmap = 'gray'), plt.title('Scharr X')
    plt.xticks([]), plt.yticks([])
    plt.subplot(143),plt.imshow(scharry, cmap = 'gray'), plt.title('Scharr Y')
    plt.xticks([]), plt.yticks([])
    plt.subplot(144),plt.imshow(scharr, cmap = 'gray'), plt.title('Scharr')
    plt.xticks([]), plt.yticks([])
    plt.savefig('%s_image_scharr'%(img_dir[5:11]), bbox_inches='tight')
    # plt.show()

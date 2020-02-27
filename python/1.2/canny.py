import cv2
import numpy as np
from matplotlib import pyplot as plt

def canny(img_dir,threshold1,threshold2):
    img = cv2.imread(img_dir)    # Carrega a imagem
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
    img_canny = cv2.Canny(img_gaussian,threshold1,threshold2)

    plt.figure("Canny operator")
    plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(cv2.cvtColor(img_canny, cv2.COLOR_BGR2RGB)), plt.title('Canny')
    plt.xticks([]), plt.yticks([])
    plt.savefig('%s_image_canny'%(img_dir[5:11]), bbox_inches='tight')
    # plt.show()
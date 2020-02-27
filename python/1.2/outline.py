import cv2
import numpy as np
from matplotlib import pyplot as plt

def outline(img_dir):
    img = cv2.imread(img_dir)    # Carrega a imagem
    matrix = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    outline = cv2.filter2D(img, -1, matrix)
    
    plt.figure('Outline extractor')
    plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(cv2.cvtColor(outline, cv2.COLOR_BGR2RGB)), plt.title('Outline extractor')
    plt.xticks([]), plt.yticks([])
    plt.savefig('%s_image_outline'%(img_dir[5:11]), bbox_inches='tight')
    plt.show()
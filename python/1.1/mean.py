import cv2
import numpy as np
from matplotlib import pyplot as plt

def mean_filter(img_dir,n_mean):
    img = cv2.imread(img_dir)
    # kernel = np.ones((n_mean,n_mean),np.float32)/n_mean**2
    # mean = cv2.filter2D(img,-1,kernel)
    mean = cv2.blur(img,(n_mean,n_mean))
    return mean
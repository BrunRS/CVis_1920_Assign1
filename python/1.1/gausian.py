import cv2
import numpy as np
from matplotlib import pyplot as plt

def gausian_filter(img_dir,n_gausian,sigma):
    img = cv2.imread(img_dir)
    gausian = cv2.GaussianBlur(img,(n_gausian,n_gausian),sigma)
    return gausian
import cv2
import numpy as np
from matplotlib import pyplot as plt

def median_filter(img_dir,n_median):
    img = cv2.imread(img_dir)
    median = cv2.medianBlur(img,n_median)
    return median
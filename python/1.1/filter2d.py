import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def filter_2d(img_dir):
    img = cv.imread(img_dir)

    kernel_row_column = int(input("How many rows/column you want for the filter?\n(Only one number since filter its a square matrix)"))

    kernel_values = [input("Input a list of values separated by commas for the matrix.").split(",")]

    divide_question = input("Want to divide the matrix by a number?(Y/N)")

    #Dividir com um valor que a media do filtro seja 1
    if(divide_question=="y" or divide_question=="Y"):
        divide_kernel = int(input("Divide by:"))
    else:
        divide_kernel = 1

    kernel_array=np.array(kernel_values,np.float32)

    kernel_matrix = kernel_array.reshape(kernel_row_column,kernel_row_column)

    kernel=np.divide(kernel_matrix,(divide_kernel))
    print(np.around(kernel,3))
    #TODO: MEter a gravar matriz com nome correto
    dst = cv.filter2D(img,-1,kernel)

    plt.figure('My own 2d filter')
    plt.suptitle('My own 2d filter', fontsize=18)
    plt.subplot(131),plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)),plt.title('Image with noise')
    plt.xticks([]), plt.yticks([])
    plt.subplot(132, frameon=False),plt.xlabel('Matrix %sx%s'%(kernel_row_column,kernel_row_column))
    plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(cv.cvtColor(dst, cv.COLOR_BGR2RGB)),plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.gcf().text(0.5,0.5,np.around(kernel,2),bbox=dict(facecolor='white', alpha=0.5),va='center', ha='center',wrap=False)
    plt.savefig('%s_filter2d'%img_dir[5:10], bbox_inches='tight')
    plt.show()

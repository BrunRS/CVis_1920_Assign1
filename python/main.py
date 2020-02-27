import cv2
import numpy as np
import imp
from matplotlib import pyplot as plt
import os
# import sys


# Imports da pasta 1.1
mean_func = imp.load_source('mean','python/1.1/mean.py')
median_func = imp.load_source('median','python/1.1/median.py')
gausian_func = imp.load_source('gausian','python/1.1/gausian.py')
g_sharpen_func = imp.load_source('g_sharpen','python/1.1/g_sharpen.py')
g_emboss_func = imp.load_source('g_emboss','python/1.1/g_emboss.py')
filter_2d_func = imp.load_source('filter_2d','python/1.1/filter2d.py')

# Imports da pasta 1.2
sobel_func = imp.load_source('sobel','python/1.2/sobel.py')
scharr_func = imp.load_source('scharr','python/1.2/scharr.py')
prewitt_func = imp.load_source('prewitt','python/1.2/prewitt.py')
roberts_func = imp.load_source('roberts','python/1.2/roberts.py')
canny_func = imp.load_source('canny','python/1.2/canny.py')
outline_func = imp.load_source('outline','python/1.2/outline.py')

# Imports da pasta 1.3
harris_func = imp.load_source('harris','python/1.3/harris.py')
shi_tomasi_func = imp.load_source('shitomasi','python/1.3/shi-tomasi.py')
fast_func = imp.load_source('fast','python/1.3/fast.py')
my_harris_func = imp.load_source('my_harris','extra_credits/1.3/my_harris.py')


#TODO: UM ficheiro que pergunte se quero guardar para chamar dentro dos imports

def main():
    clear_screen()

    choice = '0'
    while choice == '0':
        print("Select one option:\n")

        print("1 - Noise removal")
        print("2 - Edge extraction")
        print("3 - Corner detection")
        print("4 - Exit\n")

        choice = input("Please make a choice: ")

        if choice == "1":
            print("NOISE REMOVAL")
            menu_noise()

        elif choice == "2":
            print("EDGE EXTRACTION")
            menu_edge()

        elif choice == "3":
            print("CORNER DETECTION")
            menu_corner()

        elif choice == "4":
            print("See you later!")
            quit()

        else:
            print("I don't understand your choice.")


def menu_noise():
    #   Exercicio 1.1
    clear_screen()
    
    choice = '0'
    while choice == '0':
        print("NOISE REMOVAL\n")

        print("1 - Classic filters")
        print("2 - Other filters")
        print("3 - Go back")
        print("4 - Exit\n")

        choice = input("Please make a choice: ")

        if choice == "1":
            menu_classic_filters()
            main()

        elif choice == "2":
            print("--- Other filters ---")
            menu_noise_2()
            main()

        elif choice == "3":
            #   Go back
            main()

        elif choice == "4":
            print("See you later!")
            quit()

        else:
            print("I don't understand your choice.")


def menu_noise_2():
    #   NOISE REMOVAL - OTHER FILTERS
    clear_screen()  #clean screen
    
    choice = '0'
    while choice == '0':
        print("OTHER FILTERS\n")

        print("1 - Gausian sharpen filter")
        print("2 - Gausian emboss filter")
        print("3 - Custom filter")
        print("4 - Go back\n")

        choice = input("Please make a choice: ")

        if choice == "1":
            #   Gaussian sharpen filter
            print("---Gaussian sharpen filters---")
            img_dir = menu_image()  # Adquire o diretorio da imagem pretendida
            g_ksize = int(input("Please insert the size of the gaussian filter: "))
            g_sigma = int(input("Please insert the sigma of the gaussian filter: "))
            g_sharpen_func.g_sharpen(img_dir,g_ksize,g_sigma)

        elif choice == "2":
            #   Gaussian emboss filter
            print("---Gaussian emboss filter---")
            img_dir = menu_image()  # Adquire o diretorio da imagem pretendida
            g_ksize = int(input("Please insert the size of the gaussian filter: "))
            g_sigma = int(input("Please insert the sigma of the gaussian filter: "))
            g_emboss_func.g_emboss(img_dir,g_ksize,g_sigma)

        elif choice == "3":
            #   Custom filter
            print("---Custom filter---")
            img_dir = menu_image()  # Adquire o diretorio da imagem pretendida
            filter_2d_func.filter_2d(img_dir)

        elif choice == "4":
            #   Go back
            menu_noise()

        else:
            print("I don't understand your choice.")

    

def menu_edge():
    #   Exercicio 1.2
    clear_screen()    

    choice = '0'
    while choice == '0':
        print("EDGE EXTRACTION\n")

        print("1 - Classic operators")
        print("2 - Outline operator")
        print("3 - Go back")
        print("4 - Exit\n")

        choice = input("Please make a choice: ")

        if choice == "1":
            img_dir = 'data/harris.jpg'  # Adquire o diretorio da imagem pretendida

            print("---Classic operators---")
            print("* Sobel operator configuration *")
            s_ksize = int(input("Please insert the size of sobel filter: "))
            print("* Canny operator configuration *")
            threshold1 = int(input("Please insert the low threshold of canny filter (100 is the recommended): "))
            threshold2 = int(input("Please insert the high threshold of canny filter (200 is the recommended): "))
            sobel_func.sobel(img_dir,s_ksize)
            scharr_func.scharr(img_dir)
            prewitt_func.prewitt(img_dir)
            roberts_func.roberts(img_dir)
            canny_func.canny(img_dir,threshold1,threshold2)
            plt.show()
            main()

        elif choice == "2":
            print("---Outline operator---")
            img_dir = 'data/harris.jpg' # Adquire o diretorio da imagem pretendida
            outline_func.outline(img_dir)
            main()

        elif choice == "3":
            #   Go back
            main()
    

        elif choice == "4":
            print("See you later!")
            quit()

        else:
            print("I don't understand your choice.")



def menu_corner():
    #   Exercicio 1.3
    clear_screen()
    
    choice = '0'

    while choice == '0':
        print("CORNER DETECTION\n")

        print("1 - Harris detector")
        print("2 - Shi-tomasi detector")
        print("3 - FAST detector")
        print("4 - Our own Harris detector")
        print("5 - Go back")
        print("6 - Exit\n")

        choice = input("Please make a choice: ")

        if choice == "1":
            print("--- Harris detector ---")
            img_dir=menu_image2()
            harris_func.harris(img_dir)
            main()

        elif choice == "2":
            print("--- Shi-tomasi detectors ---")
            img_dir=menu_image2()
            shi_tomasi_func.shi_tomasi(img_dir)
            main()

        elif choice == "3":
            print("--- FAST detectors ---")
            img_dir=menu_image2()
            fast_func.fast(img_dir)
            main()

        elif choice == "4":
            # Exercicio 3
            print("--- Our own Harris detector ---")
            img_dir=menu_image2()
            threshold = float(input("Please insert a threshold (0 to 1): "))
            r_circle = int(input("Please insert a radius for the marks: "))
            print("\n1 - Red")
            print("2 - Green")
            print("3 - Blue")
            marks_color = int(input("Color for the marks: "))
            my_harris_func.my_harris(img_dir,5,0.04,threshold,r_circle,marks_color )
            main()

        elif choice == "5":
            #   Go back
            main()

        elif choice == "6":
            print("See you later!")
            quit()

        else:
            print("I don't understand your choice.")

def menu_image2():
    ### Função que devolve uma string com o diretorio da imagem escolhida para os corners   ###
    
    choice_img = '0'
    
    print("1 - Harris image")
    print("2 - Our image")
    choise_img = int(input('Select one image:'))
    if choise_img==1:
        imgdir = 'data/harris.jpg'
    elif choise_img==2:
        imgdir = 'extra_credits/harris2.jpg'
    print("Loading image...")
    
    return imgdir

def menu_image():
    ### Função que devolve uma string com o diretorio da imagem escolhida ###
    show_images()
    choice = '0'
    choice = input("Select one image from 1 to 13: ")

    try:
        if (int(choice)>0 and int(choice)<10):
            choice = '0%s' %(choice)
        elif (int(choice)>=10 and int(choice)<14):
            pass
    except ValueError:
        print("Enter numbers only")


    imgdir = 'data/img%s_noise.jpg'%(choice)
    print("Loading image...")
    
    return imgdir

def show_images():
    plt.figure('Choose an image')
    plt.suptitle('Choose an image', fontsize=16)
    for item in range(13):
        if (item+1<10):
            choice = '0%s' %(item+1)
            img = cv2.imread('data/img%s.jpg'%(choice))

            plt.subplot(3,5,item+1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('img%s'%(choice))
            plt.xticks([]), plt.yticks([])
        else:
            img = cv2.imread('data/img%s.jpg'%(item+1))
            plt.subplot(3,5,item+1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('img%s'%(item+1))
            plt.xticks([]), plt.yticks([])
    plt.show()

def menu_classic_filters():
    #   NOISE REMOVAL - OTHER FILTERS
    clear_screen()  #clean screen
    
    choice = '0'
    while choice == '0':
        print("Chose how many kernels you want to see\n")

        print("1 - Multiples Kernels")
        print("2 - Single Kernel")
        print("3 - Go back\n")

        choice = input("Please make a choice: ")

        if choice == "1":
            #   Multiple Kernels on window
            multiple_kernels_classic()

        elif choice == "2":
            #   Single Kernel on window
            single_kernel_classic()

        elif choice == "3":
            #   Go back
            menu_noise()

        else:
            print("I don't understand your choice.")

def single_kernel_classic():
    print("--- Classic filters ---")

    img_dir = menu_image()  # Adquire o diretorio da imagem pretendida

    # Numero de linhas ou colunas (matriz quadrada) dos filtros
    print("* Mean filter configuration *")
    n_mean = int(input("Please select the number of lines of mean filter: "))
    print("* Median filter configuration *")
    n_median = int(input("Please select the number of lines of median filter: "))
    print("* Gaussian filter configuration *")
    n_gausian = int(input("Please select the number of lines of gaussian filter: "))
    sigma = int(input("Please insert sigma value for gaussian filter: "))

    # Imagens filtradas
    mean = mean_func.mean_filter(img_dir,n_mean)  # Filtra a imagem com mean filter
    median = median_func.median_filter(img_dir,n_median)    # Filtra a imagem com median filter
    gausian = gausian_func.gausian_filter(img_dir,n_gausian,sigma) # Filtra a imagem com gausian filter
            
    org_img = cv2.imread('%s.jpg'%(img_dir[:10]))  # Imagem sem ruido
    noise_img = cv2.imread(img_dir)      # Imagem com ruido 

    # Plot dos graficos
    plt.figure("Mean:%s, Median:%s, Gausian:%s"%(n_mean,n_median,n_gausian))
    # plt.gcf().set_size_inches(8.5, 7)
    plt.gcf().set_size_inches(12, 8)
    plt.suptitle("Classic Filter", fontsize=20)
    plt.subplot(231), plt.imshow(cv2.cvtColor(org_img, cv2.COLOR_BGR2RGB)), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(233), plt.imshow(cv2.cvtColor(noise_img, cv2.COLOR_BGR2RGB)), plt.title('With noise')
    plt.xticks([]), plt.yticks([])
    plt.subplot(234), plt.imshow(cv2.cvtColor(mean, cv2.COLOR_BGR2RGB)), plt.title('Mean Filter'), plt.xlabel("Mean:%s"%(n_mean))
    plt.xticks([]), plt.yticks([])
    plt.subplot(235), plt.imshow(cv2.cvtColor(median, cv2.COLOR_BGR2RGB)), plt.title('Median Filter'), plt.xlabel("Median:%s"%(n_median))
    plt.xticks([]), plt.yticks([])
    plt.subplot(236), plt.imshow(cv2.cvtColor(gausian, cv2.COLOR_BGR2RGB)), plt.title('Gausian Filter'), plt.xlabel("Gausian:%s\nSigma:%s"%(n_gausian,sigma))
    plt.xticks([]), plt.yticks([])
    plt.savefig('%s_mean-%s_median-%s_gausian-%s.png'%(img_dir[5:10],n_mean,n_median,n_gausian), bbox_inches='tight')
    plt.show()

def multiple_kernels_classic():
    
    # img_dir = 'data/img06_noise.jpg'
    img_dir = menu_image()  # Adquire o diretorio da imagem pretendida

    lengthOfKernels = 9
    n_kernel = 1
    sigma = 0

    mean_array = ["Mean_Multiple_Kernel"]
    median_array = ["Median_Multiple_Kernel"]
    gaussian_array = ["Gaussian_Multiple_Kernel"]

    for indexK in range(1, lengthOfKernels):
        n_kernel = n_kernel + 2

        # Imagens filtradas
        mean_array.append(mean_func.mean_filter(img_dir, int(n_kernel)))  # Filtra a imagem com mean filter
        median_array.append(median_func.median_filter(img_dir, int(n_kernel)))    # Filtra a imagem com median filter
        gaussian_array.append(gausian_func.gausian_filter(img_dir, int(n_kernel),sigma)) # Filtra a imagem com gausian filter


    x_plot = 4
    y_plot = 2
    n_kernel = 1
    for indexFig in range(1, lengthOfKernels):
        n_kernel = n_kernel + 2
        plt.figure(mean_array[0])
        plt.gcf().set_size_inches(12, 6)
        plt.suptitle("Classic Filter - Mean Filter", fontsize=16)
        plt.subplot(y_plot,x_plot,indexFig), plt.imshow(cv2.cvtColor(mean_array[indexFig], cv2.COLOR_BGR2RGB)), plt.xlabel("Mean:%s"%(n_kernel))
        plt.xticks([]), plt.yticks([])
    plt.savefig('%s_mean-multiples.png'%(img_dir[5:10]), bbox_inches='tight')
    n_kernel = 1
    for indexFig in range(1, lengthOfKernels):
        n_kernel = n_kernel + 2
        plt.figure(median_array[0])
        plt.gcf().set_size_inches(12, 6)
        plt.suptitle("Classic Filter - Median Filter", fontsize=16)
        plt.subplot(y_plot,x_plot,indexFig), plt.imshow(cv2.cvtColor(median_array[indexFig], cv2.COLOR_BGR2RGB)), plt.xlabel("Median:%s"%(n_kernel))
        plt.xticks([]), plt.yticks([])
    plt.savefig('%s_median-multiples.png'%(img_dir[5:10]), bbox_inches='tight')
    n_kernel = 1
    for indexFig in range(1, lengthOfKernels):
        n_kernel = n_kernel + 2
        plt.figure(gaussian_array[0])
        plt.gcf().set_size_inches(12, 6)
        plt.suptitle("Classic Filter - Gaussian Filter", fontsize=16)
        plt.subplot(y_plot,x_plot,indexFig), plt.imshow(cv2.cvtColor(gaussian_array[indexFig], cv2.COLOR_BGR2RGB)), plt.xlabel("Gausian:%s\nSigma:%s"%(n_kernel,sigma))
        plt.xticks([]), plt.yticks([])
    plt.savefig('%s_gaussian-multiples.png'%(img_dir[5:10]), bbox_inches='tight')
    plt.show()


def clear_screen():
    # print(chr(27) + "[2J")
    os.system('cls' if os.name == 'nt' else 'clear')

main()
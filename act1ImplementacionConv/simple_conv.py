"""
By Abhisek Jana
code taken from https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection
blog http://www.adeveloperdiary.com/data-science/computer-vision/how-to-implement-sobel-edge-detection-using-python-from-scratch/

Modified by Benjamin Valdes
Documentación por: Sebastián Blanchet Sánchez A00227588
"""

#Se importan las librerias
import numpy as np #matrices
import cv2 #imagenes 
import matplotlib.pyplot as plt #graficación
 

def conv_helper(fragment, kernel):
    """ multiplica 2 matices y devuelve su suma"""
    
    f_row, f_col = fragment.shape #fragmento de la imagen
    k_row, k_col = kernel.shape #kernel
    result = 0.0
    #se realiza la suma de las dos matrices
    for row in range(f_row): 
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result

def convolution(image, kernel):
    """Aplica una convolucion sin padding (valida) de una dimesion 
    y devuelve la matriz resultante de la operación
    """

    image_row, image_col = image.shape #asigna alto y ancho de la imagen 
    kernel_row, kernel_col = kernel.shape #asigna alto y ancho del filtro
   
    output = np.zeros(image.shape) #matriz donde guardo el resultado
    
   #Se desarrolla la matriz de salida (output) y se aplica la función anterior 
    for row in range(image_row):
        for col in range(image_col):
                output[row, col] = conv_helper(
                                    image[row:row + kernel_row, 
                                    col:col + kernel_col],kernel)
             
    plt.imshow(output, cmap='gray') #gráfica el output con base en una escala de grises
    plt.title("Output Image using {}X{} Kernel".format(kernel_row, kernel_col)) #se asigna el titulo y formato
    plt.show() #Se muestra la gráfica

    return output #fin de la función

#Desarrollamos el kernel
kernelMatriz = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]])
#Desarrollamos la matriz imagen
matrizImagen = np.array([ [0,0,0,0,0,0,0],
                          [0,2,4,1,5,4,0],
                          [0,2,3,2,0,6,0],
                          [0,6,1,3,5,3,0],
                          [0,4,1,1,5,8,0],
                          [0,6,5,6,7,8,0],
                          [0,0,0,0,0,0,0]
    ])
#aplicamos la función en estos dos
convolution(matrizImagen, kernelMatriz)
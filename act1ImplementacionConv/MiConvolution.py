"""Sebastián Blanchet Sánchez A00227588 
"""
#Se importan las librerias
import numpy as np
import cv2
import matplotlib.pyplot as plt
 
#Función de convolución
def convolution(img, kernel):
    
    h_img, w_img = img.shape 
    h_ker, w_ker = kernel.shape

    #Matriz de ceros donde se guarda el resultado
    resultado = np.zeros((h_img-h_ker+1,w_img-w_ker+1))
    
    #Se recorre cada posición aplicando el kernel sobre ella
    for i in range(resultado.shape[0]):
        for j in range(resultado.shape[1]):
            sumador = 0
            for x in range(h_ker):
                for y in range(w_ker):
                    sumador += img[i+x, j+y]*kernel[h_ker-1-x, w_ker-1-y]
            resultado[i, j] = sumador
    
    #Mostrar imagen resultado
    plt.imshow(resultado, cmap='gray')
    plt.title("Utilización del kernel")
    plt.show()
    
    #regresa la imagen final
    return resultado
 
#Ubicación de la imagén
ruta = r'C:\\Users\\sebas\\Downloads\\entrgasIndividuales\\Semana6_Individual\\act1ImplementacionConv\\adachi.jpg'

#kernel
kernel = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)

imagenFinal = convolution(img, kernel)



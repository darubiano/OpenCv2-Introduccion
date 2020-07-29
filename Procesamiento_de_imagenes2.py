# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:33:13 2020

@author: darub
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

# leer una imagen binaria
imagen = cv2.imread('perro.jpg', 0)
plt.imshow(imagen, cmap='gray')

# los valores menores de 255/2 seran blancos y valores de 255 seran negros
mitad, imagen = cv2.threshold(imagen, 255/2, 255, cv2.THRESH_BINARY)
plt.imshow(imagen, cmap='gray')
# proceso inverso
mitad, imagen = cv2.threshold(imagen, 255/2, 255, cv2.THRESH_BINARY_INV)
plt.imshow(imagen, cmap='gray')


# mostrar una imagen en varios tamaños
imagen_color =  cv2.imread('perro.jpg')
imagen_color = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2RGB)
plt.imshow(imagen_color)
print(imagen_color.shape)

figura = plt.figure(figsize=(10,10))
lienzo = figura.add_subplot(111)
lienzo.imshow(imagen_color)
print(imagen_color.shape)


# Gradientes y contornos de una imagen
sudoku = cv2.imread('sudoku.jpg',0)
plt.imshow(sudoku, cmap='gray')

# identificar contornos en el eje x
sobelx = cv2.Sobel(sudoku, cv2.CV_64F, dx=1, dy=0, ksize=5)
plt.imshow(sobelx, cmap='gray')
# identificar contornos en el eje y
sobely = cv2.Sobel(sudoku, cv2.CV_64F, dx=0, dy=1, ksize=5)
plt.imshow(sobely, cmap='gray')

# unir contornos X y Y
sudoku_contorno = cv2.addWeighted(src1=sobelx, alpha=0.5, src2=sobely, beta=0.5, gamma=0)
plt.imshow(sudoku_contorno, cmap='gray')

# contorno otro metodo mas corto
laplacian = cv2.Laplacian(sudoku, cv2.CV_64F)
plt.imshow(laplacian, cmap='gray')


## efectos de erosion y eliminacion de ruido
imagen_nueva = np.zeros((300,600))
fuente = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen_nueva, text='ABCDE', org=(50,200), fontFace=fuente,
            fontScale=5, color=(255,255,255), thickness=8)
plt.imshow(imagen_nueva, cmap='gray')

nucleo = np.ones((5,5), dtype=np.uint8)
# erosionar la imagen creada con valores de 1 negros
imagen_erosion = cv2.erode(imagen_nueva, nucleo, iterations=1)  
plt.imshow(imagen_erosion, cmap='gray')

## crear una imagen con ruido
ruido = np.random.randint(low=0,high=2,size=imagen_nueva.shape)
ruido = ruido *255
plt.imshow(ruido, cmap='gray')

# imagen con ruido
imagen_ruido = imagen_nueva + ruido
plt.imshow(imagen_ruido, cmap='gray')

# imagen sin el ruido
imagen_sin_ruido = cv2.morphologyEx(imagen_ruido, cv2.MORPH_OPEN, nucleo)
plt.imshow(imagen_sin_ruido, cmap='gray')

# rellenar las letras del nucleo de unos
gradiente = cv2.morphologyEx(imagen_nueva,cv2.MORPH_GRADIENT,nucleo)
plt.imshow(gradiente, cmap='gray')


### HISTOGRAMA DE COLORES DE UNA IMAGEN
imagen_color =  cv2.imread('perro.jpg')
imagen_color = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2RGB)
plt.imshow(imagen_color)
print(imagen_color.shape)
# Color [0] Rojo
histograma = cv2.calcHist([imagen_color],[0],None,[256],[0,256])
plt.plot(histograma)

# todos los colores
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([imagen_color],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
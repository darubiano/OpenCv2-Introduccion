# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:28:50 2020

@author: darub
"""

import matplotlib.pyplot as plt
import cv2

# Cargar imagen como arreglo
imagen = cv2.imread('perro.jpg', cv2.IMR)
print(imagen.shape)

# OpenCv toma los colores BGR(blue green red)
# Matplotlib toma los colres RGB(red green blue)
plt.imshow(imagen)

# Ajustar orden BGR a RGB para hacer la grafica
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
plt.imshow(imagen)

# leer imagen en escala de grises
imagen_blanco_negro = cv2.imread('perro.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(imagen_blanco_negro, cmap="gray")

# redimencionar la imagen toma el valor (ancho,alto)
imagen_resize = cv2.resize(imagen, (600,500))
plt.imshow(imagen_resize)
print(imagen_resize.shape)
# redimencionar el 50 % de la imagen
imagen_50 = cv2.resize(imagen, (imagen.shape[1]//2,imagen.shape[0]//2))
plt.imshow(imagen_50)
print(imagen_50.shape)

# Girar la imagen 0 vertical y 1 para horizontal
imagen_girada = cv2.flip(imagen_50,1)
plt.imshow(imagen_girada)
imagen_girada = cv2.flip(imagen_50,0)
plt.imshow(imagen_girada)

# guardar imagen
# ajustar el orden RGB a BGR para que se guarde bien
imagen_girada = cv2.cvtColor(imagen_girada, cv2.COLOR_RGB2BGR)
cv2.imwrite('perro_al_reves.jpg',imagen_girada)
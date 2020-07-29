# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:14:05 2020

@author: darub
"""

import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('perro.jpg')
# imagen en RGB
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
plt.imshow(imagen)

# imagen en HSV
imagen_hsv = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)
plt.imshow(imagen_hsv)

# imagen en HLS
imagen_hls = cv2.cvtColor(imagen, cv2.COLOR_BGR2HLS)
plt.imshow(imagen_hls)

#unir imagenes
imagen_marca = cv2.imread('marca-agua-redaitcurso.jpg')
imagen_marca = cv2.cvtColor(imagen_marca, cv2.COLOR_BGR2RGB)
plt.imshow(imagen_marca)

# tamaños
print(imagen.shape)
print(imagen_marca.shape)
# ajustar el tamaño de las imagenes
imagen = cv2.resize(imagen,(1200,1200))
imagen_marca = cv2.resize(imagen_marca,(1200,1200))

# unir imagenes alpha peso de la imagen
imagen_mezcla = cv2.addWeighted(src1=imagen, alpha=0.8,
                                src2=imagen_marca, beta=0.2, gamma=0)
plt.imshow(imagen_mezcla)

# unir imagenes con diferentes tamaños
imagen_nueva = cv2.imread('logo-redaitcursos.jpg')
imagen_nueva = cv2.cvtColor(imagen_nueva, cv2.COLOR_BGR2RGB)
plt.imshow(imagen_nueva)
print(imagen.shape)
print(imagen_nueva.shape)

imagen_nueva = cv2.resize(imagen_nueva, (1200,200))
plt.imshow(imagen_nueva)

parte_imagen = imagen[:200]
plt.imshow(parte_imagen)

# parte de arriba de la imagen
parte_imagen_mezcla = cv2.addWeighted(src1=parte_imagen, alpha=0.5,
                                      src2=imagen_nueva, beta=0.5, gamma=0)
plt.imshow(parte_imagen_mezcla)
# asignar parte de imagen a la original
imagen[:200] = parte_imagen_mezcla
plt.imshow(imagen)


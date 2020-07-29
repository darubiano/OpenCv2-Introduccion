# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:23:38 2020

@author: darub
"""

import matplotlib.pyplot as plt
import cv2

# imagen completa
imagen = cv2.imread('perro.jpg')
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
plt.imshow(imagen)
# imagen cara
cara = cv2.imread('cara.jpg')
cara = cv2.cvtColor(cara, cv2.COLOR_BGR2RGB)
plt.imshow(cara)

# Emparejamiento de imagenes
metodo = cv2.TM_CCOEFF
resultado = cv2.matchTemplate(imagen,cara,metodo)
# mapa de calor donde existe una coincidencia
plt.imshow(resultado)
# posisiones de la coincidencia
valor_min, valor_max, pos_min, pos_max= cv2.minMaxLoc(resultado)

# dimensiones de la cara
alto,ancho,colores = cara.shape

# dibujar el rectangulo en la imagen inicial
cv2.rectangle(imagen, pos_max,(pos_max[0]+ancho,pos_max[1]+alto),
              (255,0,0), 8)
plt.imshow(imagen)



























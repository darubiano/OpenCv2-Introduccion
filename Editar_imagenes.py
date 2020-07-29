# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:57:50 2020

@author: darub
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2

# crear imagen negra llena de 0s
imagen = np.zeros(shape=(500,500,3), dtype=np.int16)
print(imagen.shape)
# imagen negra
plt.imshow(imagen)

# dibujar en la imagen
# crear un rectangulo rojo, thickness grosor
cv2.rectangle(imagen,pt1=(20,20),pt2=(100,100), color=(255,0,0), thickness=10)
plt.imshow(imagen)

# crear un circulo verde
cv2.circle(imagen, center=(250,250), radius=100, color=(0,255,0), thickness=5)
plt.imshow(imagen)

# crear una recta azul
cv2.line(imagen, pt1=(0,400), pt2=(500,400), color=(0,0,255), thickness=5)
plt.imshow(imagen)

# escribir texto 
# crear imagen blanca llena de 255s
imagen_blanca = np.full((500,500,3),255)
print(imagen_blanca.shape)
plt.imshow(imagen_blanca)

# fuente del texto
fuente = cv2.FONT_HERSHEY_SIMPLEX
# poner texto org ubicacion
cv2.putText(imagen_blanca, text='Hola', org=(20,100), fontFace=fuente,
            fontScale=3, color=(0,255,0), thickness=4, lineType=cv2.LINE_8)
plt.imshow(imagen_blanca)

# crear un poligono
vertices = np.array([[100,300],[300,200],[400,400],[200,400]])
print(vertices.shape)
puntos = vertices.reshape(-1,1,2)
print(puntos.shape)
cv2.polylines(imagen_blanca, [puntos], isClosed=True, color=(0,0,0), thickness=5)
plt.imshow(imagen_blanca)
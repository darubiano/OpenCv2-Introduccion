# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:53:15 2020
https://github.com/opencv/opencv/tree/master/data/haarcascades
@author: darub
"""

import matplotlib.pyplot as plt
import cv2 

# leer imagen en escala de gris
rostro = cv2.imread('rostro1.png',0)
plt.imshow(rostro, cmap='gray')

familia = cv2.imread('familia.png',0)
plt.imshow(familia, cmap='gray')

# metodo de cascada
cascada_cara = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detectar_cara(imagen):
    # copiar para no modificar la imagen original
    imagen1 = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(imagen1)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1, (x,y), (x+w,y+h),(255,0,0),5)
    return imagen1

resultado = detectar_cara(rostro)
plt.imshow(resultado, cmap='gray')

resultado1 = detectar_cara(familia)
plt.imshow(resultado1, cmap='gray')


cascada_ojos = cv2.CascadeClassifier('haarcascade_eye.xml')

def detectar_ojos(imagen):
    # copiar para no modificar la imagen original
    imagen1 = imagen.copy()
    rectangulos = cascada_ojos.detectMultiScale(imagen1)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1, (x,y), (x+w,y+h),(255,0,0),5)
    return imagen1

resultado = detectar_ojos(rostro)
plt.imshow(resultado, cmap='gray')
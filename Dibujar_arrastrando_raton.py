# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:41:09 2020

@author: darub
"""

import numpy as np
import cv2

# variables globales
dibujando = False
valorx = 0
valory = 0

# Definimos nuestra funcion para dibujar
def dibujar(event,x,y,etiquetas,parametros):
    global dibujando,valorx,valory
    if event == cv2.EVENT_LBUTTONDOWN:
        dibujando = True
        valorx = x
        valory = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if dibujando == True:
            cv2.rectangle(imagen, (valorx,valory), (x,y), (0,255,0),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        dibujando = False
        cv2.rectangle(imagen, (valorx,valory), (x,y), (0,255,0),-1)

# Conectar imagen con la funcion
cv2.namedWindow('imagen')
cv2.setMouseCallback('imagen',dibujar)

# Mostrar la imagen donde vamos a dibujar
imagen = np.zeros((500,500,3), np.int8)

while True:
    cv2.imshow('imagen', imagen)
    if cv2.waitKey(10) & 0xFF == 27:
        break
cv2.destroyAllWindows()

























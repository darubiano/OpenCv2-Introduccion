# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:30:03 2020

@author: darub
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

# Definimos la funcion para dibujar con el raton
def dibujar(event, x, y, etiquetas, parametros):
    # dibujar circulo
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen, (x,y),50, (0,255,0),-1)

# Conectar imagen con la funcion
cv2.namedWindow('imagen')
cv2.setMouseCallback('imagen',dibujar)

# mostrar imagen donde se va a pintar
imagen = np.zeros((500,500,3), np.int8)

while True:
    cv2.imshow('imagen', imagen)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()
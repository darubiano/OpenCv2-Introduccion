# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:41:24 2020

@author: darub
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 


ajedrez = cv2.imread('tablero-ajedrez.png')
ajedrez_gris = cv2.cvtColor(ajedrez, cv2.COLOR_BGR2GRAY)
plt.imshow(ajedrez_gris, cmap='gray')

# selecionar 100 esquinas
esquinas = cv2.goodFeaturesToTrack(ajedrez_gris,100,0.01,10)
# transformar los valores numericos
esquinas = np.int0(esquinas)

# colorear las esquinas del ajedrez
for i in esquinas:
    x,y = i.ravel()
    cv2.circle(ajedrez, (x,y), 4, (255,0,0), 8)
plt.imshow(ajedrez)


ajedrez_real = cv2.imread('ajedrez_real.jpg')
ajedrez_real_gris = cv2.cvtColor(ajedrez_real,cv2.COLOR_BGR2GRAY)
plt.imshow(ajedrez_real_gris, cmap='gray')

# selecionar 150 esquinas
esquinas_real = cv2.goodFeaturesToTrack(ajedrez_real_gris,150,0.01,10)
# transformar los valores numericos
esquinas_real = np.int0(esquinas_real)

# colorear las esquinas del ajedrez
for i in esquinas_real:
    x,y = i.ravel()
    cv2.circle(ajedrez_real, (x,y), 2, (255,0,0), 2)
plt.imshow(ajedrez_real)



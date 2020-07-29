# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:59:43 2020

@author: darub
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 

cara = cv2.imread('cara.jpg')
cara = cv2.cvtColor(cara, cv2.COLOR_BGR2RGB)
plt.imshow(cara)

# selecionar los valores de 100
contorno = cv2.Canny(cara,threshold1=100, threshold2=100)
plt.imshow(contorno)

# suavizar la imagen
cara = cv2.blur(cara, ksize=(5,5))
plt.imshow(cara)
contorno = cv2.Canny(cara,threshold1=100, threshold2=100)
plt.imshow(contorno)


mano = cv2.imread('mano.jpg')
mano = cv2.cvtColor(mano, cv2.COLOR_BGR2GRAY)
plt.imshow(mano, cmap='gray')

# selecionar los valores de 100
contorno1 = cv2.Canny(mano,threshold1=100, threshold2=100)
plt.imshow(contorno1)
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:12:19 2020

solucion al error xfeatures2d

pip install opencv-contrib-python --user
@author: darub
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 

cereal = cv2.imread('cereal.png')
cereal = cv2.cvtColor(cereal, cv2.COLOR_BGR2RGB)
plt.imshow(cereal)

cereales = cv2.imread('cereales.png')
cereales = cv2.cvtColor(cereales, cv2.COLOR_BGR2RGB)
plt.imshow(cereales)

# extractor de caracteristicas
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(cereal,None)
kp2, des2 = sift.detectAndCompute(cereales,None)

# buscar valores emparejados de de las descripciones de las imagenes
indice = dict(algorithm=0, tress=5)
busqueda = dict(checks=50)

flan = cv2.FlannBasedMatcher(indice,busqueda)
emparejamientos = flan.knnMatch(des1, des2, k=2)

mejores = []
for e1, e2 in emparejamientos:
    if e1.distance < 0.7*e2.distance:
        mejores.append([e1])

imagen_emparejamientos = cv2.drawMatchesKnn(cereal, kp1, cereales,kp2,mejores[0:30],None,flags=0)
imagen_emparejamientos = cv2.cvtColor(imagen_emparejamientos, cv2.COLOR_BGR2RGB)
plt.imshow(imagen_emparejamientos)



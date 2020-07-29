# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:25:15 2020
https://github.com/opencv/opencv/tree/master/data/haarcascades
@author: darub
"""

import matplotlib.pyplot as plt
import cv2

# metodo de cascada
cascada_cara = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detectar_cara(imagen):
    # copiar para no modificar la imagen original
    imagen1 = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(imagen1)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1, (x,y), (x+w,y+h),(255,0,0),5)
    return imagen1, imagen[y:y+h,x:x+w]

## pruebas
# Cargar imagen 
pedro = cv2.imread('pedro0.jpg',0)
#pedro = cv2.cvtColor(pedro, cv2.COLOR_BGR2RGB)
plt.imshow(pedro, cmap='gray')
#buscar a pedro
resultado_pedro, cara = detectar_cara(pedro)
plt.imshow(resultado_pedro,cmap='gray')
plt.imshow(cara,cmap='gray')

# Cargar imagen 
jaime = cv2.imread('jaime.jpg')
jaime = cv2.cvtColor(jaime, cv2.COLOR_BGR2RGB)
plt.imshow(jaime)
# buscar a jaime
resultado_jaime, _ = detectar_cara(jaime)
plt.imshow(resultado_jaime)      
 

# cargar imagen
bus = cv2.imread('bus.jpg')
bus = cv2.cvtColor(bus, cv2.COLOR_BGR2RGB)
plt.imshow(bus)

# buscar caras
resultado_bus = detectar_cara(bus)
plt.imshow(resultado_bus)

""" REAL TIME """
# url de DroidCam 'http://192.168.0.4:4848/video'
captura = cv2.VideoCapture(0)
while True:
    resultado, video = captura.read()
    rectangulos = cascada_cara.detectMultiScale(video)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(video, (x,y), (x+w,y+h),(0,255,0),2)
    cv2.imshow('video',video)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
captura.release()
cv2.destroyAllWindows()

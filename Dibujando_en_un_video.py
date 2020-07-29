# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:01:57 2020

@author: darub
"""
import cv2


captura = cv2.VideoCapture('http://192.168.0.4:4848/video')

ancho = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Esquina izquierda
x,y = ancho//2,alto//2
# dimension del rectangulo
w = ancho//4
h = alto//4

while True:
    resultado, video = captura.read()
    # dibujar el rectangulo
    cv2.rectangle(video,(x,y),(x+w,y+h),color=(255,0,0), thickness=4)
    cv2.imshow('video',video)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
cv2.destroyAllWindows()












# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:21:10 2020

@author: darub
"""

import cv2

captura = cv2.VideoCapture('video.mp4')

while captura.isOpened():
     resultado, video = captura.read()
     if resultado == True:
         cv2.imshow('video',video)
         if cv2.waitKey(1) & 0xFF == ord('q'):
             break
     else:
         break

captura.release()
cv2.destroyAllWindows()

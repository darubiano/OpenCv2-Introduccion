# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:02:09 2020

@author: darub
"""

import cv2

# url de DroidCam 'http://192.168.0.4:4848/video'
captura = cv2.VideoCapture(0)

# dimensiones del video
ancho = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Windows
codigo = cv2.VideoWriter_fourcc(*'DIVX')
grabador = cv2.VideoWriter('video.mp4',codigo,20,(ancho,alto))

while True:
    resultado, video = captura.read()
    cv2.imshow('video',video)
    # Grabar
    grabador.write(video)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
grabador.release()
cv2.destroyAllWindows()
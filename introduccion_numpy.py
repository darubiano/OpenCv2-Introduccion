# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:01:32 2020

@author: darub
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

array = np.array([1,2,3])
rango = np.arange(5,30,2)
unos = np.ones(shape=(3,3))
# generar 50 numeros aleatorios entre 0 y 100
aleatorios = np.random.randint(0,100,50)
# valor maximo posicion
aleatorios.argmax()
# numero maximo
aleatorios.max()
# numero minimo
aleatorios.min()
# tamaño
aleatorios.shape
# redimencionar lista a matriz
aleatorios = aleatorios.reshape([10,5])

# cargar imagen de tipo imagen
imagen = Image.open('perro.jpg')
print(type(imagen))
# shape de la imagen
print(imagen.size)
# convetir la imagen en una matriz
array_imagen = np.array(imagen)
# mostrar imagen
plt.imshow(array_imagen)
# (1280, 1920, 3)
print(array_imagen.shape)

# seleccionar solo un color del RGB (0,1,2)
# rojo
print(array_imagen[:,:,0])
# verde
print(array_imagen[:,:,1])
# azul
print(array_imagen[:,:,2])

# mapear rojos de este arreglo
plt.imshow(array_imagen[:,:,0], cmap="Reds")




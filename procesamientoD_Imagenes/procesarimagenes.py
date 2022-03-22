# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 13:05:50 2022

@author: armma
"""

import cv2
import numpy as np

img = cv2.imread('crash_ejem.jpg');
print("- Number of Pixels: " + str(img.size))
print("- Shape/Dimensions: " + str(img.shape))
img = cv2.resize(img, (750, 500));
#imagen original
cv2.imshow('Esta es la imagen original',img);


#La imagen cambiada a color gris
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
cv2.imshow('Esta es la imagen GRIS',imgGray);
#----------------guardar imagen---------------------#
cv2.imwrite("guardar/ImagenGris.png",imgGray);
imageOut = imgGray[60:220,280:480];
cv2.imwrite("guardar/ImagenGris_recortada.png",imageOut);

#ortar imagen

rotationMatrix = cv2.getRotationMatrix2D((750/2, 500/2), 180, .5);
rotatedImage = cv2.warpAffine(img, rotationMatrix, (750, 500));
cv2.imshow('Imagen Girada', rotatedImage)
cv2.imwrite("guardar/ImagenRotada.png",rotatedImage);
#contraste

contrast_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
cv2.imshow('Imagen Contraste', contrast_img);
cv2.imwrite("guardar/ImagenContraste.png",contrast_img);
imageOut_contrats = contrast_img[60:220,280:480];
cv2.imshow("Imagen recortada",imageOut_contrats);

#La imagen cambiada a Blur
imgBlur = cv2.GaussianBlur(imgGray, (5,5),2) ;
cv2.imshow('Esta es la imagen BLUR',imgBlur);
cv2.imwrite("guardar/ImagenBlur.png",imgBlur);


#La imagen con bordes Canny
imgCanny = cv2.Canny(img,100,100) ;
cv2.imshow('Esta es con bordes Canny',imgCanny);
cv2.imwrite("guardar/ImagenCanny.png",imgCanny);

#La imagen cambiada a la dilataion
kernel = np.ones((5,5), np.uint8);
imgDilate = cv2.dilate(imgCanny, kernel, iterations=1);
cv2.imshow('Esta es la imagen con dilatacion',imgDilate);
cv2.imwrite("guardar/ImagenDilate.png",imgDilate);


#La imagen eroded
imgEroded = cv2.erode(imgDilate, kernel, iterations=1);
cv2.imshow('Esta es la imagen con eroded',imgEroded);
cv2.imwrite("guardar/ImagenEroded.png",imgEroded);




cv2.waitKey(0);



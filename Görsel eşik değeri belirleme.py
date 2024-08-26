import cv2
import numpy as np

foto =cv2.imread("deniz.jpg",0)

_, esik_foto = cv2.threshold(foto,80,255,cv2.THRESH_BINARY)

esik_foto2 = cv2.adaptiveThreshold(foto,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,13,9)
#blocksize değeri tek sayı olması lazım +1 kendi pikselimiz var ort tam sayı çıkması içn

cv2.imshow('foto',foto)
cv2.imshow('esik_foto',esik_foto)
cv2.imshow('esik_foto2',esik_foto2)
cv2.waitKey(0)

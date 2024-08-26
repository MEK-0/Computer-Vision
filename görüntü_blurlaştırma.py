import cv2

import numpy as np

foto = cv2.imread("deniz.jpg")

ortalama = cv2.blur(foto,(3,3))

gauss = cv2.GaussianBlur(foto,(3,3),8)
# gauss ortalama blurden daha doğru gösterir

medyan =cv2.medianBlur(foto,5)

cv2.imshow("foto",foto)
cv2.imshow("ortalama",ortalama)
cv2.imshow("gauss",gauss)
cv2.imshow("medyan",medyan)
cv2.waitKey(0)

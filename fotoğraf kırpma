import cv2
import time

foto = cv2.imread("carl.jpg")

print("fotoğraf boyutu :",foto.shape)


cv2.imshow("carl.jpg",foto)
foto2 = cv2.resize(foto,(500,500))
print("yeni fotoğraf boyutu :",foto2.shape)
cv2.imshow("foto2",foto2)

foto3= foto[150:700,500:900]
cv2.imshow("foto3",foto3)
cv2.waitKey(0)

import cv2

foto =cv2.imread("carl.jpg")
print("fotoğrafın boyutu : ",foto.shape)

#çizgi

cv2.line(foto,(0,0),(500,500),(0,255,0),5) #BGR

#dikdörtgen


cv2.rectangle(foto,(450,200),(900,700),(255,0,0),5)

#çember

cv2.circle(foto,(650,400),250,(0,0,255),5)

#yazı
cv2.putText(foto,"carl sagan",(450,200),cv2.FONT_ITALIC,1,(255,255,255),4)

cv2.imshow("carl.jpg",foto)
cv2.waitKey(0)



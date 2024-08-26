import cv2

uzay = cv2.imread("uzay (1).jpg")
uzayb = cv2.resize(uzay,(660,660))
deniz = cv2.imread("deniz.jpg")

birlestir =cv2.addWeighted(uzayb,0.5,deniz,0.5,0)


cv2.imshow("foto",birlestir)
cv2.waitKey(0)

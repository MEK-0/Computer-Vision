import cv2

foto =cv2.imread("carl.jpg",0)

cv2.imshow('carl.jpg',foto)

k = cv2.waitKey()


if k == ord("s"):
    cv2.imwrite("carl.jpg_gri1",foto)
    print("kayıt edildi")

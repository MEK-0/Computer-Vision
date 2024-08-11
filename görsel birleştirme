import cv2

import numpy as np

kedi = cv2.imread("kedi.jpg")
kediB =cv2.resize(kedi,(500,500))
köpek = cv2.imread("kopek.jpg")
köpekB =cv2.resize(köpek,(500,500))


yatay =np.hstack((kediB,köpekB))


dikey = np.vstack((kediB,köpekB))




cv2.imshow("foto", dikey)
cv2.waitKey(0)

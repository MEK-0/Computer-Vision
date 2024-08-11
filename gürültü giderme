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
print(foto.shape)




def gaus_gürültüsü(foto):
    row,col,ch = foto.shape
    mean = 0
    var = 0.05
    sigma = var**0.5

    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)

    gürültülü_gaus = foto + gauss


    return gürültülü_gaus

foto2 =foto/255
gaus_gürültüü = gaus_gürültüsü(foto2)

gaus2 = cv2.GaussianBlur(gaus_gürültüü,(3,3),6)

cv2.imshow("gaus gurultu",gaus_gürültüü)

def tuz_biber_gürültüsü(foto):
    row,col,ch = foto.shape
    oran = 0.5
    miktar = 0.005

    gürültülü = np.copy(foto)

    tuz_foto = np.ceil(miktar*foto.size*oran)
    koordinat = [np.random.randint(0,i - 1,int(tuz_foto)) for i in foto.shape]
    gürültülü[koordinat] = 1

    biber_foto = np.ceil(miktar*foto.size*oran)
    koordinat = [np.random.randint(0, i - 1, int(biber_foto)) for i in foto.shape]
    gürültülü[koordinat] = 0

    return gürültülü

tuz_biber = tuz_biber_gürültüsü(foto2)
medyan2 =cv2.medianBlur(tuz_biber.astype(np.float32),3)
cv2.imshow("tuz biber",tuz_biber)
cv2.imshow("medyan",medyan2)
cv2.waitKey(0)

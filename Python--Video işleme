import cv2

import time

video =cv2.VideoCapture("newyork.mp4")

print("genişlik : ",video.get(3))
print("yükseklik : ",video.get(4))




if video.isOpened() == False:
    print("hata !!")

while True:

    ret, frame = video.read()

    if ret == True:
      time.sleep(0.01)
      cv2.imshow("video",frame)
      cv2.waitKey(1)

    else:
        break

    if cv2.waitKey(1) == ord("q"):
        quit()



video.release()
cv2.destroyAllWindows()

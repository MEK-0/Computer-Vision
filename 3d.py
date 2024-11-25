import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

image_path="ucgen.jpg"
image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image,(200,200))
image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
cv2.waitKey(0)

x=np.arange(0,image.shape[1],1)
y=np.arange(0,image.shape[0],1)
x,y=np.meshgrid(x,y)
z=image


fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(x,y,z)
ax.set_title("xx")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()


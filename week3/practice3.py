# rotation

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('img/starfire.jpg',0)
rows,cols = img.shape

#plot original image
plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(img)

img_rotation = cv.warpAffine(img,cv.getRotationMatrix2D((cols/2,rows/2),30,0.6),(cols,rows))

#plot rotated image
plt.subplot(1,2,2)
plt.title("Rotated Image")
plt.imshow(img_rotation)
plt.show()

cv.imshow('img',img_rotation)
cv.imwrite('rotation_out.jpg',img_rotation)
cv.waitKey(0)
cv.destroyAllWindows()
# image shearing y axis

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('img/starfire.jpg',0)
rows, cols = img.shape

#plot original image
plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(img)

M = np.float32([[1,0,0],[0.5,1,0],[0,0,1]])
sheared_y_img = cv.warpPerspective(img,M, (int(cols*1.5),int(rows*1.5)))


#plot sheared image
plt.subplot(1,2,2)
plt.title("Sheared Y Image")
plt.imshow(sheared_y_img)
plt.show()

cv.imwrite('sheared_y_out.jpg',sheared_y_img)
cv.waitKey(0)
cv.destroyAllWindows()
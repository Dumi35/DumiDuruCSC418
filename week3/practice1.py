# translation

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('img/starfire.jpg',0)
rows, cols = img.shape

#plot original image
plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(img)

M = np.float32([[1,0,100],[0,1,50]])
trans1 = cv.warpAffine(img,M,(cols,rows))

#plot translated image
plt.subplot(1,2,2)
plt.title("Translated Image")
plt.imshow(trans1)

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
# image cropping

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('img/starfire.jpg',0)

#plot original image
plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(img)

cropped_img = img[450:700,200:500]

#plot cropped image
plt.subplot(1,2,2)
plt.title("Cropped Image")
plt.imshow(cropped_img)
plt.show()

cv.imwrite('cropped_out.jpg',cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()
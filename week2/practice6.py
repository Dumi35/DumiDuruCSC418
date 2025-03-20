#image scaling

import cv2
import matplotlib.pyplot as plt
import numpy as np

#load image
image = cv2.imread('img/starfire.jpg')

#plot original image
plt.subplot(1,2,1)
plt.title('Original')
plt.imshow(image)

#scale image by a factor of 2 along both axes
scaled_image = cv2.resize(image,None, fx=2, fy=2)

#save image
cv2.imwrite('img/Scaled.jpg', scaled_image)

#plot contrast image
plt.subplot(1,2,2)
plt.title('Scaled')
plt.imshow(scaled_image)
plt.show()
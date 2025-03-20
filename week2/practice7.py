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

#inverse by subtracting from 255
inverse_image = 255 - image

#save image
cv2.imwrite('img/inverse_image.jpg', inverse_image)

#plot contrast image
plt.subplot(1,2,2)
plt.title('Inverse Colour')
plt.imshow(inverse_image)
plt.show()
#removing noise from images

import cv2
import matplotlib.pyplot as plt
import numpy as np

#load image
image = cv2.imread('img/starfire.jpg')

#plot original image
plt.subplot(1,2,1)
plt.title('Original')
plt.imshow(image)

#remove noise using a median filter
filtered_image = cv2.medianBlur(image, 15)

#save image
cv2.imwrite('img/Median-Blur.jpg', filtered_image)

#plot contrast image
plt.subplot(1,2,2)
plt.title('Median Blur')
plt.imshow(filtered_image)
plt.show()
#sharpening images

import cv2
import matplotlib.pyplot as plt
import numpy as np

#load image
image = cv2.imread('img/starfire.jpg')

#plot original image
plt.subplot(1,2,1)
plt.title('Original')
plt.imshow(image)

#create sharpening kernel
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

#sharpen the image
sharpened_image = cv2.filter2D(image, -1, kernel)

#save the image
cv2.imwrite('img/sharpened_image.jpg', sharpened_image)

#plot sharpened image
plt.subplot(1,2,2)
plt.title('Sharpening')
plt.imshow(sharpened_image)
plt.show()
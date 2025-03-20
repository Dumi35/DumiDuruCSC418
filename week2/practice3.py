#adjusting brightness and contrast

import cv2
import matplotlib.pyplot as plt
import numpy as np

#load image
image = cv2.imread('img/starfire.jpg')

#plot original image
plt.subplot(1,2,1)
plt.title('Original')
plt.imshow(image)

#adjust the brightness and contrast
brightness = 5
contrast = 1.5
image2 = cv2.addWeighted(image,contrast,np.zeros(image.shape, image.dtype),0,brightness)

#save the image
cv2.imwrite('img/contrast_image.jpg', image2)

#plot contrast image
plt.subplot(1,2,2)
plt.title('Brightness & contrast')
plt.imshow(image2)
plt.show()
print ('hi apple')
import cv2
import numpy as np
# import matplotlib as plt

image = cv2.imread("img/rgb-colour-space.jpg")

#separate the colour spaces
B, G, R = cv2.split(image)

cv2.imshow("original",image)
cv2.waitKey(0)

cv2.imshow("blue",B)
cv2.waitKey(0)

cv2.imshow("green",G)
cv2.waitKey(0)

cv2.imshow("red",R)
cv2.waitKey(0)

cv2.destroyAllWindows()
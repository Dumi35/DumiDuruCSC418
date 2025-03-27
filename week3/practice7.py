# image blurring

import cv2 as cv

img = cv.imread('img/starfire.jpg',0)

cv.imshow('Original Image', img)
cv.waitKey(0)

# Gaussian blur
Gaussian = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian Blurring', Gaussian)
cv.waitKey(0)

# median blur
median = cv.medianBlur(img,5)
cv.imshow('Median Blurring', median)
cv.waitKey(0)

# Bilateral blur
bilateral = cv.bilateralFilter(img,9,75,75)
cv.imshow('Bilateral Blurring', bilateral)
cv.waitKey(0)

cv.destroyAllWindows()
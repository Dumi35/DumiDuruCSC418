#illustrating arithmetic operation of addition

#organising imports
import cv2

image1 = cv2.imread("img/starfire.jpg")
image2 = cv2.imread("img/powerpuffMe.png")

#resize images as both images must have the same size
image1 = cv2.resize(image1,(500,400))
image2 = cv2.resize(image2,(500,400))

#0.5 is opacity/weight of image1, 0.6 is opacity/weight of image2
addImage = cv2.addWeighted(image1,0.5,image2,0.6,0)

#window showing output image
cv2.imshow("Weighted image",addImage)

#deallocate associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
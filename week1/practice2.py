#read image in grayscale

import cv2

#image path
path = "img/me.png"

#read image using imread function
image = cv2.imread(path,0)

#window name where image is displayed
window_name = 'Dumi in Gray'

#Display image
cv2.imshow(window_name,image)

#hold the window
cv2.waitKey(0)

#remove/delete gui window from screen andmemory
cv2.destroyAllWindows()
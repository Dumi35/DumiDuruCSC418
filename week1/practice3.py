#saving an image

import cv2
import os

#image path
path = r'C:\\Users\dumid\Documents\\PAU Notes\\Year4\\CSC 418\\codes\week1\\img\\me.png'

#image directory
directory = r'C:\\Users\dumid\Documents\\PAU Notes\\Year4\\CSC 418\\codes\week1\\img'


#read image in greyscale
image = cv2.imread(path,0)

#change current directory to specified directory
os.chdir(directory)

#list files and directories
print("Before saving images")
print(os.listdir(directory))

filename = 'greyDumi.jpg'

#using cv2.imwrite() to save the image
cv2.imwrite(filename,image)

#list files and directories
print("After saving images")
print(os.listdir(directory))

print('Successfully saved')
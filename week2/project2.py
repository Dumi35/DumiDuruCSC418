#this project allows PAU UMC Members to login and displays their profile pic upon successful login

import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_image(title,image):
    #plot contrast image
    plt.subplot(1,2,2)
    plt.title(title)
    plt.imshow(image)
    plt.show()

class CSC400LvlMembers:
    def __init__(self):
        self.members = {}

    def add_member(self, username, firstname, mat_no):
        #Adds a new member .
        self.members[username] = {
            'firstname': firstname,
            'mat_no': mat_no,
            'originalImage': 'img/proj2/'+username+'.jfif'
        }

    def returnAllMembers(self):
        return self.members.items()
    
    def displayProfilePic(self,originalImage):
        # read original image
        image = cv2.imread(originalImage)

        cv2.imshow("Profile Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def adjustBrightness(self,originalImage):
        # read original image
        image = cv2.imread(originalImage)

        #adjust the brightness and contrast
        brightness = 5
        contrast = 1.5
        brightened_image = cv2.addWeighted(image,contrast,np.zeros(image.shape, image.dtype),0,brightness)

        plot_image("Brightness", brightened_image)

    def sharpen(self,originalImage):
        # read original image
        image = cv2.imread(originalImage)

        #create sharpening kernel
        kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

        #sharpen the image
        sharpened_image = cv2.filter2D(image, -1, kernel)

        plot_image("Sharpening", sharpened_image)

    def removeNoise(self,originalImage):
        # read original image
        image = cv2.imread(originalImage)

        #remove noise using a median filter
        filtered_image = cv2.medianBlur(image, 15)

        plot_image("Median Blur", filtered_image)

    def scaling(self,originalImage):
        # read original image
        image = cv2.imread(originalImage)

        #scale image by a factor of 2 along both axes
        scaled_image = cv2.resize(image,None, fx=2, fy=2)

        plot_image("Scaled", scaled_image)

    def inverseTransform(self,originalImage):
        # read original image
        image = cv2.imread(originalImage)

        #inverse by subtracting from 255
        inverse_image = 255 - image

        plot_image("Inverse Colour", inverse_image)

    def selectEnhancement(self,originalImage):
        print('Type B for brightness')
        print('Type I for inverse transformation')
        print('Type N to remove noise')
        print('Type P to view profile pic')
        print('Type RS to resize and scale')
        print('Type S for sharpening')
        print('Type Q to quit')

        while True:
            option = input('Please select an option ')
            match option:
                case 'B':
                    self.adjustBrightness(originalImage)
                case 'I':
                    self.inverseTransform(originalImage)
                case 'N':
                    self.removeNoise(originalImage)
                case 'P':
                    self.displayProfilePic(originalImage)
                case 'RS':
                    self.scaling(originalImage)
                case 'S':
                    self.sharpen(originalImage)
                case 'Q':
                    return

# initialising the Computer Science class
csc = CSC400LvlMembers()

# Adding members
csc.add_member('Dumi', 'Dumebi', '001')
csc.add_member('Clementicus', 'Clement', '002')
csc.add_member('Miraculous', 'Miracle', '003')
csc.add_member('StainlessSteel', 'Chima', '004')
csc.add_member('Testy', 'Testimony', '005')
csc.add_member('BurnaBoy', 'Bonaventure', '006')
csc.add_member('Love', 'Love', '007')
csc.add_member('Preccie', 'Precious', '008')
csc.add_member('Steph', 'Stephanie', '009')
csc.add_member('Bimpz', 'Bimpe', '010')

          
def login():
    name = input('Please enter your username ')
    mat_no = input('Please enter your matric number ')

    for key, value in csc.returnAllMembers():
        if name == key and mat_no == value['mat_no']:
            print('login successful')
            csc.selectEnhancement(value['originalImage'])
            return
    #if no match found
    print('login failed')
        
login()


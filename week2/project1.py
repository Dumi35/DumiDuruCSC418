#this project allows PAU UMC Members to login and displays their profile pic upon successful login

import cv2
import numpy as np
import requests

class UMCMembers:
    def __init__(self):
        self.members = {}

    def add_member(self, username, firstname, lastname, url):
        #Adds a new member .
        self.members[username] = {
            'firstname': firstname,
            'lastname': lastname,
            'password': self.derivePasswordLength(lastname),
            'url': url
        }

    #determine the length of the password from the username.
    # Password = sum of the number of alphabets of the surname
    def derivePasswordLength(self, lastname):
        return len(lastname)

    def returnAllMembers(self):
        return self.members.items()
    
    def displayProfilePic(self,url):
        # Fetch the image from the URL
        response = requests.get(url)
        image_array = np.asarray(bytearray(response.content), dtype=np.uint8)

        # Decode the image using OpenCV
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        image = cv2.resize(image,(500,400))

        cv2.imshow("Online Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# initialising the umc members class
umc = UMCMembers()

# Adding members
umc.add_member('enase', 'Enase', 'Okonedo', "https://pau.edu.ng/wp-content/uploads/2024/06/enase-okonedo-vice-chancellor-pan-atlantic-university.jpg")
umc.add_member('darlington', 'Darlington', 'Agbholor', "https://pau.edu.ng/wp-content/uploads/2024/06/Darlington-Agbholor-sst-scaled.jpg")
umc.add_member('adaora', 'Adaora', 'Onaga', "https://pau.edu.ng/wp-content/uploads/2023/04/Dr.-Onaga-Picture-200x300.jpg")

def login():
    name = input('Please enter your username ')
    password = int(input('Please enter your password '))

    for key, value in umc.returnAllMembers():
        if name == key and password == value['password']:
            print('login successful')
            umc.displayProfilePic(value['url'])
            return
    #if no match found
    print('login failed')
        
login()


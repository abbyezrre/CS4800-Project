# Map controller to search for specific room building
#Abigail
from user import *
from Database.StoringUserInfo import *
class Map:
    
    def __init__(self):
        self.signupStatus = False
        self.user = storingMap()
        self.map = pullingMapInfo()
        
    #stores room info, needs to be updated so I don't have to manually insert each image    
    def storeMap(self):
        
        ig = r"bizzini1/b103.png"
        mapImage = storingMap()
        
        mapImage.set_location("")
        mapImage.set_building("")
        mapImage.set_roomnumber("")
        mapImage.set_image(ig)
        
        
        
        mapImage.create_new_document()
    # searches for room number and retrives the image associated with it
    def searchMap(self, roomnumber):
        mapI = self.map
        if mapI.get_location(roomnumber) == roomnumber:
            return mapI.get_image(roomnumber)
        
        pass
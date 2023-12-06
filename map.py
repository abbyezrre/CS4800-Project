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
    def storeMap(self, location, building, roomnumber, image):
        
        ig = r"bizzini1/b103.png"
        mapImage = storingMap()
        
        mapImage.set_location = location
        mapImage.set_building = building
        mapImage.set_roomnumber = roomnumber
        mapImage.set_image = image
        
        
        
        mapImage.create_new_document()
        
    # searches for room number and retrives the image associated with it
    def searchMap(self, roomnumber):
        getroomImage = self.map
        if getroomImage.get_location(roomnumber) == roomnumber:
            return getroomImage.get_image(roomnumber)
        
        pass
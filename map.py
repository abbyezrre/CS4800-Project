# Map controller to search for specific room building
#Abigail
from user import *
from Database.StoringUserInfo import *
class Map:
    
    def __init__(self):
        self.map = pullingMapInfo()
        
    #stores room info, needs to be updated so I don't have to manually insert each image    
    def storeMap(self):
        
        ig = r"bizzini1\b108.png"
        mapImage = storingMap()
        
        mapImage.set_location("")
        mapImage.set_building("")
        mapImage.set_image(ig)
        
        
        
        mapImage.create_new_document()
        
    # searches for room number and retrives the image associated with it
    def searchMap(self, roomnumber):
        getroomImage = self.map
        if getroomImage.get_location(roomnumber) == roomnumber:
            return getroomImage.get_image(roomnumber)
        
        pass
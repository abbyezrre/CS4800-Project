# Map controller to search for specific room building
from user import *
from Database.StoringUserInfo import *
class Map:
    
    def __init__(self):
        self.signupStatus = False
        self.user = storingMap()
        self.map = pullingMapInfo()
        
    def storeMap(self):
        
        ig = r"C:\Users\abiga\OneDrive\Documents\CS4800\Project\CS4800-Project\bizzini1\b101.png"
        mapImage = storingMap()
        
        mapImage.set_location("B101")
        mapImage.set_building("Bizzini")
        mapImage.set_roomnumber("101")
        mapImage.set_image(ig)
        
        
        
        mapImage.create_new_document()
        
    def searchMap(self, roomnumber):
        mapI = self.map
        if mapI.get_location(roomnumber) == roomnumber:
            return mapI.get_image(roomnumber)
        
        pass
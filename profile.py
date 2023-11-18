#Elvin

from login import *
from Database.StoringUserInfo import *
from Database.pullingUserInfo import *

class profile:
    
    def __init__(self):
        self.user = pullingUserInfo()
        

        
    def userProfile(self):
        
        #pulls user info from database
        dbase = pullingUserInfo()
    
        
        typeUsername = loginPage.forProfile()


        print("\n" + "User Profile:")
        print(dbase.get_fullname(typeUsername))
        #print(dbase.get_major(typeUsername))
        print("<major here>")
        print(dbase.get_bio(typeUsername))

        #displays profile image
        i = input("\n" + "Display Profile Image?: ")
        if i == "yes":
            dbase.get_image(typeUsername)


        
            

        
     
        
          
            
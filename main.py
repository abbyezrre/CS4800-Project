
from Database.pullingUserInfo import *
from Database.StoringUserInfo import *
from PIL import Image
from io import BytesIO

from login import *
from user import *
from signup import *
from map import *
from profile import *



def main():
    """
    #login testing - helen
    loginTest = loginPage()
    loginTest.login()


    
    # test for signup and login - Abigail
    n = input("\n" + "Are you a new User: ")
    if n == "y":
        #signup testing - Abigail
        signupTest = signupPage()
        signupTest.signup()
        
        loginTest = loginPage()
        loginTest.login()
        
    else:
        #login testing - helen
        loginTest = loginPage() 
        loginTest.login()
        
    # test for profile - Elvin
    u = input("\n" + "Display profile?: ")  
    if u == "yes":
        #profile testing - Elvin
        displayUser = profile()
        displayUser.userProfile()
    """
    #map testing - Abigail Ezrre
    #stores the map images into the database
    """
    
    mapTest.storeMap()
    """
    mapTest = Map()
    #searches for the room 
    x = input("Enter room number: ")
    mapI = mapTest.searchMap(x) 
    if mapI is True:
        print(mapI)
    
if __name__ == "__main__":
    main()

    

from Database.pullingUserInfo import *
from Database.StoringUserInfo import *

from login import *
from user import *
from signup import *
from profile import *


def main():
<<<<<<< HEAD

    #login testing - helen
    loginTest = loginPage()
    loginTest.login()


=======
    
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
   
    
>>>>>>> 74639907507f3b687c6abf307844bcc37dded12b
if __name__ == "__main__":
    main()

    
from Database.pullingUserInfo import *
from Database.StoringUserInfo import *

from login import *
from user import *
from signup import *


def main():
    
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
    


if __name__ == "__main__":
    main()

    
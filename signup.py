# Abigail 
from user import *
from Database.StoringUserInfo import *


class signupPage:
    
    def __init__(self):
        self.signupStatus = False
        self.user = StoringUserInfo()
    
    def signup(self):
        
            #create a new user
            newUser = StoringUserInfo()
            
            
            newUser.set_username(input("Username: "))
            newUser.set_firstname(input("First Name: "))
            newUser.set_lastname(input("Last Name: "))
            newUser.set_password(input("Create Password: "))

            # stores the new info back into the database document
            newUser.create_new_document()
            



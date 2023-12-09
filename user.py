# written by: helen
# tested by: helen
# debugged by: helen
from Database.pullingUserInfo import *

# this class creates the user object and stores username, pass, email, etc.
class User:
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.fullname = ""
        self.username = ""
        self.password = ""
        self.user_email = ""
        self.age = -99
        self.signup_date = -99
        self.profile_name = ""
        self.bio = ""
        self.database = pullingUserInfo()
        
    #finds the user if key matches and updates values and returns true, otherwise returns false

    def findUser(self, username):

        if username in self.database.get_allFieldInfo('username'):

            self.firstname = self.database.get_firstname(username)
            self.lastname = self.database.get_lastname(username)  
            self.fullname = self.database.get_fullname(username)
            self.username = self.database.get_username(username)
            self.password = self.database.get_password(username)
            #self.user_email = self.database.get_useremail(username)
            self.age = self.database.get_age(username)
            
            #error with retrieving bio if you pick a user that doesnt have a bio
            #self.bio = self.database.get_bio(username)
            return True
        else:
            return False
    
    #returns the user object after user/pass is modified
    def returnUser(self):
        return User()

        
    #copy pasted from fakeB.py that isaac made
    
    # get full name
    def get_fullname(self):
        return self.firstname + " " + self.lastname
    
    # get only first name
    def get_firstname(self):
        return self.firstname
    
    # get only last name
    def get_lastname(self):
        return self.lastname
    
    # get username
    def get_username(self):
        return self.username
    
    # get password
    def get_password(self):
        return self.password
    
    # get email
    def get_useremail(self):
        return self.user_email
    
    # get age
    def get_age(self): 
        return self.age
    
    # get sign in date
    def get_signin_date(self):
        return self.signup_date
    
    # get name of profile
    def get_profile_name(self):
        return self.profile_name
    
    def get_user_bio(self):
        return self.bio

# written by: abigail and helen
# tested by: helen
# debugged by: helen
from Database.StoringUserInfo import *
from Database.pullingUserInfo import *

class signupPage:
    
    def __init__(self, username, fname, lname, pass1, pass2, email):
        self.signupStatus = False
        self.newUser = StoringUserInfo()
        self.username = username
        self.pass1 = pass1
        self.pass2 = pass2
        self.email = email
        self.fname = fname
        self.lname = lname
        self.error = None
    
    def signup(self):
        
        #create array of existing usernames
        usernameList = pullingUserInfo().get_allFieldInfo('username')

        #checks to see if username is taken
        if self.username in usernameList:
            self.error = 'Username is taken. Try again'
        else:

            #checks to see if passwords match
            if self.pass1 == self.pass2:
                self.newUser.set_username(self.username)
                self.newUser.set_firstname(self.fname)
                self.newUser.set_lastname(self.lname)
                self.newUser.set_email(self.email)
                self.newUser.set_password(self.pass1)
                self.newUser.create_new_document()
                self.signupStatus = True
            else:
                self.error = "Passwords don't match. Try again"
        

        
            



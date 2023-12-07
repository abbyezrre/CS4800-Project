#helen
from user import *
class loginPage:
    
    def __init__(self, username, password):
        self.loginStatus = False
        self.user = User()
        self.username = username
        self.password = password
        self.error = None
    
    #funciton to check if passwords are a match
    def checkpassword(self):
        #returns a bool if username is found
        verifyUser = self.user.findUser(self.username)
        
        #if user is found, then it sets login status as true
        #else it will set error to the error message
        if verifyUser:
            
            if self.user.get_password() == self.password:
                self.loginStatus = True
            else:
                self.error = 'Invalid Password. Please try again.'
        else:
            self.error = 'Invalid Username. Please try again.'
            
  
    
   
        
  
   

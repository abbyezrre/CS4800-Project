#helen
from user import *
class loginPage:
    
    def __init__(self, username, password):
        self.loginStatus = False
        self.user = User()
        self.username = username
        self.password = password
        self.error = None
        
    def checkpassword(self):
        
        verifyUser = self.user.findUser(self.username)
        
        if verifyUser:
    
            if self.user.get_password() == self.password:
                self.loginStatus = True
            else:
                self.error = 'Invalid Password. Please try again.'
        else:
            self.error = 'Invalid Username. Please try again.'
            
  
    
   
        
  
   

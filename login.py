
from user import *

class loginPage:
    
    def __init__(self):
        self.loginStatus = False
        self.user = User()

    # login function that prints success if user and pass are correct
    # else prints invalid and prompts user to try again
    def login(self):

        
        while self.loginStatus == False:
            userInputUsername = input("Enter your username: ")
            verifyUser = self.user.findUser(userInputUsername)
            
            if verifyUser is True:
                
                userInputPassword = input("Enter your password: ")
                if self.user.get_password() == userInputPassword:
                    print(f'You were successfully logged in {self.user.get_username()}!')
                    self.loginStatus = True
                else:
                    print("Invalid password.")
            else:
                print("Invalid username.")
                
            


        

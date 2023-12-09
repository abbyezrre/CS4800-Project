# written by: elvin
# tested by: elvin
# debugged by: elvin and helen

from login import *
from Database.StoringUserInfo import *
from Database.pullingUserInfo import *

class Profile:

  def __init__(self, username):
        self.dbase = pullingUserInfo()
        self.username = username
        self.error = None
        self.fullname = None
        self.age = None
        #self.major = major
        self.bio = None
        
  def displayFullname(self, username):
     
     
     self.fullname = self.dbase.get_fullname(username)     
  
  def displayAge(self, username):
      #username = 'reydub'
      self.age = self.dbase.get_age(username)
      
      
  #def displayMajor(self):
      
     
  def displayBio(self, username):
     
   self.bio = self.dbase.get_bio(username)

  def check_sign_in(self):
     
     self.error = 'Please sign in'
     
     
        
         
        
              

        
            

        
     
        
          
            
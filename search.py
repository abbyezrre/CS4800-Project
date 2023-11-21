
from user import *

#Helen
class searchBar:
    def __init__(self, query):
        self.query =  query
        self.user = User()
        self.output = []

        
    #for now, it just searches for usernames in the database and returns their first + last name
    def search(self):
        userValid = self.user.findUser(self.query)
        
        if userValid == True:
            self.output.append(self.user.get_fullname())


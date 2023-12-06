
from user import *
from Database.pullingUserInfo import *

#Helen
class searchBar:
    def __init__(self, query):
        self.query =  query
        self.user = User()
        self.output = []
        self.clubValid = False
        self.userValid = False

        
    #for now, it just searches for usernames in the database and returns their first + last name
    def search(self):

        self.userValid = self.user.findUser(self.query)
        club = pullingClubInfo()
        clubExists = club.get_club(self.query)

        
        if self.userValid == True:
            self.output.append(self.user.get_fullname())

            
        elif clubExists is not None:
            self.output.append(club.get_club(self.query) + " Club")
            self.output.append(club.get_contact(self.query))
            self.clubValid = True
        else:
            
            self.output.append("No results found")

            
    def getClubImage(self, club):
        getClubImage = pullingClubInfo()
        if self.clubValid is True:
            return getClubImage.get_image(club)
        
            
            



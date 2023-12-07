
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

        
    #searches usernames and clubs (Case sensitive)
    def search(self):
        #returns a bool if the search is a username
        self.userValid = self.user.findUser(self.query)
        #creates club db class
        club = pullingClubInfo()
        #returns the club if search matches, else clubExists = None
        clubExists = club.get_club(self.query)

        #if the search was a username, the full name of the user is appended tothe output
        if self.userValid == True:
            self.output.append(self.user.get_fullname())

        #else if the club is a match, then the club name and contact info is added
        elif clubExists is not None:
            self.output.append(club.get_club(self.query) + " Club")
            self.output.append(club.get_contact(self.query))
            self.clubValid = True
        
        #else no results are found
        else:
            self.output.append("No results found")

    #returns club image if the club is found     
    def getClubImage(self, club):
        getClubImage = pullingClubInfo()
        if self.clubValid is True:
            return getClubImage.get_image(club)
        
            
            



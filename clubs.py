#kim
from user import *
from Database.StoringUserInfo import *
from Database.pullingUserInfo import *

class ClubsController:
    def __init__(self):
        self.user_info = pullingClubInfo()

    def get_clubs_info(self):
        clubs = [
            {'name': self.user_info.get_club("Computer Science") , 'description': self.user_info.get_eventinfo("Computer Science") , 'contact': self.user_info.get_contact("Computer Science"), 'logo': self.user_info.get_image("Computer Science")},
            {'name': self.user_info.get_club("Gaming") , 'description': self.user_info.get_eventinfo("Gaming") , 'contact': self.user_info.get_contact("Gaming"), 'logo': self.user_info.get_image("Gaming")},
        ]
        return clubs
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
            {'name': self.user_info.get_club("Theatre"), 'description': self.user_info.get_eventinfo("Theatre"), 'contact': self.user_info.get_contact("Theatre"), 'logo': self.user_info.get_image("Theatre")},
            {'name': self.user_info.get_club("Anthropology"), 'description': self.user_info.get_eventinfo("Anthropology"), 'contact': self.user_info.get_contact("Anthropology"), 'logo': self.user_info.get_image("Anthropology")},
            {'name': self.user_info.get_club("Women's Club"), 'description': self.user_info.get_eventinfo("Women's Club"), 'contact': self.user_info.get_contact("Women's Club"), 'logo': self.user_info.get_image("Women's Club")},
            {'name': self.user_info.get_club("Math"), 'description': self.user_info.get_eventinfo("Math"), 'contact': self.user_info.get_contact("Math"), 'logo': self.user_info.get_image("Math")},
        ]
        return clubs
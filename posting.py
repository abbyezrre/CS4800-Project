from user import *
from Database.StoringUserInfo import *
from Database.pullingUserInfo import *

class posting:
    def __init__(self):
        self.user_post = []
        self.storing_post = storingPost()
        self.pulling_post = pullingPostInfo()
    
    def post_feed(self, name, message):
        self.user_post.append({'name': name, 'message': message})

    def get_user_post(self):
        return self.user_post
    

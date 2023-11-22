from user import *

class posting:
    def __init__(self):
        self.user_post = []
    
    def post_feed(self, name, message):
        self.user_post.append({'name': name, 'message': message})

    def get_user_post(self):
        return self.user_post
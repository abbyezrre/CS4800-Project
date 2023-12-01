from user import *
from Database.StoringUserInfo import *
from Database.pullingUserInfo import *

class PostingController:
    def __init__(self):
        self.user_post = []
        self.storing_post = storingPost()
        self.pulling_post = pullingPostInfo()
    
    #set user for the post
    def set_user(self, name):
        self.storing_post.set_user = name

    #function to check if user is set
    def post_feed(self, name, message):
        if self.storing_post.set_user is None:
            print("User required.")

        self.storing_post.set_comment(message)
        self.storing_post.create_new_document()

        self.user_post.append({'name': name, 'message': message})

    #get user post if a user is set
    def get_user_post(self):
        if self.user is not None:
            user_posts = self.pulling_post.get_user_posts(self.user)
            self.user_post = user_posts
        return self.user_post
    

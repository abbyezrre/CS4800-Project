class FakeData:

    #include clubs connection with data
    #include club activity 
    #event with summary post
    #place it is taking place
    # club info 
    
    def __init__(self):
        self.firstname = "John"
        self.lastname = "Smith"
        self.middlename = "Ken"
        self.username = "johnsmith209"
        self.password = "Password"
        self.user_email = "jsmith209@csustan.edu"
        self.age = 21
        self.signup_date = "10/18/23"
        self.profile_name = "Senor John"
        self.user_post_comment = "post comment here"
        self.comment_date = "10/18/23 10:54:12"
        self.post_image = "image here"
        self.post_video = "video here"
        self.clubs = ["Gaming Club", "Computer Science"]
        self.search_club = ""
        self.bio = "user bio here"
        self.validUsers = ["johnsmith209", "budgie", "superc0co", "elvin", "kim", "abbyeee"]
    
    #returns list of valid users
    def getUsernames(self):
        return self.validUsers
    
    # get full name
    def get_fullname(self):
        return self.firstname + " " + self.middlename + " " + self.lastname
    
    # get only first name
    def get_firstname(self):
        return self.firstname
    
    # get only middle name
    def get_middlename(self):
        return self.middlename
    
    # get only last name
    def get_lastname(self):
        return self.lastname
    
    # get username
    def get_username(self):
        return self.username
    
    # get password
    def get_password(self):
        return self.password
    
    # get email
    def get_useremail(self):
        return self.user_email
    
    # get age
    def get_age(self): 
        return self.age
    
    # get sign in date
    def get_signin_date(self):
        return self.signup_date
    
    # get name of profile
    def get_profile_name(self):
        return self.profile_name
    
    # get user post comment
    def get_user_post_comment(self):
        return self.user_post_comment
    
    # get date of posted comment
    def get_comment_date(self):
        return self.comment_date
    
    # get image posted (right now its a string but should be a pdf? pgn? discuss as a group)
    def get_post_image(self):
        return self.post_image
    
    # get video posted (right now its a string but should be a vid? discuss as a group)
    def get_post_video(self):
        return self.post_video
    
    def get_user_bio(self):
        return self.bio
    
    
    # check if we have club 
    #def get_clubs(self):
      #  if self.
    
    
    #
    # Example usage:
#fdb = FakeData()

    # Accessing variables

        # DO NOT REMOVE: 
        # password db: nJnreV9AdMHQoBs7
        # mongodb+srv://iflores10:<password>@cluster0.skqqar6.mongodb.net/
        # mongodb+srv://iflores10:nJnreV9AdMHQoBs7@cluster0.skqqar6.mongodb.net/

        
#print(fdb.get_fullname())

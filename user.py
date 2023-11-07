
# this class creates the user object and stores username, pass, email, etc.
class User:
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.middlename = ""
        self.username = ""
        self.password = ""
        self.user_email = ""
        self.age = -99
        self.signup_date = -99
        self.profile_name = ""
        self.bio = ""
        
        #creates a test dictionary of usernames and passwords for login functionality
        self.validUsers = {
            "johnsmith209" : "Password",
            "budgie" : "parakeet1",
            "superc0co" : "Isaac123",
            "abbyeee" : "h00ray!", 
            "kim" : "2bunny",
            "elvin" : "basketB"
        }
        
    #finds the user if key matches and updates values and returns true, otherwise returns false

    def findUser(self, key):
        #TODO: Update with correct database function. Right now it is pulling from a made up username list in FakeB
        if key in self.validUsers.keys():
            #TODO: needs to be uncommented out when we have a full database
            #self.firstname = self.database.get_firstname()
            #self.lastname = self.database.get_lastname()  
            #self.middlename = self.database.get_middlename()
            self.username = key
            self.password = self.validUsers[key]
            #self.user_email = self.database.get_useremail()
            #self.age = self.database.get_age()
            #self.signup_date = self.database.get_signin_date()
            #self.profile_name = self.database.get_profile_name()
            #self.bio = self.database.get_user_bio()
            return True
        else:
            return False
    
    #returns the user object after user/pass is modified
    def returnUser(self):
        return User()

        
    #copy pasted from fakeB.py
    
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
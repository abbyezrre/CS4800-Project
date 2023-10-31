import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://iflores10:nJnreV9AdMHQoBs7@cluster0.skqqar6.mongodb.net/")  

# Select the database
db = client["CampusConnect"]  

# Select the collection
collection = db["users"]  

# Query to retrieve documents (example: find all documents)
query = {}

# Find documents in the collection based on the query
cursor = collection.find(query)

#Iterate over the cursor to access each document
for document in cursor:
    print(document)


# def get_firstname():
#     # Query to retrieve documents only with the first name isaac
#     query = {"firstname" :"abby" }
#     cursor = collection.find(query)
    
    
#     # Find documents in the collection based on the query
#     cursor = collection.find(query)
    
#     for document in cursor:
#         print(document)
        
print(get_firstname())
# print(get_firstname())

    # # get full name
    # def get_fullname(self):
    #     return self.firstname + " " + self.middlename + " " + self.lastname

    # # get only first name
    # def get_firstname(self):
    #     return self.firstname
    
    # # get only middle name
    # def get_middlename(self):
    #     return self.middlename
    
    # # get only last name
    # def get_lastname(self):
    #     return self.lastname
    
    # # get username
    # def get_username(self):
    #     return self.username
    
    # # get password
    # def get_password(self):
    #     return self.password
    
    # # get email
    # def get_useremail(self):
    #     return self.user_email
    
    # # get age
    # def get_age(self): 
    #     return self.age
    
    # # get sign in date
    # def get_signin_date(self):
    #     return self.signup_date
    
    # # get name of profile
    # def get_profile_name(self):
    #     return self.profile_name
    
    # # get user post comment
    # def get_user_post_comment(self):
    #     return self.user_post_comment
    
    # # get date of posted comment
    # def get_comment_date(self):
    #     return self.comment_date
    
    # # get image posted (right now its a string but should be a pdf? pgn? discuss as a group)
    # def get_post_image(self):
    #     return self.post_image
    
    # # get video posted (right now its a string but should be a vid? discuss as a group)
    # def get_post_video(self):
    #     return self.post_video
    
    
    
    # # check if we have clu
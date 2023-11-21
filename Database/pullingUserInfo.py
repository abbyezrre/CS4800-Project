import pymongo
import base64  
from PIL import Image
from io import BytesIO

#Isaac Flores
class pullingUserInfo:
     
    def __init__(self):
        # connect to MongoDB
        self.client = pymongo.MongoClient("mongodb+srv://iflores10:nJnreV9AdMHQoBs7@cluster0.skqqar6.mongodb.net/")

        # select the database
        self.db = self.client["CampusConnect"]

        # select the collection
        self.collection = self.db["users"]

    # method to return a list all the user's info of one field
    # example "age" - displays a list of all the users ages in the database
    # example "username" - displays a list of all the usernames in the database
    def get_allFieldInfo(self, fieldname):
        # query to retrieve all documents
        query = {}

        # find documents in the collection based on the query
        cursor = self.collection.find(query)

        # initialize a list to store
        fieldList = []

        for document in cursor:
            # check if field exists in the document
            if fieldname in document:
                # append to the list
                fieldList.append(document[fieldname])

        # return the list 
        return fieldList

    # this method allows me to use it for every method we want to pull information from the database return a signle document filter
    # document how each users data is being store and filters are the information it store
    # example filter : username  ---- this filters the data by the user username ONLY
    def get_userInfo(self, field, username1):
        # query to retrieve documents only with the first name isaac
        query = {"username": username1}
        projection = {field:1}

        # find documents in the collection based on the query
        cursor = self.collection.find(query, projection)

        for document in cursor:
            return document[field]

    def get_firstname(self, username):
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "firstname"
        # call the get_userInfo method
        firstname = self.get_userInfo(fieldfilter, username)

        # return the result
        return firstname

    def get_lastname(self, username):
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "lastname"
        # call the get_userInfo method
        lastname = self.get_userInfo(fieldfilter, username)

        # return the result
        return lastname
        
        
    def get_username(self, username):
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "username"
        # call the get_userInfo method
        user = self.get_userInfo(fieldfilter, username)

        # return the result
        return user
     
    # THIS WILL ONLY BE USED TO CONFIRM USERS PASSWORD (USE ONLY FOR LOGIN)
    def get_password(self, username):
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "password"
        # call the get_userInfo method
        password = self.get_userInfo(fieldfilter, username)

        # return the result
        return password
    
    # method to return the age
    def get_age(self, username): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "age"
        # call the get_userInfo method
        age = self.get_userInfo(fieldfilter, username)

        # return the result
        return age
    
    # method to return the full name 
    def get_fullname(self, username1):
        # storing the first and last name in variable using the method already created
        first = self.get_firstname(username1)
        last = self.get_lastname(username1)
        
        # return the result
        return first + " " + last
    
    # open image stored in database
    def get_image(self, username):
        # filter for the info we need 
        field_filter = "image_data"
        # call the get_userInfo method
        image_data = self.get_userInfo(field_filter, username)

        if image_data:
            # decode the base64 image data
            decoded_image_data = base64.b64decode(image_data)

            # open and display the image using PIL
            image = Image.open(BytesIO(decoded_image_data))
            image.show()

   # method to return the bio
    def get_bio(self, username): 
        # filter of the info we need "bio"
        fieldfilter = "bio"
        # call the get_userInfo method
        bio = self.get_userInfo(fieldfilter, username)

        # return the result
        return bio
    
    


#Isaac Flores
class pullingMapInfo:
     
    def __init__(self):
        # connect to MongoDB
        self.client = pymongo.MongoClient("mongodb+srv://iflores10:nJnreV9AdMHQoBs7@cluster0.skqqar6.mongodb.net/")

        # select the database
        self.db = self.client["CampusConnect"]

        # select the collection
        self.collection = self.db["map"]
        
    def get_mapInfo(self, field, location):
        # query to retrieve documents only with the first name isaac
        query = {"location": location}
        projection = {field:1}

        # find documents in the collection based on the query
        cursor = self.collection.find(query, projection)

        for document in cursor:
            return document[field]   
        
        # open image stored in database
    def get_image(self, location):
        # filter for the info we need 
        field_filter = "image_data"
        # call the get_userInfo method
        image_data = self.get_mapInfo(field_filter, location)

        if image_data:
            # decode the base64 image data
            decoded_image_data = base64.b64decode(image_data)

            # open and display the image using PIL
            image = Image.open(BytesIO(decoded_image_data))
            image.show()

    # method to return the building
    def get_building(self, location): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "building"
        # call the get_mapInfo method
        building = self.get_mapInfo(fieldfilter, location)

        # return the result
        return building
    
        # method to return the roomnumber
    def get_roomnumber(self, location): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "roomnumber"
        # call the get_mapInfo method
        roomnumber = self.get_mapInfo(fieldfilter, location)

        # return the result
        return roomnumber
    
    # method to return the location
    def get_location(self, location): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "location"
        # call the get_mapInfo method
        roomnumber = self.get_mapInfo(fieldfilter, location)

        # return the result
        return roomnumber
    
        # # get only middle name
        # def get_middlename(self):
        #     return self.middlename
        


        # # get email
        # def get_useremail(self):
        #     return self.user_email
        
        
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
        
        
        
   

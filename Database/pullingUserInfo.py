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

        return image_data
    
        # if image_data:
        #     # decode the base64 image data
        #     decoded_image_data = base64.b64decode(image_data)

        #     # open and display the image using PIL
        #     image = Image.open(BytesIO(decoded_image_data))
        #     image.show()

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
        
        return image_data
        """
        if image_data:
    
        # if image_data:
        #     # decode the base64 image data
            decoded_image_data = base64.b64decode(image_data)

        #     # open and display the image using PIL
            image = Image.open(BytesIO(decoded_image_data))
            image.show()
        """
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
    
#Isaac Flores
class pullingClubInfo:
     
    def __init__(self):
        # connect to MongoDB
        self.client = pymongo.MongoClient("mongodb+srv://iflores10:nJnreV9AdMHQoBs7@cluster0.skqqar6.mongodb.net/")

        # select the database
        self.db = self.client["CampusConnect"]

        # select the collection
        self.collection = self.db["Clubs"]
        
    def get_clubInfo(self, field, club):
        # query to retrieve documents only with the first name isaac
        query = {"club": club}
        projection = {field:1}

        # find documents in the collection based on the query
        cursor = self.collection.find(query, projection)

        for document in cursor:
            return document[field]   
        
        # open image stored in database
    def get_image(self, club):
        # filter for the info we need 
        field_filter = "image_data"
        # call the get_userInfo method
        image_data = self.get_clubInfo(field_filter, club)

        return image_data
        #if image_data:
        #     # decode the base64 image data
        #    decoded_image_data = base64.b64decode(image_data)

        #     open and display the image using PIL
        #    image = Image.open(BytesIO(decoded_image_data))
        #    image.show()

    # method to return the title
    def get_title(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "title"
        # call the get_clubInfo method
        title = self.get_clubInfo(fieldfilter, club)

        # return the result
        return title
    
        # method to return the club name
    def get_club(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "club"
        # call the get_clubInfo method
        club = self.get_clubInfo(fieldfilter, club)

        # return the result
        return club
    
    def get_contact(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "contact"
        # call the get_clubInfo method
        contact = self.get_clubInfo(fieldfilter, club)

        # return the result
        return contact
    
    # method to return the location
    def get_location(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "location"
        # call the get_clubInfo method
        eventlocation = self.get_clubInfo(fieldfilter, club)

        # return the result
        return eventlocation
    
        # method to return the eventinfo
    def get_eventinfo(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "eventinfo"
        # call the get_clubInfo method
        eventinfo = self.get_clubInfo(fieldfilter, club)

        # return the result
        return eventinfo
    
        # method to return the event date
    def get_date(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "date"
        # call the get_clubInfo method
        date = self.get_clubInfo(fieldfilter, club)

        # return the result
        return date
    
        # method to return the time of event
    def get_time(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "time"
        # call the get_clubInfo method
        time = self.get_clubInfo(fieldfilter, club)

        # return the result
        return time
    

#Isaac Flores
class pullingPostInfo:
     
    def __init__(self):
        # connect to MongoDB
        self.client = pymongo.MongoClient("mongodb+srv://iflores10:nJnreV9AdMHQoBs7@cluster0.skqqar6.mongodb.net/")

        # select the database
        self.db = self.client["CampusConnect"]

        # select the collection
        self.collection = self.db["post"]
        
    def get_postInfo(self, field, user):
        # query to retrieve documents only with the first name isaac
        query = {"user": user}
        projection = {field:1}

        # find documents in the collection based on the query
        cursor = self.collection.find(query, projection)

        for document in cursor:
            return document[field]   
        
        # open image stored in database
    def get_image(self, user):
        # filter for the info we need 
        field_filter = "image_data"
        # call the get_userInfo method
        image_data = self.get_postInfo(field_filter, user)

        return image_data
        # if image_data:
        #     # decode the base64 image data
        #     decoded_image_data = base64.b64decode(image_data)

        #     # open and display the image using PIL
        #     image = Image.open(BytesIO(decoded_image_data))
        #     image.show()

    # method to return the building
    def get_comment(self, user): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "comment"
        # call the get_mapInfo method
        comment = self.get_postInfo(fieldfilter, user)

        # return the result
        return comment
    
        # method to return the roomnumber
    def get_timestamp(self, user): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "timestamp"
        # call the get_mapInfo method
        timestamp = self.get_postInfo(fieldfilter, user)

        # return the result
        return timestamp
    

    
#Isaac Flores
class pullingEventInfo:
     
    def __init__(self):
        # connect to MongoDB
        self.client = pymongo.MongoClient("mongodb+srv://iflores10:nJnreV9AdMHQoBs7@cluster0.skqqar6.mongodb.net/")

        # select the database
        self.db = self.client["CampusConnect"]

        # select the collection
        self.collection = self.db["events"]
        
    def get_eventsInfo(self, field, club):
        # query to retrieve documents only with the first name isaac
        query = {"club": club}
        projection = {field:1}

        # find documents in the collection based on the query
        cursor = self.collection.find(query, projection)

        for document in cursor:
            return document[field]   
        
        # open image stored in database
    def get_image(self, club):
        # filter for the info we need 
        field_filter = "image_data"
        # call the get_userInfo method
        image_data = self.get_eventsInfo(field_filter, club)

        return image_data
        # if image_data:
        #     # decode the base64 image data
        #     decoded_image_data = base64.b64decode(image_data)

        #     # open and display the image using PIL
        #     image = Image.open(BytesIO(decoded_image_data))
        #     image.show()

    # method to return the title
    def get_title(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "title"
        # call the get_clubInfo method
        title = self.get_eventsInfo(fieldfilter, club)

        # return the result
        return title
    
        # method to return the club name
    def get_club(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "club"
        # call the get_clubInfo method
        club = self.get_eventsInfo(fieldfilter, club)

        # return the result
        return club
    
    def get_contact(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "contact"
        # call the get_clubInfo method
        contact = self.get_eventsInfo(fieldfilter, club)

        # return the result
        return contact
    
    # method to return the location
    def get_location(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "location"
        # call the get_clubInfo method
        eventlocation = self.get_eventsInfo(fieldfilter, club)

        # return the result
        return eventlocation
    
        # method to return the eventinfo
    def get_eventinfo(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "eventinfo"
        # call the get_clubInfo method
        eventinfo = self.get_eventsInfo(fieldfilter, club)

        # return the result
        return eventinfo
    
        # method to return the event date
    def get_date(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "date"
        # call the get_clubInfo method
        date = self.get_eventsInfo(fieldfilter, club)

        # return the result
        return date
    
        # method to return the time of event
    def get_time(self, club): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "time"
        # call the get_clubInfo method
        time = self.get_eventsInfo(fieldfilter, club)

        # return the result
        return time
    
        # method to return the timestamp
    def get_timestamp(self, user): 
        # filter of the info we need (this name as to how it is stored in the data base)
        fieldfilter = "timestamp"
        # call the get_mapInfo method
        timestamp = self.get_eventsInfo(fieldfilter, user)

        # return the result
        return timestamp
    
import pymongo
import base64
from datetime import datetime

#Isaac Flores
class StoringUserInfo:

  def __init__(self):
    # connect to MongoDB
    self.client = pymongo.MongoClient("mongodb+srv://iflores10:nJnreV9AdMHQoBs7@cluster0.skqqar6.mongodb.net/")  

    # select the database
    self.db = self.client["CampusConnect"] 

    # select the collection
    self.collection = self.db["users"] 

    # initialize variables
    self.firstname = ""
    self.lastname = ""
    self.middlename = ""
    self.age = ""
    self.username = ""
    self.password = ""
    self.bio = ""
    self.email = ""
    self.image_data = None
    

   # setter method for image data
  def set_image(self, image_path):
    with open(image_path, "rb") as image_file:
      self.image_data = base64.b64encode(image_file.read()).decode("utf-8")

  # setter method for first name
  def set_firstname(self, firstname):
    self.firstname = firstname

  # setter method for last name
  def set_lastname(self, lastname):
    self.lastname = lastname

  # setter method for middle name
  def set_middlename(self, middlename):
    self.middlename = middlename

  # setter method for age
  def set_age(self, age):
    self.age = age

  # setter method for username
  def set_username(self, username):
    self.username = username

  # setter method for password
  def set_password(self, password):
    self.password = password
    
  # setter method for middle name
  def set_email(self, email):
    self.email = email
    
  # setter method for bio
  def set_bio(self, bio):
    self.bio = bio

  # method to create a new document in the MongoDB collection
  def create_new_document(self):
    # create a new document
    new_document = {
        "firstname": self.firstname,
        "lastname": self.lastname,
        "middlename": self.middlename,
        "username": self.username,
        "password": self.password,
        "age": self.age,
        "email": self.email,
        "bio": self.bio,
        "image_data": self.image_data
      }

    # insert the document into the collection
    result = self.collection.insert_one(new_document)


class storingMap:

  def __init__(self):
    # connect to MongoDB
    self.client = pymongo.MongoClient("mongodb+srv://iflores10:nJnreV9AdMHQoBs7@cluster0.skqqar6.mongodb.net/")  

    # select the database
    self.db = self.client["CampusConnect"] 

    # select the collection
    self.collection = self.db["map"] 

    self.roomnumber = ""
    self.building = ""
    self.location = ""
    self.image_data = None
    
  # setter method for image data
  def set_image(self, image_path):
    with open(image_path, "rb") as image_file:
      self.image_data = base64.b64encode(image_file.read()).decode("utf-8")
      
  # setter method for building
  def set_building(self, building):
    self.building = building
    
  # setter method for roomnumber
  def set_roomnumber(self, roomnumber):
    self.roomnumber = roomnumber
    
  # setter method for location
  def set_location(self, location):
    self.location = location
    
  # method to create a new document in the MongoDB collection
  def create_new_document(self):
    # create a new document
    new_document = {
        "location": self.location,
        "building": self.building,
        "roomnumber": self.roomnumber,
        "image_data": self.image_data
      }

    # insert the document into the collection
    result = self.collection.insert_one(new_document)
    
class storingClubs:

  def __init__(self):
    # connect to MongoDB
    self.client = pymongo.MongoClient("mongodb+srv://iflores10:nJnreV9AdMHQoBs7@cluster0.skqqar6.mongodb.net/")  

    # select the database
    self.db = self.client["CampusConnect"] 

    # select the collection
    self.collection = self.db["Clubs"] 

    self.club = ""
    self.contact = ""
    self.title = ""
    self.location = ""
    self.eventinfo = ""
    self.date = ""
    self.time = ""
    self.image_data = None
    
  # setter method for image data
  def set_image(self, image_path):
    with open(image_path, "rb") as image_file:
      self.image_data = base64.b64encode(image_file.read()).decode("utf-8")
      
  # setter method for club
  def set_club(self, club):
    self.club = club
    
    # setter method for eventinfo
  def set_contact(self, contact):
    self.contact = contact
    
  # setter method for title
  def set_title(self, title):
    self.title = title
    
  # setter method for location
  def set_location(self, location):
    self.location = location
    
  # setter method for eventinfo
  def set_eventinfo(self, eventinfo):
    self.eventinfo = eventinfo
    
  # setter method for date
  def set_date(self, date):
    self.date = date
  
  # setter method for time
  def set_time(self, time):
    self.time = time
    
    
  # method to create a new document in the MongoDB collection
  def create_new_document(self):
    # create a new document
    new_document = {
        "club" : self.club,
        "contact" : self.contact,
        "title" : self.title,
        "eventinfo" : self.eventinfo,
        "date" : self.date,
        "time" : self.time,
        "location": self.location,
        "image_data": self.image_data
      }

    # insert the document into the collection
    result = self.collection.insert_one(new_document)
    
class storingPost:

  def __init__(self):
    # connect to MongoDB
    self.client = pymongo.MongoClient("mongodb+srv://iflores10:nJnreV9AdMHQoBs7@cluster0.skqqar6.mongodb.net/")  

    # select the database
    self.db = self.client["CampusConnect"] 

    # select the collection
    self.collection = self.db["post"] 

    self.user = ""
    self.comment = ""
    self.image_data = None
    
  # setter method for image data
  def set_image(self, image_path):
    with open(image_path, "rb") as image_file:
      self.image_data = base64.b64encode(image_file.read()).decode("utf-8")
      
  # setter method for building
  def set_user(self, user):
    self.user = user
    
  # setter method for roomnumber
  def set_comment(self, comment):
    self.comment = comment
    
    
  # method to create a new document in the MongoDB collection
  def create_new_document(self):
    # create a new document
    timestamp = datetime.now()
    new_document = {
        "user": self.user,
        "comment": self.comment,
        "timestamp" : timestamp,
        "image_data": self.image_data
      }

    # insert the document into the collection
    result = self.collection.insert_one(new_document)
    
class storingEvents:

  def __init__(self):
    # connect to MongoDB
    self.client = pymongo.MongoClient("mongodb+srv://iflores10:nJnreV9AdMHQoBs7@cluster0.skqqar6.mongodb.net/")  

    # select the database
    self.db = self.client["CampusConnect"] 

    # select the collection
    self.collection = self.db["events"] 

    self.club = ""
    self.contact = ""
    self.title = ""
    self.location = ""
    self.eventinfo = ""
    self.date = ""
    self.time = ""
    self.image_data = None
    
  # setter method for image data
  def set_image(self, image_path):
    with open(image_path, "rb") as image_file:
      self.image_data = base64.b64encode(image_file.read()).decode("utf-8")
      
  # setter method for club
  def set_club(self, club):
    self.club = club
    
    # setter method for eventinfo
  def set_contact(self, contact):
    self.contact = contact
    
  # setter method for title
  def set_title(self, title):
    self.title = title
    
  # setter method for location
  def set_location(self, location):
    self.location = location
    
  # setter method for eventinfo
  def set_eventinfo(self, eventinfo):
    self.eventinfo = eventinfo
    
  # setter method for date
  def set_date(self, date):
    self.date = date
  
  # setter method for time
  def set_time(self, time):
    self.time = time
    
    
  # method to create a new document in the MongoDB collection
  def create_new_document(self):
    # create a new document
    timestamp = datetime.now()
    
    new_document = {
        "club" : self.club,
        "contact" : self.contact,
        "title" : self.title,
        "eventinfo" : self.eventinfo,
        "date" : self.date,
        "time" : self.time,
        "timestamp" : timestamp,
        "location": self.location,
        "image_data": self.image_data
      }

    # insert the document into the collection
    result = self.collection.insert_one(new_document)
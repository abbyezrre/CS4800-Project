import pymongo
import base64

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
        "bio": self.bio,
        "image_data": self.image_data
      }

    # insert the document into the collection
    result = self.collection.insert_one(new_document)





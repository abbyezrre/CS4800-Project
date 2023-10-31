import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://iflores10:nJnreV9AdMHQoBs7@cluster0.skqqar6.mongodb.net/")  

# Select the database
db = client["CampusConnect"] 

# Select the collection
collection = db["users"] 

firstname = input("First name: ")
lastname = input("Enter Last name: ")
middlename = input("Enter middle: ")
age = input("Enter age: ")
username = input("Whats the username: ")
password = input("password: ")


# Create a new document
new_document = {
  "firstname": firstname,
  "lastname": lastname,
  "middlename":  middlename,
  "username": username,
  "password": password,
  "age": age
}

# Insert the document into the collection
result = collection.insert_one(new_document)

# Print the inserted document's ID
print("Document inserted with ID:", result.inserted_id)

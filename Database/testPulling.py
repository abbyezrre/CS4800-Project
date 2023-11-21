#from pullingUserInfo import pullingUserInfo
#from StoringUserInfo import StoringUserInfo
from StoringUserInfo import storingMap
from pullingUserInfo import pullingMapInfo
from PIL import Image
from io import BytesIO

# USING THE STORING MAP------------------------
map_info = storingMap()

map_info.set_location("B100")
map_info.set_building("Bizzini")
map_info.set_roomnumber("100")
ig = r"C:\Users\abiga\OneDrive\Documents\CS4800\Project\CS4800-Project\bizzini1\b100.png"
map_info.set_image(ig)

# map_info.create_new_document()
# END OF STORING MAP--------------------------

# USING THE PULLMAPINFO------------
user_info = pullingMapInfo()

print(user_info.get_image("B100"))


#Isaac Flores
# START - testing if I am able to pull information fromt he data base


#user_info = pullingUserInfo()

# call the get_firstname method and print the result
# print(user_info.get_firstname("reydub"))
# print(user_info.get_lastname("reydub"))
# print(user_info.get_username("reydub"))
# print(user_info.get_password("reydub"))
# print(user_info.get_age("reydub"))
# print(user_info.get_fullname("reydub"))
# print(user_info.get_bio("reydub"))
# you can insert any other field to return all the data from that field 
# Example: "age" will return a list of all the ages
# print(user_info.get_allFieldInfo("username")) 

# displays the CSU logo Image
#print(user_info.get_image("reydub"))


# # END - pulling from the database



#START - testing if I am able to store/ser information for new user

# # create an instance of the class
#user_info = StoringUserInfo()



# # # set values using setter methods
# user_info.set_firstname(input("First name: "))
# user_info.set_lastname(input("Enter Last name: "))
# user_info.set_middlename(input("Enter middle: "))
# user_info.set_age(input("Enter age: "))
# user_info.set_username(input("Whats the username: "))
# user_info.set_password(input("password: "))
# user_info.set_bio(input("Include in Bio: "))

# # store the directory path of the image
# ig = r"c:\Users\isaac\OneDrive\Documents\CS4800-Project\CampusConnect\static\img\CSU_Stanislaus_seal.svg.png"
# # stores to the database
# user_info.set_image(ig)

# # create a new document with the set values
#user_info.create_new_document()

# # END - storing user

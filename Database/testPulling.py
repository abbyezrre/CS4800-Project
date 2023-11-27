#from pullingUserInfo import pullingUserInfo
#from StoringUserInfo import StoringUserInfo
from StoringUserInfo import storingMap
from pullingUserInfo import pullingMapInfo
from StoringUserInfo import storingClubs
from pullingUserInfo import pullingClubInfo
from StoringUserInfo import *
from pullingUserInfo import *
from PIL import Image
from io import BytesIO


# USING THE Post------------------------
# post_info = storingPost()

# post_info.set_user("isaac")
# post_info.set_comment("hello world")
# ig = r"c:\Users\isaac\OneDrive\Pictures\Screenshots\Gaming-logo.PNG"
# post_info.set_image(ig)

# post_info.create_new_document()
# END OF Post--------------------------

# USING THE PULLMAPINFO------------
# user_info = pullingPostInfo()
# #print(user_info.get_location("DBH 145"))
# print(user_info.get_timestamp("isaac"))
# print(user_info.get_comment("isaac"))
# print(user_info.get_image("isaac"))

# USING THE STORING MAP------------------------
# map_info = storingMap()

# map_info.set_location("check test")
# map_info.set_building("Demergasso-Bava Hall")
# map_info.set_roomnumber("145")
# ig = r"c:\Users\isaac\OneDrive\Documents\CS4800-Project\CampusConnect\static\img\CSU_Stanislaus_seal.svg.png"
# map_info.set_image(ig)

# map_info.create_new_document()
# END OF STORING MAP--------------------------

# USING THE PULLMAPINFO------------
# user_info = pullingMapInfo()
# print(user_info.get_location("DBH 145"))
# print(user_info.get_building("DBH 145"))
# print(user_info.get_roomnumber("DBH 145"))
# print(user_info.get_image("DBH 145"))

# USING THE PULLCLUBINFO
# user_info = storingEvents()
# user_info.set_club("Gaming")
# user_info.set_location("b100")
# user_info.set_date("11/23/23")
# user_info.set_time("7:00pm")
# user_info.set_contact("stanstategaming@gmail.com")
# user_info.set_title("friendgiving")
# info = "Our club is mainly run through a Discord community server, so our membership benefits mostly pertain to receiving permissions to access text channels as well as use bot commands in our server. We use a tier system to give active participants even more benefits and a higher status in the club."
# user_info.set_eventinfo(info)
# ig = r"c:\Users\isaac\OneDrive\Pictures\Screenshots\Gaming-logo.PNG"
# user_info.set_image(ig)

# user_info.create_new_document()
# user_info = pullingClubInfo()
# print(user_info.get_club("cs"))
# print(user_info.get_location("cs"))
# print(user_info.get_date("cs"))
# print(user_info.get_time("cs"))
# print(user_info.get_eventinfo("cs"))
# print(user_info.get_image("cs"))

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

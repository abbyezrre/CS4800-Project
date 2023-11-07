from pullingUserInfo import pullingUserInfo
from StoringUserInfo import StoringUserInfo
from PIL import Image
from io import BytesIO
#Isaac Flores
# START - testing if I am able to pull information fromt he data base


user_info = pullingUserInfo()

# # Call the get_firstname method and print the result
print(user_info.get_firstname("johnsmith209"))
print(user_info.get_lastname("johnsmith209"))
print(user_info.get_username("johnsmith209"))
print(user_info.get_password("johnsmith209"))
print(user_info.get_age("johnsmith209"))
print(user_info.get_fullname("johnsmith209"))

# you can insert any other field to return all the data from that field 
# Example: "age" will return a list of all the ages
print(user_info.get_allFieldInfo("username")) 

# displays the CSU logo Image
print(user_info.get_image("rr"))


# # END - pulling from the database



#START - testing if I am able to store/ser information for new user

# # create an instance of the class
# user_info = StoringUserInfo()
# ig = r"c:\Users\isaac\OneDrive\Documents\CS4800-Project\CampusConnect\static\img\CSU_Stanislaus_seal.svg.png"
# # set values using setter methods
# user_info.set_firstname(input("First name: "))
# user_info.set_lastname(input("Enter Last name: "))
# user_info.set_middlename(input("Enter middle: "))
# user_info.set_age(input("Enter age: "))
# user_info.set_username(input("Whats the username: "))
# user_info.set_password(input("password: "))
# user_info.set_image(ig)

# create a new document with the set values
#user_info.create_new_document()

# # END - storing user

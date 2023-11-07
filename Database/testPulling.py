from pullingUserInfo import pullingUserInfo
from StoringUserInfo import StoringUserInfo
#Isaac Flores
# START - testing if I am able to pull information fromt he data base


# user_info = pullingUserInfo()

# # # Call the get_firstname method and print the result
# print(user_info.get_firstname("abby123"))
# print(user_info.get_lastname("abby123"))
# print(user_info.get_username("abby123"))
# print(user_info.get_password("abby123"))
# print(user_info.get_age("abby123"))
# print(user_info.get_fullname("abby123"))

# END - pulling from the database



#START - testing if I am able to store/ser information for new user

# create an instance of the class
user_info = StoringUserInfo()

# set values using setter methods
user_info.set_firstname(input("First name: "))
user_info.set_lastname(input("Enter Last name: "))
user_info.set_middlename(input("Enter middle: "))
user_info.set_age(input("Enter age: "))
user_info.set_username(input("Whats the username: "))
user_info.set_password(input("password: "))

# create a new document with the set values
user_info.create_new_document()

# # END - storing user

from Database.pullingUserInfo import *

usernameList = pullingUserInfo().get_allFieldInfo('username')
print(usernameList)
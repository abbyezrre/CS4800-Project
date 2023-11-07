If you are looking to use the database class:
    - install pymongo (pip install pymongo) # this is needed to connect with the database (mongodb)
    - instal PIL (pip install pillow) # this is needed to read images

Storing Info:
    - all function should be straight forward when calling the function you'll be able to create a new user
    - ONLY FUNCTION THAT NEEDS EXTRA IS set_image()
        - when trying to store image you need the full directory path of the image
            example: 
            # ig = r"c:\Users\isaac\OneDrive\Documents\CS4800-Project\CampusConnect\static\img\CSU_Stanislaus_seal.svg.png"
            # user_info.set_image(ig)

Pulling Info:
    - all functions are staight forward when pulling from it
    - the only information you need is the users username, from that you can pull any information that this stored under that username
        example:
        #print(user_info.get_firstname("johnsmith209")) ----> John

Test Functions:
    - use testPulling.py to test the storing snd pulling user info from the database

Future Plans:
    - create a seperate collection for the clubs 
        - include images
        - include comments/summary
        - club info
    - create a seperate collection for events 
        - events are only posted by club admins
        - store event infor : images, text (date, time, location)
    - create a seperate collection for map
        - this will mainly be images of the location
    - create a seperate collection for post
        - user can post multiple times
        - post include: images, videos, text
        - keep track of the order
    - create functions to update and delete information of user/admin/post
    - store/pull videos in database

        


from Database.pullingUserInfo import *

class PostingController:
    def __init__(self):
        # instead of creating a new instance of pullingPostInfo, use the existing instance
        self.post = pullingPostInfo()


        # access the collection from the pullingPostInfo instance
        self.collection = self.post.collection


    def get_last_5_documents(self):
        # sort by the timestamp field in descending order and limit to 5 documents
        cursor = self.collection.find().sort("timestamp", pymongo.DESCENDING).limit(5)


        # convert the cursor to a list of documents
        last_5_documents = list(cursor)


        return last_5_documents
   
# just testing it works properly
# # instantiate the PostingController class
# posting_controller = PostingController()


# # call the get_last_5_documents method and print the result
# print(posting_controller.get_last_5_documents())

    

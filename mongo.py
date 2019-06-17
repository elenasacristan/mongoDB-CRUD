
import pymongo
import os
import env

MONGODB_URI = os.environ.get("MONGODB_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

# print(MONGODB_URI)

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

coll.update_many({"first":"pepe"},{"$set":{"first":"pepaaaaaaaaaaaa"}})
documents = coll.find()

for doc in documents:
    print(doc)
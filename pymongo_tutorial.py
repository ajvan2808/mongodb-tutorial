from pymongo import MongoClient
import pprint


'''
Create MongoClient instance to establish a connection to database. 
This class provides a client for a MongoDB instance or server. 
Each client object has a built-in connection pool, which by default handles up to a hundred connections to the server.
'''

client = MongoClient()
# >>> client
# MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)

'''
MongoClient takes a set of arguments that allows you to specify custom host, port, and other connection parameters
'''
# client1 = MongoClient(host='localhost', port=27017)
# client2 = MongoClient('mongodb://localhost:27017')  # You can also use the MongoDB URI format


''' Working With Databases, Collections, and Documents '''
# Once you have a connected instance of MongoClient, you can access any database managed by the specified MongoDB server
# When you use the mongo shell, you have access to the database through the db global object.
# When you use PyMongo, you can assign the database to a variable called db to get similar behavior.

# If the database doesn’t exist, then MongoDB creates it for you, but only when you perform the first operation on the database.
db = client.tutorial
# >>> db
# Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'tutorial')

# Or dictionary-style access
# db1 = client1["temp-tutorial"]

#   Data
data0 = {
    "title": "Reading and Writing CSV Files in Python",
    "author": "Jon",
    "contributors": [
        "Aldren",
        "Geir Arne",
        "Joanna",
        "Jason"
    ],
    "url": "https://realpython.com/python-csv/"
}

data1 = {
    "title": "How to Iterate Through a Dictionary in Python",
    "author": "Leodanis",
    "contributors": [
        "Aldren",
        "Jim",
        "Joanna"
    ],
    "url": "https://realpython.com/iterate-through-dictionary-python/"
}

data2 = {
     "title": "Python 3's f-Strings: An Improved String Formatting Syntax",
     "author": "Joanna",
     "contributors": [
         "Adriana",
         "David",
         "Dan",
         "Jim",
         "Pavel"
     ],
     "url": "https://realpython.com/python-f-strings/"
}

''' INSERT DOCUMENTS TO COLLECTION  '''
# specify which collection to use
tutorial = db.tutorial
# print(tutorial)
# doc0 = tutorial.insert_one(data0)
# print(doc0) -> InsertOneResult(ObjectId('6582a33d0ad99e16359e9aa7'), acknowledged=True)
# print(doc0.inserted_id)

# docs = tutorial.insert_many([data1, data2])
# print(f"Ids of multiple documents: {docs.inserted_ids}")


''' RETRIEVING DOCUMENTS
Use .find()
Without arguments, .find() returns a Cursor object that yields the documents in the collection on demand
'''

for doc in tutorial.find():
    pprint.pprint(doc)

one_record = tutorial.find_one({'author': 'Jon'})
# current db having duplicates due to data insertion from CLI and here.
# As MongoDB perform ordered insert find_one() return 1st document inserted.
print(one_record)
print(tutorial.count_documents({}))


''' CLOSING CONNECTION  '''
# Close the connection by calling .close() on the MongoClient instance
client.close()

# OR using context manager
with MongoClient() as client:
    db = client.tutorial
    for doc in db.tutorial.find():
        pprint.pprint(doc)

    # the client’s .__exit__() method gets called

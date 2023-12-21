from mongoengine import connect, disconnect
from mongoengine import Document, ListField, StringField, URLField

''' ESTABLISH CONNECTION '''
# You can assign a variable for the connection then call .close() once finished else:
# Note: close() does not actually remove the connection from MongoEngine's connection list.
# This causes problems when trying to connect to a different database later on.
connect(db='tutorial', host='localhost', port=27017, alias='db')


''' CREATE MODEL/ SCHEMA '''


# To create a model, you need to subclass Document and provide the required fields as class attributes.
# The base class, Document, uses information along with the field types to validate the input data
class Tutorial(Document):
    title = StringField(required=True, max_length=70)
    author = StringField(required=True, max_length=50)
    contributors = ListField(StringField(max_length=50))
    url = URLField(required=True)


''' WORKING WITH DB '''
# To save a document to database, you need to call .save() on a document object.
# If the document already exists, then all the changes will be applied to the existing document.
# If the document does not exist, then it’ll be created.
tutorial1 = Tutorial(
    title="Beautiful Soup: Build a Web Scraper With Python",
    author="Martin",
    contributors=["Aldren", "Geir Arne", "Jaya", "Joanna", "Mike"],
    url="https://realpython.com/beautiful-soup-web-scraper-python/"
)

# Insert the new data. PyMongo performs data validation and raise exception if it violates the schema
tutorial1.save()

tutorial2 = Tutorial()
tutorial2.title = 222
tutorial2.save()
# mongoengine.errors.ValidationError: ValidationError (Tutorial:None) (StringField only accepts string values: ['title'] Field is required: ['author', 'url'])


# Each Document subclass has an .objects attribute
# that you can use to access the documents in the associated collection
for doc in Tutorial.objects:
    print(doc.title)

# you can also filter your documents
for doc in Tutorial.objects(author="Alex"):
    print(doc.title)

''' DISCONNECT '''
disconnect(alias='db')

# user: read&write any db
username = "utoivfqam"
password = "dhgfdhgQWS234"

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = 'mongodb+srv://utoivfqam:dhgfdhgQWS234@basic.xooz2jh.mongodb.net/?retryWrites=true&w=majority&appName=basic'

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

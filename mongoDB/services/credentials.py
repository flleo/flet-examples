from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

basic_uri = "mongodb+srv://ravelo:yCScT0c5liVYCmbv@basic.xooz2jh.mongodb.net/?retryWrites=true&w=majority&appName=basic"
client = MongoClient(basic_uri, server_api=ServerApi('1'))


def deb_names():
    for db_name in client.list_database_names():
        print(db_name)


# Send a ping to confirm a successful connection
def ping():
    # Create a new client and connect to the server
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

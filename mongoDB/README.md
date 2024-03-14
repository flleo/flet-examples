# mongoDB operations in Python

## En raiz del proyecto, si creamos entorno virtual
<pre>py -m venv ./.venv
echo '.venv'>>.gitignore
</pre>

### Run the following on OSX & Linux to acitvate it:
<pre>
source ./.venv/bin/activate
</pre>

https://cloud.mongodb.com/v2/65f2cf7c73b7ce34221d868f#/overview

## Application Development
Python

Get connection string


### Install driver
<pre>
python -m pip install "pymongo[srv]"
</pre>
https://www.mongodb.com/docs/drivers/python-drivers/
Realice el curso en línea gratuito impartido por MongoDB
https://learn.mongodb.com/learning-paths/using-mongodb-with-python?_ga=2.69660112.1588606114.1710193427-136387887.1710193426
### Certifications
https://learn.mongodb.com/courses/mongodb-associate-developer-exam-python

### Connecting to MongoDB in Python
https://learn.mongodb.com/learn/course/connecting-to-mongodb-in-python/lesson-2-connecting-to-an-atlas-cluster-in-python-applications/first-lesson?client=customer

#### Add your connection string into your application code

### Basic operations
- Set up your MongoDB instance
- Create a user
- Allow an IP address
- Connect to your database


credentials.py
<pre>
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
</pre>
run
<pre>
/media/work/python/flet/examples/.venv/bin/python /media/work/python/flet/examples/mongoDB/credentials.py 
Pinged your deployment. You successfully connected to MongoDB!

Process finished with exit code 0
</pre>










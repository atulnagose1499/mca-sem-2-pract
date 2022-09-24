# pip install pymongo

import pymongo
connection_url="mongodb://localhost:27017/"
client=pymongo.MongoClient(connection_url)
client.list_database_names()

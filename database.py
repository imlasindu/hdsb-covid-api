import pymongo
import os

# Initialize MongoDB
MONGODB_URI = os.getenv('MONGODB_URI')
client = pymongo.MongoClient(MONGODB_URI)
db = client['Cluster0']
collection = db['data']


def insert_into_db(date: str, data: dict):
    '''Inserts data from a specific date into the database.'''
    if not collection.find_one({'date': date}):
        document = {
            'date': date,
            'data': data
        }
        collection.insert_one(document)
    quit()

def find_from_db(date: str = ''):
    '''Finds either all data, or data from a specific date from the database.'''
    if not date:
        return collection.find()
    return collection.find_one({'date': date})
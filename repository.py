import pymongo
from pymongo import MongoClient

def get_connection():
    return MongoClient('localhost', 27017)['gitnomic']

def find_user (username):
    db = get_connection()
    userDB = db.users
    return userDB.find_one({"_id":username})
    
    
if __name__ == '__main__':
    #tests
    user = find_user('forrest')
    print user['points']

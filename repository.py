import pymongo
from pymongo import MongoClient


def find_user (username):
    db = MongoClient('localhost', 27017)['gitnomic'];
    userDB = db.users
    return userDB.find_one({"_id":username})
    
    
if __name__ == '__main__':
    #tests
    user = find_user('forrest')
    print user['points']

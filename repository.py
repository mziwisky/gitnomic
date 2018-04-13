import pymongo
from pymongo import MongoClient

def get_connection():
    return MongoClient('localhost', 27017)['gitnomic']

def find_user (username):
    db = get_connection()
    userDB = db.users
    return userDB.find_one({"_id": username})

def add_points(username, points):
  #Adds the specified number of points to a player.
  #If the player doesnt exist, adds them with the specified points
  db = get_connection()
  userDB = db.users
  return userDB.update_one({"_id" : username}, {"$inc" : {"points" : points}}, upsert=True)
  
def get_game_state():
  #Gets the gamestate object from the db
  db = get_connection()
  gameDB = db.game
  return gameDB.find_one({"_id" : "gameState"})
  
def advance_round(new_current_player):
  #set a new current player and increment the turn counter
  db = get_connection()
  gameDB = db.game
  gameDB.update_one({"_id" : "gameState"}, 
                    {"$set" : {"currentPlayer" : new_current_player}, "$inc" : {"currentRound" : 1}})

def init_db(first_player):
  db = get_connection()
  gameDB = db.game
  gameDB.insert_one({"_id" : "gameState", 
                     "currentPlayer" : first_player,
                    "currentRound" : 0})

if __name__ == '__main__':
    #tests
    user = find_user('forrest')
    print(user['points'])

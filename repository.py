import pymongo
from pymongo import MongoClient
import json

def get_connection():
    return MongoClient('localhost', 27017)['gitnomic']
  
def get_config():
  with open('config.json') as config_file:
    conf = json.load(config_file)
  return conf
  
def set_config(new_config):
  with open('config.json', 'w') as config_file:
    json.dump(new_config, config_file)

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

def get_current_player():
  #Gets the player whose turn it is
  state = get_game_state()
  return state['currentPlayer']
  
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

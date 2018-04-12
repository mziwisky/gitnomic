import git_repo
import server
import repository
from multiprocessing import Process
import subprocess
import time
import os
import random

#Contains essential game logic. 

def wins(user):
  if user.points > 200:
    return True
  else:
    return False

def is_approved(yay, nay, total):
  #Initially, all pull requests must be approved unanimously
  if yay < total:
    return False
  return True

def assign_points(votes, players, pull):
  

def resolve_round():
  #get the pull requests
  pulls = git_repo.get_pulls()
  players = git_repo.get_players()
  current_player = repository.get_current_player()
  for pull in pulls:
    if pull['user']['login'] == current_player:
      votes = git_repo.get_votes(pull['number'])
      #We approve all 
      if is_approved(len(votes[0]), len(votes[1]), len(players)):
        #Assign points and merge
        assign_points(votes, players, pull)
        #When we merge a pull we quit immediately
        break;

def play_round():
  #Start the game server
  game_server = Process(target = server.start_server)
  game_server.start()
  #Wait until the end of the round
  time.sleep(604800) #1 week
  #End the server
  game_server.terminate()
  #Finish the round
  resolve_round()
  
def init_game():
  #Sets up the game environment in case weve never been run before.
  #Also a good place to put commands which should only be run once
  pass

  
if __name__ == '__main__':
  #Start the database
  database_process = subprocess.Popen(["mondgod"])  
  #Do first time setup/onetime commands
  init_game()
  #START THE GAME
  play_round()
  
  #Rounds over. Clean up time.
  #Stop the db
  database_process.terminate()
  #Return and exit for restart.
  return 0

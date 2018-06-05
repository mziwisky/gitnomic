import git_repo
import server
import repository
from multiprocessing import Process
import subprocess
import time
import os
import random
import math

#Contains essential game logic. 

def wins(user):
  if user.points > 200:
    return True
  else:
    return False

def is_approved(yay, nay, total):
  #203. A rule-change is adopted if and only if the vote is unanimous among the eligible voters. If this rule is not amended by the end of the [fith round], it automatically changes to require only a simple majority.
  #105. Every player is an eligible voter. Every eligible voter must participate in every vote on rule-changes.
  round = repository.get_game_state()["currentRound"]
  if round < 10:
    #unanimous, since players cant vote on their own proposals
    if yay < total - 1:
      return False
    return True
  else:
    #simple majority, and every player voted besides the proposer.
    if yay <= nay and yay + nay == total -1:
      return False
    return True
  
def pick_next_player(players, current=None):
  #201. Players shall alternate in alphabetical order by [username].
  players.sort()
  if not current:
    return players[0]
  for i in range(len(players)):
    if players[i] == current:
      if i == len(players)-1:
        return players[0]
      else:
        return players[i+1]


def assign_points(votes, players, pull, approved):
  #assign points based on votes
  #206. When a proposed rule-change is defeated, the player who proposed it loses 10 points.
  current = pull['user']['login']
  if not approved:
    repository.add_points(current, -10)
  else:
    #201. A number between 0 and 10 for the first player, with the upper limit increasing by one each turn; more points are awarded for more popular proposals.
    round = repository.get_game_state()["currentRound"]
    round = round + 9
    approval_rate = float(len(votes[0]))/float(len(votes[0]) + len(votes[1]))
    points = math.ceil(round * approval_rate)
    repository.add_points(current, points)
    #204. If and when rule-changes can be adopted without unanimity, the players who vote against winning proposals shall receive 10 points each.
    for nay in votes[1]:
      repository.add_points(nay, 10)

def resolve_round():
  #get the pull requests
  pulls = git_repo.get_pulls()
  players = git_repo.get_players()
  current_player = repository.get_current_player()
  for pull in pulls:
    #If a player has multiple proposals, we pick the first one
    if pull['user']['login'] == current_player:
      votes = git_repo.get_votes(pull['number'])
      #We approve all 
      if is_approved(len(votes[0]), len(votes[1]), len(players)):
        #Assign points and merge
        assign_points(votes, players, pull, True)
        git_repo.merge(pull)
      else:
        #Assing points and close
        assign_points(votes, players, pull, False)
        git_repo.close(pull)
	#Only one pull request per player per round.
    break;
  #get the next player and advance the round
  next_player = pick_next_player(players, current_player)
  repository.advance_round(next_player)
  
def init_game():
  #Sets up the game environment.
  #Also a good place to put commands which should only be run once.
  config = repository.get_config()
  os.environ["GITHUB_USERNAME"] = config["git_login"]
  os.environ["GITHUB_REPO"] = config["git_repo"]
  os.environ["GITHUB_PASS"] = config["git_password"]
  if not "db_setup" in config:
    players = git_repo.get_players()
    player1 = pick_next_player(players)
    repository.init_db(player1)
    #Save that weve set up the db
    config['db_setup'] = "complete"
    repository.set_config(config)
  
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
  
if __name__ == '__main__':
  #Start the database
  database_process = subprocess.Popen(["mongod"])
  #give the database a chance to start up
  time.sleep(5)
  #Do first time setup/onetime commands
  init_game()
  #START THE GAME
  play_round()
  
  #Rounds over. Clean up time.
  #Stop the db
  database_process.terminate()
  sleep(5)

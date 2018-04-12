import os
import requests
import json


def get_auth():
  return (os.environ.get('GITHUB_USERNAME'), os.environ.get("GITHUB_PASS"))

def get_pulls():
  url = "https://api.github.com/repos/" + os.environ.get("GITHUB_USERNAME") + "/" + os.environ.get("GITHUB_REPO") + "/pulls"
  auth = get_auth()
  response = json.loads(requests.get(url, auth=get_auth()))
  return response

def get_players():
  url = "https://api.github.com/repos/" + os.environ.get("GITHUB_USERNAME") + "/" + os.environ.get("GITHUB_REPO") + "/contributors"
  response = requests.get(url, auth=get_auth())
  player_data = json.loads(response.text)
  players = []
  for player in player_data:
    players.append(player['login'])
  return players

def get_votes(pull_id):
  url = "https://api.github.com/repos/" + 
    os.environ.get("GITHUB_USERNAME") + "/" + 
    os.environ.get("GITHUB_REPO") + "/pulls/" +
    pull_id + "/reviews"
  response = requests.get(url, auth=get_auth())
  approved = []
  rejected = []
  for review in json.loads(response.text):
    if review['state'] == "APPROVED":
      approved.append(review)
    else:
      rejected.append(review)
  return (approved, rejected)

def merge(pull):
  url = "https://api.github.com/repos/" + 
    os.environ.get("GITHUB_USERNAME") + "/" + 
    os.environ.get("GITHUB_REPO") + "/pulls/" + 
    pull['number'] + "/merge"
  response = requests.put(url, auth=get_auth(), data={})
  if response.status_code == 200:
    #merge was successful
    return True
  else:
    #Something went wrong. Oh well.
    return False
  
def close(pull):
  url = "https://api.github.com/repos/" + 
    os.environ.get("GITHUB_USERNAME") + "/" + 
    os.environ.get("GITHUB_REPO") + "/pulls/" + 
    pull['number']
  payload = {"state" : "closed"}
  requests.put(url, auth=get_auth(), data=payload)
  if response.status_code == 200:
    #close was successful
    return True
  else:
    #Something went wrong. Oh well.
    return False
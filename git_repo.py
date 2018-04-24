import os
import requests
import json
import repository


def get_auth():
  return (os.environ.get('GITHUB_USERNAME'), os.environ.get("GITHUB_PASS"))

def get_pulls():
  url = "https://api.github.com/repos/{}/{}/pulls".format(os.environ.get("GITHUB_USERNAME"), os.environ.get("GITHUB_REPO"))
  auth = get_auth()
  response = json.loads(requests.get(url, auth=get_auth()).text)
  return response

def get_players():
<<<<<<< HEAD
  url = "https://api.github.com/repos/{}/{}/collaborators".format(os.environ.get("GITHUB_USERNAME"), os.environ.get("GITHUB_REPO"))
=======
  url = "https://api.github.com/repos/{}/{}/contributors".format(os.environ.get("GITHUB_USERNAME"), os.environ.get("GITHUB_REPO"))
>>>>>>> 95764e37082e7fe8aa03554d3f5315262bb2e5ef
  response = requests.get(url, auth=get_auth())
  player_data = json.loads(response.text)
  players = []
  for player in player_data:
    if player['login'] != os.environ.get("GITHUB_USERNAME"):
      players.append(player['login'])
  return players

def get_votes(pull_id):
  url = "https://api.github.com/repos/{}/{}/pulls/{}/reviews".format(os.environ.get("GITHUB_USERNAME"), os.environ.get("GITHUB_REPO"), pull_id)
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
  url = "https://api.github.com/repos/{}/{}/pulls/{}/merge".format(os.environ.get("GITHUB_USERNAME"), os.environ.get("GITHUB_REPO"), pull['number'])
  response = requests.put(url, auth=get_auth(), data={})
  if response.status_code == 200:
    #Merge was successful
    return True
  else:
    #Something went wrong. Oh well.
    return response.status_code
  
def close(pull):
  url = "https://api.github.com/repos/{}/{}/pulls/{}".format(os.environ.get("GITHUB_USERNAME"), os.environ.get("GITHUB_REPO"), pull['number'])
  payload = {"state" : "closed"}
  response = requests.post(url, auth=get_auth(), data=json.dumps(payload))
  if response.status_code == 200:
    #Close was successful
    return True
  else:
    #Something went wrong. Oh well.
    return response.text
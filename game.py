import git_repo
#Contains essential game logic. 

def is_winner(user):
    if user.points > 100:
        return True
    else:
        return False

def 

def resolve_round():
    #get current player
    current_player = 'kelpycreek'
    #find current players pull request
    pulls = git_repo.get_pulls()
    #approve/disapprove pull request
    #assign points
    #if approved, restart server

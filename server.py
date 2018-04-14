from flask import Flask
import repository

app = Flask(__name__)

def start_server(main=False):
  app.run(threaded=True, host="0.0.0.0", port=80, debug=not main, use_reloader=main)

@app.route('/')
def hello_world():
  return "Current player: " + repository.get_current_player()
    
@app.route('/score/<username>')
def getScore(username):
  print(username)
  return str(repository.find_user(username)['points'])

if __name__ == '__main__':
  start_server(True)
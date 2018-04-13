from flask import Flask
import repository

app = Flask(__name__)

def start_server(main=False):
  app.run(threaded=True, debug=not main, use_reloader=main)

@app.route('/')
def hello_world():
  return 'Hello World!'
    
@app.route('/score/<username>')
def getScore(username):
  print(username)
  return str(repository.find_user(username)['points'])

if __name__ == '__main__':
  start_server(True)
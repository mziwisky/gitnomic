from flask import Flask
import repository
import scheduler

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route('/score/<username>')
def getScore(username):
    print username
    return str(repository.find_user(username)['points'])

if __name__ == '__main__':
    scheduler.init_scheduler(repository.get_connection())
    app.run()

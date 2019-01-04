from flask import Flask
from redis import Redis
 
app = Flask(__name__)
redis = Redis(host='redis', port=6379)
 
@app.route('/')
def hello():
    count = redis.incr('hits')
    return '<b>You have successfully completed the concept of docker-compose!</b><br><br>Did you learn any new cool things here?<br><br>You came and clicked this page for  {} times.\n'.format(count)
 
if __name__ == "__main__":
    app.run(host="18.212.103.158", debug=True)

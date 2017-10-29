from flask import Flask, render_template
from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client.test
users = db.users
user = {'firs_name': 'Gleb',
        'last_name': 'Evdokimov',
        'email': 'Romissevd@gmail.com',
        }
db.users.save(user)

app = Flask(__name__)

@app.route('/')
@app.route('/<username>/')
def hello_world(username=None):
    user = db.users.find_one({'firs_name': 'Ivan'})
    print(user)

    return render_template('hello.html', name=user.get('last_name'))

if __name__ == '__main__':
    app.debug = True
    app.run()

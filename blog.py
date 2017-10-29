__author__ = 'Roman Evdokimov'
__email__ = 'Romissevd@gmail.com'

from flask import Flask, render_template, request
from data_base import db

DEBUG = True

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('base.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/admin/', methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        log = request.form.get('login')
        passwd = request.form.get('password')

        if list(db.admins.find({'password': passwd, 'login': log})):
            return render_template('admin.html')
        else:
            return render_template('base.html')
    else:
        return render_template('base.html')


if __name__ == '__main__':

    app.run(debug=DEBUG)

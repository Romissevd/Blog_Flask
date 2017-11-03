__author__ = 'Roman Evdokimov'
__email__ = 'Romissevd@gmail.com'

from flask import Flask, render_template, request, redirect, session
from data_base import db

DEBUG = True
# HOST = '0.0.0.0'

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('start.html', posts=db.post.find())


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
            return render_template('login.html',
                                   error='the administrator name or password was not entered correctly')
    else:
        return redirect('/')


@app.route('/admin/add/', methods=['GET'])
def post_add():
    return render_template('post_add.html')


@app.route('/admin/added/', methods=['POST'])
def add():
    new_post = {
        'post_title':request.form.get('post_title'),
        'post_text': request.form.get('post'),
    }
    db.post.save(new_post)
    return  redirect('/')


if __name__ == '__main__':

    app.run(debug=DEBUG)

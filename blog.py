__author__ = 'Roman Evdokimov'
__email__ = 'Romissevd@gmail.com'

from flask import Flask, render_template, request, redirect
from data_base import db
from datetime import datetime

DEBUG = True
# HOST = '0.0.0.0'

app = Flask(__name__)


@app.route('/')
def start():
    if db.posts.find():
        posts = db.posts.find().sort([('post_time', -1)])
        return render_template('start.html', posts=posts)
    return render_template('start.html')


@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        log = request.form.get('login')
        passwd = request.form.get('password')

        if list(db.admins.find({'password': passwd, 'login': log})):
            return redirect('/admin/')
        else:
            return render_template('login.html',
                                   error='the administrator name or password was not entered correctly')
    else:
        return render_template('login.html')


@app.route('/admin/')
def login_admin():
    if db.posts.find():
        posts = db.posts.find().sort([('post_time', -1)])
        return render_template('admin.html', posts=posts)
    return render_template('admin.html')
    # if request.method == 'POST':
    #     log = request.form.get('login')
    #     passwd = request.form.get('password')
    #
    #     if list(db.admins.find({'password': passwd, 'login': log})):
    #         if db.posts.find():
    #             posts = db.posts.find().sort([('post_time', -1)])
    #             return render_template('admin.html', posts=posts)
    #         return render_template('admin.html')
    #     else:
    #         return render_template('login.html',
    #                                error='the administrator name or password was not entered correctly')
    # else:
    #     return redirect('/')
    return render_template('admin.html')

@app.route('/admin/add/', methods=['GET'])
def post_add():
    return render_template('post_add.html')


@app.route('/admin/added/', methods=['POST'])
def add():
    new_post = {
        'post_title':request.form.get('post_title'),
        'post_text': request.form.get('post'),
        'post_time': datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S'),
    }
    db.posts.save(new_post)
    return  redirect('/')


if __name__ == '__main__':

    app.run(debug=DEBUG)

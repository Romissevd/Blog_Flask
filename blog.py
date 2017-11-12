__author__ = 'Roman Evdokimov'
__email__ = 'Romissevd@gmail.com'

from flask import Flask, render_template, request, redirect, session
from data_base import db
from datetime import datetime
from bson.objectid import ObjectId

DEBUG = True
# HOST = '0.0.0.0'
ADMIN_NAME = 'admin'
ADMIN_PASSWORD = 'admin'

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.template_filter('comment_count')
def comment_count(comment, post_id):
    return db.comments.count({'post': ObjectId("{}".format(post_id))})

@app.template_filter('comment_find')
def comment_count(comment, post_id):
    return db.comments.find({'post': ObjectId("{}".format(post_id))}).sort([('comment_time', -1)])
#
#
# app.add_template_filter(comment_count)


@app.route('/')
def start():
    if db.posts.find():
        posts = db.posts.find().sort([('post_time', -1)])
        comments = db.comments.find()
        return render_template('start.html', posts=posts, comments=comments)
    return render_template('start.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        log = request.form.get('login')
        passwd = request.form.get('password')

        if log == ADMIN_NAME and passwd == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect('/admin/')
        else:
            return render_template('login.html',
                                   error='The administrator name or password'
                                         ' was not entered correctly')
    else:
        return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    return redirect('/')


@app.route('/admin/')
def login_admin():
    if not session.get('logged_in'):
        return redirect('/')
    # при входе нужно наименование статей сделать ссылками, чтобы переходили либо на id в доменном имени
    # http://127.0.0.1:5000/59fcdadd366a492d8a9e37fc, либо переводить название на английские буквы,
    # http://127.0.0.1:5000/nasha_statya
    if db.posts.find():
        posts = db.posts.find().sort([('post_time', -1)])
        return render_template('admin.html', posts=posts)
    return render_template('admin.html')


@app.route('/admin/add/', methods=['GET', 'POST'])
def post_add():
    if not session.get('logged_in'):
        return redirect('/')
    if request.method == 'GET':
        return render_template('post_add.html')
    elif request.method == 'POST':
        new_post = {
            'post_title': request.form.get('post_title'),
            'post_text': request.form.get('post'),
            'post_time': datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S'),
        }
        db.posts.save(new_post)
    return redirect('/admin/')


@app.route('/post/<id_post>/', methods=['GET', 'POST'])
def post(id_post):
    if request.method == 'POST':
        new_comment = {
            'comment_username': request.form.get('username'),
            'comment_text': request.form.get('comment'),
            'comment_time': datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S'),
            'post': ObjectId("{}".format(request.form.get('id'))),
            }
        db.comments.save(new_comment)
        return redirect('/')
    else:
        poster = db.posts.find({'_id': ObjectId("{}".format(id_post))})
        comments = db.comments.find()
        return render_template('post.html', poster=poster, comments=comments)


if __name__ == '__main__':

    app.run(debug=DEBUG)

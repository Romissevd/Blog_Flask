from flask import Flask, render_template, request
from data_base import db



app = Flask(__name__)




#
#
# @app.route('/admin/')
# def admin():
#     return render_template('admin.html')
#
#
# @app.route('/hello/', methods=['GET', 'POST'])
# def start():
#     if request.method == 'POST':
#         print(request.form)
#         return render_template('base.html')

app.run()

# if __name__ == '__main__':
#
#     app.run(debug = True)

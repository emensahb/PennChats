from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app.models import Student,

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql +psycopg2://postgres:pbNdO#cdxtskP7Da9d7@@localhost/pennchats'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False


@app.route('/')
def penn_chats():
    return 'Welcome to Penn Chats'

#for profile route
@app.route('/profile')
def penn_chats():
    return 'Welcome to Penn Chats'

#for processing profile route
@app.route('/process', methods = ['POST'])
def process():
    name = request.form['name']
    email = request.form['email']

    return redirect(url_for('index.html'))


@app.route("/name/<name>")
def get_user_name(name):
    return "name : {}".format(name)

if __name__ == '__main__':
    app.run()

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
 #   print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

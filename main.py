import os
from flask import Flask, render_template, request, redirect, url_for
from forms import SignUpForm
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pbNdO#cdxtskP7Da9d7@@localhost/pennchats'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)
#migrate = Migrate(app, db)



# home page
@app.route('/')
def penn_chats():
    return render_template("home.html")

# dummy signup page
@app.route('/signup', methods=["POST", "GET"])
def signup():
    form = SignUpForm()
    return render_template("signup.html", form = form)

# dummy login page
@app.route('/login', methods=["POST", "GET"])
def login():
    form = SignUpForm()
    return render_template("login.html", form = form)

# example profile page
@app.route('/create_profile')
def create_profile():
    form = SignUpForm()
    return render_template("create_profile.html", form = form)



@app.route("/name/<name>")
def get_user_name(name):
    return "name : {}".format(name)

if __name__ == '__main__':
    app.run()

# check pull request - Audra

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

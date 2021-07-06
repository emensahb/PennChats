import os
from flask import Flask, render_template, request, redirect, url_for
from forms import SignUpForm
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pbNdO#cdxtskP7Da9d7@@localhost/pennchats'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

@app.route('/')
def penn_chats():
    # get student's first name from Google Authenticate
    # student_name = from google authenticate.name  or something like that
    # return render_template("home.html", current_student = student_name)
    return render_template("home.html")


# example profile page
@app.route('/profile')
def test_profile():
    return render_template("profile.html")


# example login (registered user main screen) page
@app.route('/login')
def test_login():
    return render_template("login.html")


@app.route('/process_login')
def test_login():
    email = request.form['email']
    password = request.form['password']
    return redirect(url_for("home.html"))


@app.route('/signup', methods=["POST", "GET"])
def signup():
    """
    Handle requests to the /signup route
    Adds a student to the database through the sign up form
    """
    form = SignUpForm()
    if form.validate_on_submit():
        student = Student(firstname=form.firstname.data,
                          lastname=form.lastname.data,
                          email=form.email.data,
                          city=form.city.data,
                          state=form.state.data,
                          country=form.country.data,
                          bio=form.bio.data,
                          cohort=form.cohort.data,
                          linkedin=form.linkedin.data
                          )
    return render_template("signup.html", form=form)


# example matches page
@app.route('/matches')
def test_matches():
    return render_template("matches.html")


# for profile route
@app.route('/profile')
def penn_chats():
    return 'Welcome to Penn Chats'


@app.route("/name/<name>")
def get_user_name(name):
    return "name : {}".format(name)


if __name__ == '__main__':
    app.run()

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
 #   print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

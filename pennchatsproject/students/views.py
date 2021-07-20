# pennchatsproject/students/views.py
# contains routing code for eight views
# register, login, logout, sign-up for next week's chat, thank you, account, edit profile, <username> profile page
# from Audra's main.py file lines 12-44

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from pennchatsproject import db
#from werkzeug.security import generate_password_hash, check_password_hash
from pennchatsproject.models import Student
from pennchatsproject.students.forms import RegistrationForm, LoginForm


students = Blueprint('students', __name__)

#register
@students.route('/register', methods=["POST", "GET"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        student = Student(email=form.email.data,
                    username=form.username.data,
                    student_id=form.student_id.data,
                    password=form.password.data)

        db.session.add(student)
        db.session.commit()
        flash('Thank you for registering!')
        return redirect(url_for('students.login'))

    return render_template("register.html", form = form)

#login
@students.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Grab the student from our Student Models table
        student = Student.query.filter_by(email=form.email.data).first()

        if student.check_password(form.password.data) and student is not None:

            #log in the user by calling in the login_user method
            login_user(student)

            #flash a msg with the following message
            flash('You have logged in successfully!')

            # if a user was trying to visit a page that requires a log, flask saves that URL as 'next'
            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)

    return render_template("login.html", form = form)

#logout
@students.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out.")
    return redirect(url_for('core.index'))


# #sign up-for next week's chat
@students.route('/next_week')
def next_week():
    form = RegistrationForm()
    return render_template("next_week.html", form = form)

#thank you
@students.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

#account
@students.route('/account')
def account():
    return render_template("account.html")

#logout
@students.route('/logout_message')
def logout_message():
    return render_template("logout.html")
#
# #edit profile
# @students.route('/account/<name>')
# def edit_profile(name):
#     return 'edit profile'
#
# #<username> profile page
# @students.route("/name/<name>")
# def get_user_name(name):
#     return render_template("get_user_name.html", name = name)

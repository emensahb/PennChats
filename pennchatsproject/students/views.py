# pennchatsproject/students/views.py
# contains routing code for eight views
# register, login, logout, sign-up for next week's chat, thank you, account, edit profile, <username> profile page

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from pennchatsproject import db
# from werkzeug.security import generate_password_hash, check_password_hash
from pennchatsproject.models import *
from pennchatsproject.students.forms import *
# from pennchatsproject.students.picture_handler import add_profile_pic


students = Blueprint('students', __name__)


# register
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

    return render_template("register.html", form=form)

# login
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
            if next == None or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)

    return render_template("login.html", form=form)

# logout
@students.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out.")
    return redirect(url_for('core.index'))

# update profile page
@students.route('/edit_profile', methods=["POST", "GET"])
@login_required
def edit_profile():
    form = ProfileForm()

    if form.validate_on_submit():
        # print(form)

        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.city = form.city.data
        current_user.state = form.state.data
        current_user.country = form.country.data
        current_user.linkedin = form.linkedin.data
        current_user.bio = form.bio.data
        current_user.current_courses = form.current_courses.data
        current_user.past_courses = form.past_courses.data
        current_user.course_id_to_match = form.course_id_to_match.data
        current_user.interests = form.interests.data
        current_user.interest_id_to_match = form.interest_id_to_match.data
        current_user.cohort = form.cohort.data

        db.session.commit()
        flash('Profile Updated')
        return redirect(url_for('students.account'))

    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.city.data = current_user.city
        form.state.data = current_user.state
        form.country.data = current_user.country
        form.linkedin.data = current_user.linkedin
        form.bio.data = current_user.bio
        form.current_courses.data = current_user.current_courses
        form.past_courses.data = current_user.past_courses
        form.course_id_to_match.data = current_user.course_id_to_match
        form.interests.data = current_user.interests
        form.interest_id_to_match.data = current_user.interest_id_to_match
        form.cohort.data = current_user.cohort

    return render_template('edit_profile.html', form=form)

# sign up-for next week's chat
@students.route('/sign_up', methods=["POST", "GET"])
@login_required
def sign_up():
    form = WeeklySignUpForm()

    if form.validate_on_submit():

        form = WeeklySignUp(week_meet=form.week_meet.data,
                            student_id=current_user.student_id,
                            prime_time_id=form.prime_time_id.data,
                            sec_time_id=form.sec_time_id.data,
                            prime_networking_goal_id=form.prime_networking_goal_id.data,
                            sec_networking_goal_id=form.sec_networking_goal_id.data,
                            )

        db.session.add(form)
        db.session.commit()
        flash('Signup Form Submitted')
        return redirect(url_for('students.thank_you'))

    return render_template("weekly_signup.html", form=form)

# thank you
@students.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

# account
@students.route('/account')
@login_required
def member_area():
    return render_template("account.html")
#
# # <username> profile page
# @students.route("/name/<name>")
# def get_user_name(name):
#     return render_template("get_user_name.html", name = name)

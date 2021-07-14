# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship

# from app import db

# A side note. Table and class names camel case. Field names with the dashes
# import os
# from flask import Flask, render_template, request, redirect, url_for
# from students.forms import *
# from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from models import *

# basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pbNdO#cdxtskP7Da9d7@@localhost/pennchats'
# app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


class Student(db.Model):
    """
    Create a student table
    """

    # Ensures that table will be named students in plural vs singular like the model name
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, unique=True)
    email = db.Column(db.Text, index=True, unique=True)
    # password_hash = db.Column(db.Text)
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    country = db.Column(db.Text)
    bio = db.Column(db.Text)
    cohort = db.Column(db.Text)
    linkedin = db.Column(db.Text)

    # Many to many relationships
    courses_taken = db.relationship('Course', secondary='courses_taken', backref='student', lazy='dynamic')
    courses_enrolled = db.relationship('Course', secondary='courses_enrolled',  backref='student', lazy='dynamic')
    interests = db.relationship('Interest', secondary='student_interests', backref='student', lazy='dynamic')
    # week_meet
    #.hy0=


    # Many to one relationships
    networking_goal = db.relationship('NetworkingGoal', secondary='student_networking_goals', backref='weekly_signup',lazy='dynamic')
    prim_time = db.relationship('TimePreference', secondary='primary_time_preferences',backref='student',lazy='dynamic')
    sec_time = db.relationship('TimePreference', secondary='secondary_time_preferences',backref='student',lazy='dynamic')
    prim_interest = db.relationship('Interest', secondary='primary_interests', backref='student',lazy='dynamic')
    sec_interest = db.relationship('Interest', secondary='secondary_interests', backref='student',lazy='dynamic')
    course_to_match = db.relationship('Course', secondary='courses_to_match', backref='student', lazy='dynamic')

    def __init__(self, student_id, firstname, lastname, email, city, country, bio, cohort, linkedin):
        self.student_id = student_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.city = city
        self.state = state
        self.country = country
        self.bio = bio
        self.cohort = cohort
        self.linkedin = linkedin

    def __repr__(self):
        """
        the toString method of the Student class
        :return: a String that includes the student's name and email.
        """
        return f"{self.firstname} {self.lastname} has email: {self.email}"


class TimePreference(db.Model):
    """
    This table is used to store all available time slots for students to choose from
    """

    __tablename__ = 'time_preferences'

    id = db.Column(db.Integer, primary_key=True)  # time_preference_id
    time = db.Column(db.Text)  # Might have to be text for now and then convert later

    def __init__(self, time):
        self.time = time

    def __repr__(self):
        """
        the toString method of the Student class
        :return: a String that includes the time preference.
        """
        return f"{self.time} "


class NetworkingGoal(db.Model):

    """
    this table is used to store the all networking goals for PennChats.
    Currently contains only two goals: match by class, match by interest
    """

    __tablename__ = 'networking_goals'

    id = db.Column(db.Integer, primary_key=True)  # networkingGoal_id
    networking_goal = db.Column(db.Text)

    def __init__(self, networking_goal):
        self.networking_goal = networking_goal


class Course(db.Model):
    """
    This table is used to store all MCIT Online courses.
    Course id is the actual MCIT online course ID number.

    """

    __tablename__ = 'courses'

    course_id = db.Column(db.Text, primary_key=True)  # we want to make sure it's unique
    course_name = db.Column(db.Text)

    def __init__(self, course_id):
        self.course_id = course_id


class Interest(db.Model):
    """
    this table is used to sore all interests we plan to provide as options for students to choose from
    when they fill out their user profile.
    """

    __tablename__ = 'interests'
    id = db.Column(db.Integer, primary_key=True)
    interest_name = db.Column(db.Text)

    weekly_signup_id = db.Column(db.Text, db.ForeignKey('weekly_signups.id'))

    def __init__(self, interest_name):
        self.interest_name = interest_name


###################################################
#              Association tables                 #
###################################################
class CoursesTaken(db.Model):
    """
    This table is used to store all pairings of students and their courses tables.
    There is a one-to-many relationship between the student table and this table.
    """
    __tablename__ = 'courses_taken'

    student_id = db.Column(db.Integer, ForeignKey("students.student_id"), primary_key=True)
    course_id = db.Column(db.Text, ForeignKey("courses.course_id"), primary_key=True)

    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id


class CourseEnrolled(db.Model):
    """
    This table is used to store all pairings of students and their courses tables.
    There is a one-to-one relationship between the student table and this table.
    """
    __tablename__ = 'courses_enrolled'

    student_id = db.Column(db.Integer, ForeignKey("students.student_id"), primary_key=True)
    course_id = db.Column(db.Text, ForeignKey("courses.course_id"), primary_key=True)

    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id


class StudentInterest(db.Model):
    """
    This table is used to store all pairings of students and their courses tables.
    There is a one-to-one relationship between the student table and this table.
    """
    __tablename__ = 'student_interests'

    student_id = db.Column(db.Integer, ForeignKey("students.student_id"), primary_key=True)
    interest_id = db.Column(db.Text, ForeignKey("interests.id"), primary_key=True)

    def __init__(self, student_id, interest_id):
        self.student_id = student_id
        self.interest_id = interest_id


class StudentNetworkingGoal(db.Model):
    """
    This table is used to store all pairings of students and their networking_goals tables.
    There is a one-to-many relationship between the student table and this table.
    """
    __tablename__ = 'student_networking_goals'

    student_id = db.Column(db.Integer, ForeignKey("students.student_id"), primary_key=True)
    networking_goal_id = db.Column(db.Integer, ForeignKey("networking_goals.id"), primary_key=True)

    def __init__(self, student_id, networking_goal_id):
        self.student_id = student_id
        self.networking_goal_id = networking_goal_id


class StudentPrimaryTimePreference(db.Model):
    """
    This table is used to store all pairings of students and their time_preferences tables.
    There is a one-to-many relationship between the student table and this table.
    """
    __tablename__ = 'primary_time_preferences'

    student_id = db.Column(db.Integer, ForeignKey("students.student_id"), primary_key=True)
    time_preference_id = db.Column(db.Integer, ForeignKey("time_preferences.id"))

    def __init__(self, student_id, time_preference_id):
        self.student_id = student_id
        self.time_preference_id = time_preference_id


class StudentSecondaryTimePreference(db.Model):
    """
    This table is used to store all pairings of students and their time_preferences tables.
    There is a one-to-many relationship between the student table and this table.
    """
    __tablename__ = 'secondary_time_preferences'

    student_id = db.Column(db.Integer, ForeignKey("students.student_id"), primary_key=True)
    time_preference_id = db.Column(db.Integer, ForeignKey("time_preferences.id"))

    def __init__(self, student_id, time_preference_id):
        self.student_id = student_id
        self.time_preference_id = time_preference_id


class StudentPrimaryInterest(db.Model):
    """
    This table is used to store all pairings of students and their courses tables.
    There is a one-to-one relationship between the student table and this table.
    """
    __tablename__ = 'primary_interests'

    student_id = db.Column(db.Integer, ForeignKey("students.student_id"), primary_key=True)
    interest_id = db.Column(db.Text, ForeignKey("interests.id"), primary_key=True)

    def __init__(self, student_id, interest_id):
        self.student_id = student_id
        self.interest_id = interest_id


class StudentSecondaryInterest(db.Model):
    """
    This table is used to store all pairings of students and their courses tables.
    There is a one-to-one relationship between the student table and this table.
    """
    __tablename__ = 'secondary_interests'

    student_id = db.Column(db.Integer, ForeignKey("students.student_id"), primary_key=True)
    interest_id = db.Column(db.Text, ForeignKey("interests.id"), primary_key=True)

    def __init__(self, student_id, interest_id):
        self.student_id = student_id
        self.interest_id = interest_id


class CourseToMatch(db.Model):
    """
    The course the student wants to match on
    """
    __tablename__ = 'courses_to_match'

    student_id = db.Column(db.Integer, ForeignKey("students.student_id"), primary_key=True)
    course_id = db.Column(db.Text, ForeignKey("courses.course_id"), primary_key=True)

    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id


class WeeklySignUp(db.Model):
    # should be an edit sheet that will pull in from last week and when they hit submit repopulates
    """
    Create a weekly signup table. This is in essence a join table from students to weekly signup
    """

    # Ensures that table will be named students in plural vs singular like the model name

    __tablename__ = 'weekly_signups'
    student_id = db.Column(db.Integer, ForeignKey("students.student_id"), primary_key=True)
    week_meet = db.Column(db.Text)

    def __init__(self, week_meet):
        self.week_meet = week_meet

    def __repr__(self):
        """
        the toString method of the Student class
        :return: a String that includes the student's name and email.
        """
        return f"We we're talking about {self.week_meet}"

    # if we want to know the number of students participating this week
    def count_students(self):
        print("Students participating in Penn Chats this week")
        student_count = 0
        for weekly_signup in self.weekly_signups:
            student_count += 1
        return student_count


class Group(db.Model):
    """
    This table is used to store all pairings of students and their courses tables.
    There is a one-to-one relationship between the student table and this table.
    """
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    # give the group a number so that we can collect students in the same group
    group_id = student_id = db.Column(db.Integer)

    student_id = db.Column(db.Integer, ForeignKey("students.student_id"))
    networking_goal_id = db.Column(db.Integer, ForeignKey("networking_goals.networking_goal_id"))
    time_preference_id = db.Column(db.Text, ForeignKey("TimePreference.time_preference_id"))

    def __init__(self, student_id, time_preference_id, networking_goal_id):
        self.student_id = student_id
        self.time_preference_id = time_preference_id
        self.networking_goal_id = networking_goal_id



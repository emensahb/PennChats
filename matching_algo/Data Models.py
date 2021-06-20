import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
CRUD - create, read, update, delete
Four main actions to perform on a table in a database
"""

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# this line is to connect flask app to the database, will need to be updated to our own PostgreSQL link
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Data models

class Student(db.model):

    student_id = db.Column(db.Integer, primary_key=True)
    # profile setup
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    city = db.Column(db.Text)
    country = db.Column(db.Text)
    bio = db.Column(db.Text)
    cohort = db.Column(db.Text)
    linkedin = db.Column(db.Text)

    # matching setup
    primary_time_selection_id = db.Column(db.Integer)
    secondary_time_selection_id = db.Column(db.Integer)
    primary_networking_goal_id = db.Column(db.Integer)
    secondary_networking_goal_id = db.Column(db.Integer)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        '''the toString method of the Student class
        :return: a String that includes the student's name and email.
        '''
        return f"{this.name} has email: {this.email}"


class TimePreference(db.model):
    """this table is used to store all available time slots for students to choose from"""

    time_preference_id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Time)

    def __init__(self, time):
        self.name = time


class NetworkingGoal(db.model):
    """this table is used to store the all networking goals for PennChats.
    Currently contains only two goals: match by class, match by interest"""

    networking_goal_id = db.Column(db.Integer, primary_key=True)
    networking_goal = db.Column(db.Text)

    def __init__(self, time):
        self.name = time


class Course(db.model):
    """this table is used to store all MCIT Online courses."""

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.Text)

    def __init__(self, course_name):
        self.course_name = course_name


class CourseEnrolledLookup(db.model):
    """this table is used to store all pairings of students and their enrolled_courses_by_student tables.
    There is a one-to-one relationship between the student table and this table."""

    student_id = db.Column(db.Integer, primary_key=True)
    enrolled_courses_by_student_id = db.Column(db.Integer)

    def __init__(self, student_id, enrolled_courses_by_student_id):
        self.student_id = student_id
        self.enrolled_courses_table_by_student_id = enrolled_courses_by_student_id


class CoursesEnrolledByStudent(db.model):
    """this table records all the courses currently taken by a specific student."""

    enrolled_courses_by_student_id # this is the id of this table and the primary_key
    enrolled_course_number = db.Column(db.Integer)
    course_id = db.Column(db.Integer)

    def __init__(self, enrolled_course_number, course_id):
        self.enrolled_course_number = enrolled_course_number
        self.course_id = course_id


class Interest(db.model):
    """this table is used to sore all interests we plan to provide as options for students to choose from
    when they fill out their user profile."""

    interest_id = db.Column(db.Integer, primary_key=True)
    interest_name = db.Column(db.Text)

    def __init__(self, interest_name):
        self.interest_name = interest_name


class StudentInterestTableLookup(db.model):
    """this table is used to store all pairings of students and their interests_by_student tables.
    There is a one-to-one relationship between the student table and this table."""

    student_id = db.Column(db.Integer, primary_key=True)
    interests_by_student_id = db.Column(db.Integer)

    def __init__(self, student_id, interests_by_student_id):
        self.student_id = student_id
        self.interests_by_student_id = interests_by_student_id


class InterestsByStudent(db.model):
    """this table records all the interests of a specific student."""

    interests_by_student_id = db(db.Integer, primary_key=True) # this is the id of this table and the primary_key
    student_interest_number = db.Column(db.Integer)
    interest_id = db.Column(db.Integer)

    def __init__(self, student_interest_number, interest_id):
        self.student_interest_number = student_interest_number
        self.interest_id = interest_id


class Group(db.model):
    """this table records all the students that are grouped together."""

    group_id = db(db.Integer, primary_key=True) # this is the id of this table and the primary_key
    group_student_number = db.Column(db.Integer)
    student_id = db.Column(db.Integer)
    name = db.Column(db.Text)
    email = db.Column(db.Text)

    def __init__(self, name, student_id, email):
        self.name = name
        self.student_id = student_id
        self.email = email


class Meeting(db.model):
    """this table describes all the meetings that will take place.
    the final output of the matching algorithm will be a list of Meeting objects.
    There is a one-to-one relationship between the Group table and this table."""

    meeting_id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.time)   # time slot that this meeting will take place
    course = db.Column(db.Text)   # the course that all students of this meeting share
    interest = db.Column(db.Text)   # the interest that all students of this meeting share

    def __init__(self, group_id, time):
        """Each meeting object has to have a group associated with it, and a meeting time associated with it."""
        self.group_id = group_id
        self.time = time


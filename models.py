from main import db, models
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Student(db.Model):
    """
    Create a student table
    """

    # Ensures that table will be named students in plural vs singular like the model name
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, index=True, unique=True)
    #password_hash = db.Column(db.Text)
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    country = db.Column(db.Text)
    bio = db.Column(db.Text)
    cohort = db.Column(db.Text)
    linkedin = db.Column(db.Text)

    def __init__(self, firstname, lastname, email, city, country, bio, cohort, linkedin):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.city = city
        # self.state = state We don't need state
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

    time_preference_id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Datetime)

    def __init__(self, time):
        self.time = time


class NetworkingGoal(db.Model):

    """
    this table is used to store the all networking goals for PennChats.
    Currently contains only two goals: match by class, match by interest
    """

    __tablename__ = 'networking_goals'

    networking_goal_id = db.Column(db.Integer, primary_key=True)
    networking_goal = db.Column(db.Text)

    def __init__(self, networking_goal):
        self.networking_goal = networking_goal


class Course(db.model):
    """
    This table is used to store all MCIT Online courses.
    Course id is the actual MCIT online course ID number.

    """

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True) # this is auto generated
    course_id = db.Column(db.Integer, unique=True)  # we want to make sure it's unique
    course_name = db.Column(db.Text)

    def __init__(self, course_id):
        self.course_id = course_id


class Interest(db.model):
    """
    this table is used to sore all interests we plan to provide as options for students to choose from
    when they fill out their user profile.
    """

    __tablename__ = 'interests'


    interest_id = db.Column(db.Integer, primary_key=True)
    interest_name = db.Column(db.Text)

    def __init__(self, interest_name):
        self.interest_name = interest_name


class CourseEnrolledLookup(db.model):
    """
    This table is used to store all pairings of students and their enrolled_courses_by_student tables.
    There is a one-to-one relationship between the student table and this table.
    """

    student_id = db.Column(db.Integer, primary_key=True)
    enrolled_courses_by_student_id = db.Column(db.Integer)

    def __init__(self, student_id, enrolled_courses_by_student_id):
        self.student_id = student_id
        self.enrolled_courses_table_by_student_id = enrolled_courses_by_student_id

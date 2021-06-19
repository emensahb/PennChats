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

    time_preference_id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Time)

    def __init__(self, time):
        self.name = time


class NetworkingGoal(db.model):

    networking_goal_id = db.Column(db.Integer, primary_key=True)
    networking_goal = db.Column(db.Text)

    def __init__(self, time):
        self.name = time


class Course(db.model):

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.Text)

    def __init__(self, course_name):
        self.course_name = course_name


class CourseEnrolledLookup(db.model):

    student_id = db.Column(db.Integer, primary_key=True)
    enrolled_courses_table_by_student_id = db.Column(db.Integer)

    def __init__(self, student_id, enrolled_courses_table_by_student_id):
        self.student_id = student_id
        self.enrolled_courses_table_by_student_id = enrolled_courses_table_by_student_id


class CoursesEnrolledByStudent(db.model):

    enrolled_course_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer)

    def __init__(self, enrolled_course_id, course_id):
        self.enrolled_course_id = enrolled_course_id
        self.course_id = course_id


class Group(db.model):

    group_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    name = db.Column(db.Text)
    email = db.Column(db.Text)

    def __init__(self, name, student_id, email):
        self.name = name
        self.student_id = student_id
        self.email = email


class Meeting(db.model):

    meeting_id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer)
    time = db.Column(db.time)
    course = db.Column(db.Text)
    interest = db.Column(db.Text)

    def __init__(self, group_id, time):
        self.group_id = group_id
        self.time = time


def main():
    """This is the main function that runs the algorithm. Pseudocode for now."""

    # import user information
        # read all students who would like to be matched into a list from todo STUDENT_WHO_WANT_MATCHED_TABLE
        # all_students = Student.query.all()

    # check if list is empty
        # if list is empty, output N/A, exit program
        # if list is not empty, proceed to next step

    # sort by primary time selection
        # for loop: for each student object in list, read the primary_time_selection_id of the student
        # from the STUDENT TABLE, put the student object into a todo PRIME TIME SELECTION DICTIONARY
        # with the primary_time_selection_id as key, and a list of student objects as value

    # check how many students are in each time selection group
        # for loop: for each key in the PRIME TIME SELECTION DICTIONARY, count the number of student objects
        # if conditional statement:
            # if size between 2-5, initialize a new Group object and add all student objects to the Group object table
            # if size = 1, add the student in this time group to todo the LIST OF UNMATCHED STUDENTS
            # if size > 5, proceed to next step to sort by primary networking goal

    # sort students by primary networking goal
        # for loop: for each student object in the given time selection group, read the primary_networking_goal_id
        # of the student from the STUDENT_WHO_WANT_MATCHED_TABLE, put the student object into a todo PRIME NETWORKING GOAL DICTIONARY
        # with the primary_networking_goal_id as key, and a list of student objects as value
        # there will likely be only two keys in this dictionary (sort by class & sort by interest)

    # further sort students by by type of primary networking goal
        # for loop if condition: for each key in the PRIME NETWORKING GOAL DICTIONARY, compare the primary_networking_goal_id...
            # if the key = "sort by class", do the following:
                # for loop: for each student object in the "sort by class" list, lookup the courses the student is currently taking
                # from the todo COURSES_ENROLLED_BY_STUDENT TABLE, put the student into a SHARED COURSE DICTIONARY
                # with the key being the course_id of the first course of the COURSES_ENROLLED_BY_STUDENT TABLE
                # and the value being a list of students who are also enrolled in this course
            # if the key = "sort by interest", do the following:
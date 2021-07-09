from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from main import db
# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash
# import datetime

# A side note. Table and class names camel case. Field names with the dashes


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

    def __init__(self, student_id, firstname, lastname, email, city, country, bio, cohort, linkedin):
        self.student_id = student_id
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

    __tablename__ = 'timePreferences'

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

    __tablename__ = 'networkingGoals'

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

    id = db.Column(db.Integer, primary_key=True)  # this is auto generated
    course_id = db.Column(db.Text, unique=True)  # we want to make sure it's unique
    course_name = db.Column(db.Text)

    def __init__(self, course_id):
        self.course_id = course_id


class Interest(db.Model):
    """
    this table is used to sore all interests we plan to provide as options for students to choose from
    when they fill out their user profile.
    """

    __tablename__ = 'interests'

    interest_id = db.Column(db.Integer, primary_key=True)
    interest_name = db.Column(db.Text)

    def __init__(self, interest_name):
        self.interest_name = interest_name


class StudentTimePreference(db.Model):
    """
    This table is used to store all pairings of students and their time_preferences tables.
    There is a one-to-many relationship between the student table and this table.
    """
    __tablename__ = 'student_time_preferences'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, ForeignKey("students.student_id"))
    time_preference_id = db.Column(db.Integer, ForeignKey("time_preferences.time_preference_id"))

    # Relationships
    student_id = relationship("Student", foreign_keys=[student_id])
    time_preference_id = relationship("TimePreference", foreign_keys=[time_preference_id])

    def __init__(self, student_id, time_preference_id):
        self.student_id = student_id
        self.time_preference_id = time_preference_id


class StudentNetworkingGoal(db.Model):
    """
    This table is used to store all pairings of students and their networking_goals tables.
    There is a one-to-many relationship between the student table and this table.
    """
    __tablename__ = 'studentNetworkingGoals'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, ForeignKey("students.student_id"))
    networking_goal_id = db.Column(db.Integer, ForeignKey("networking_goals.networking_goal_id"))

    # Relationships
    student_id = relationship("Student", foreign_keys=[student_id])
    networking_goal_id = relationship("NetworkingGoal", foreign_keys=[networking_goal_id])

    def __init__(self, student_id, networking_goal_id):
        self.student_id = student_id
        self.networking_goal_id = networking_goal_id


class CoursesTaken(db.Model):
    """
    This table is used to store all pairings of students and their courses tables.
    There is a one-to-many relationship between the student table and this table.
    """
    __tablename__ = 'coursesTaken'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, ForeignKey("students.student_id"))
    course_id = db.Column(db.Text, ForeignKey("courses.course_id"))

    # Relationships
    student_id = relationship("Student", foreign_keys=[student_id])
    course_id = relationship("Course", foreign_keys=[course_id])

    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id


class CourseEnrolledLookup(db.Model):
    """
    This table is used to store all pairings of students and their courses tables.
    There is a one-to-one relationship between the student table and this table.
    """
    __tablename__ = 'coursesEnrolled'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, ForeignKey("students.student_id"))
    course_id = db.Column(db.Text, ForeignKey("courses.course_id"))

    # Relationships
    student_id = relationship("Student", foreign_keys=[student_id])
    course_id = relationship("Course", foreign_keys=[course_id])

    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id


class StudentInterest(db.Model):
    """
    This table is used to store all pairings of students and their courses tables.
    There is a one-to-one relationship between the student table and this table.
    """
    __tablename__ = 'studentInterests'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, ForeignKey("students.student_id"))
    interest_id = db.Column(db.Text, ForeignKey("interests.interest_id"))

    # Relationships
    student_id = relationship("Student", foreign_keys=[student_id])
    interest_id = relationship("Interest", foreign_keys=[interest_id])

    def __init__(self, student_id, interest_id):
        self.student_id = student_id
        self.interest_id = interest_id


class Group(db.Model):
    """
    This table is used to store all pairings of students and their courses tables.
    There is a one-to-one relationship between the student table and this table.
    """
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, ForeignKey("students.student_id"))
    networking_goal_id = db.Column(db.Integer, ForeignKey("networking_goals.networking_goal_id"))
    time_preference_id = db.Column(db.Text, ForeignKey("TimePreference.time_preference_id"))

    # Relationships
    student_id = relationship("Student", foreign_keys=[student_id])
    time_preference_id = relationship("TimePreference", foreign_keys=[time_preference_id])
    networking_goal_id = relationship("NetworkingGoal", foreign_keys=[networking_goal_id])

    def __init__(self, student_id, time_preference_id, networking_goal_id):
        self.student_id = student_id
        self.time_preference_id = time_preference_id
        self.networking_goal_id = networking_goal_id

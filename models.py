from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from main import db

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
    # Student to many courses enrolled and taken
    courses_taken = db.relationship('Course', backref='student', lazy='dynamic')
    courses_enrolled = db.relationship('Course', backref='student', lazy='dynamic')

    # Student to many interests
    interests = db.relationship('Interest', backref='student', lazy='dynamic')

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


class WeeklySignUp(db.Model):
    # should be an edit sheet that will pull in from last week and when they hit submit repopulates
    """
    Create a weekly signup table
    """

    # Ensures that table will be named students in plural vs singular like the model name

    __tablename__ = 'weekly_signups'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.relationship('Student', backref='weeklySignup', lazy='dynamic')
    week_meet = db.Column(db.Text)  # week students are meeting

    # one to one relationships
    networking_goal = db.relationship('NetworkingGoal', backref='weeklySignup', uselist=False)
    prim_time = db.relationship('TimePreference', backref='weeklySignup', uselist=False)
    sec_time = db.relationship('TimePreference', backref='weeklySignup', uselist=False)
    prim_interest = db.relationship('Interest', backref='weeklySignup', uselist=False)
    sec_interest = db.relationship('Interest', backref='weeklySignup', uselist=False)
    course_to_match = db.relationship('Course', backref='weeklySignup', uselist=False)

    def __init__(self, student_id, week_meet, networking_goal, prim_time, sec_time, prim_interest, sec_interest,
                 course_to_match):
        self.student_id = student_id
        self.week_meet = week_meet
        self.networking_goal = networking_goal
        self.prim_time = prim_time
        self.sec_time = sec_time
        self.prim_interest = prim_interest
        self.sec_interest = sec_interest
        self.course_to_match = course_to_match

    def __repr__(self):
        """
        the toString method of the Student class
        :return: a String that includes the student's name and email.
        """
        return f"Meetings happening {self.week_meet}"

    # if we want to know the number of students participating this week
    def count_students(self):
        print("Students participating in Penn Chats this week")
        student_count = 0
        for weekly_signup in self.weekly_signups:
            student_count += 1
        return student_count


class TimePreference(db.Model):
    """
    This table is used to store all available time slots for students to choose from
    """

    __tablename__ = 'timePreferences'

    id = db.Column(db.Integer, primary_key=True)  # time_preference_id
    time = db.Column(db.Text)  # Might have to be text for now and then convert later

    weekly_signup_id = db.Column(db.Text, db.ForeignKey('weekly_signups.id'))

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

    weekly_signup_id = db.Column(db.Text, db.ForeignKey('weekly_signups.id'))

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

    student_id = db.Column(db.Text, db.ForeignKey('students.id'))

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

    weekly_signup_id = db.Column(db.Text, db.ForeignKey('weekly_signups.id'))

    def __init__(self, interest_name):
        self.interest_name = interest_name



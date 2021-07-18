from pennchatsproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(student_id):
    """Allows app the load the student based on the student_id that was passed in."""
    return Student.query.get(student_id)


class Student(db.Model, UserMixin):
    """Creates a model that represents a student.
    nullable=False means it will be compulsory to set the value for that column.
    index=True indicates that the column will be indexed.
    There is a many to many relationship between student and current courses,
    past courses, interests, and groups."""

    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    username = db.Column(db.String(64), unique=True, index=True)
    # not sure if we can just use student_id as primary key here.
    student_id = db.Column(db.Integer, unique=True)
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    country = db.Column(db.Text)
    bio = db.Column(db.Text)
    cohort = db.Column(db.Text)
    linkedin = db.Column(db.Text)
    profile_image = db.Column(
        db.String(64), nullable=False, default='default_profile.png')

    # many to many relationships
    current_courses = db.relationship(
        'Course', secondary='current_courses_record', backref='current_students')
    past_courses = db.relationship(
        'Course', secondary='past_courses_record', backref='past_students')
    interests = db.relationship(
        'Interest', secondary='student_interest_record', backref='all_students')

    # many to one relationships
    # calling weekly_signups.student will refer to the student associated with the weekly signup form
    weekly_signups = db.relationship('WeeklySignUp', backref='student')

    # one to many relatinoships
    course_id_to_match = db.Column(db.Integer, db.ForeignKey(
        'courses.id'))  # one to many, use course table
    interest_id_to_match = db.Column(db.Integer, db.ForeignKey(
        'interests.interest_id'))  # one to many, use interest table twice

    def __init__(self, email, username, student_id, password):
        self.username = username
        self.student_id = student_id
        self.password_hash = generate_password_hash(password)
        self.email = email

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Registered student: {self.username}, {self.student_id}, and {self.email}."


class WeeklySignUp(db.Model):
    """This table will store information of the matching preferences of a student on a given week.
    There is a one to many relationship between this table and the student table, the primetime table,
    the sectime table, primenetworkinggoal table, and the secnetworkinggoal table."""

    __tablename__ = 'weekly_signups'

    weekly_signup_id = db.Column(db.Integer, primary_key=True)
    week_meet = db.Column(db.Text)

    # one to many relationships
    student_id = db.Column(db.Integer, db.ForeignKey(
        'students.id'), nullable=False)

    prime_time_id = db.Column(db.Integer, db.ForeignKey(
        'time_options.time_id'), nullable=False)
    sec_time_id = db.Column(db.Integer, db.ForeignKey(
        'time_options.time_id'), nullable=False)

    prime_networking_goal_id = db.Column(db.Integer, db.ForeignKey(
        'networking_goals.networking_goal_id'), nullable=False)
    sec_networking_goal_id = db.Column(db.Integer, db.ForeignKey(
        'networking_goals.networking_goal_id'), nullable=False)

    def __init__(self, week_meet, student_id, prime_time_id, sec_time_id, prime_networking_goal_id, sec_networking_goal_id):
        # need to figure out how to best time stamp WeeklySignUp Forms
        self.week_meet = week_meet
        self.student_id = student_id
        self.prime_time_id = prime_time_id
        self.sec_time_id = sec_time_id
        self.prime_networking_goal_id = prime_networking_goal_id
        self.sec_networking_goal_id = sec_networking_goal_id

    def __repr__(self):
        return f"WeeklySignUp Form: time stamp: {self.week_meet}, {self.student_id}, prime time pref ID: {self.prime_time_id}, the sec time pref ID: {self.sec_time_id}, prime goal ID: {self.prime_networking_goal_id}, sec goal ID: {self.sec_networking_goal_id}."


class Course(db.Model):
    """This table is used to store all MCIT Online courses
    Course id is the actual MCIT online course ID number.
    There are several relationships between this table and the Student table."""
    # how do we input data to this table?

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    # not sure if we can just use course_id as primary key here
    course_id = db.Column(db.Text, unique=True, nullable=False)
    course_name = db.Column(db.Text, nullable=False)
    # calling student.course_to_match will return all the course this student prefers to be matched with
    students = db.relationship('Student', backref='course_to_match')

    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def __repr__(self):
        return f"This is the course of {self.course_name} with the course ID of {self.course_id}."


current_courses_record = db.Table('current_courses_record',
                                  db.Column('student_id', db.Integer, db.ForeignKey(
                                      'students.id'), primary_key=True),
                                  db.Column('course_id', db.Integer, db.ForeignKey(
                                      'courses.id'), primary_key=True)
                                  )

past_courses_record = db.Table('past_courses_record',
                               db.Column('student_id', db.Integer, db.ForeignKey(
                                   'students.id'), primary_key=True),
                               db.Column('course_id', db.Integer, db.ForeignKey(
                                   'courses.id'), primary_key=True)
                               )


class Interest(db.Model):
    """This table is used to store all interests we plan to provide as options for students to choose from
    when they fill out their user profile.
    There is a many to many relationship between this table and the student table."""
    # how do we input data to this table?

    __tablename__ = 'interests'

    interest_id = db.Column(db.Integer, primary_key=True)
    interest_name = db.Column(db.Text, nullable=False, unique=True)
    # calling student.interest_to_match will return all the interest this student prefers to be matched with
    students = db.relationship('Student', backref='interest_to_match')

    def __init__(self, interest_name):
        self.interest_name = interest_name

    def __repr__(self):
        return f"This is the interest of {self.interest_name} with the interest ID of {self.interest_id}."


student_interest_record = db.Table('student_interest_record',
                                   db.Column('student_id', db.Integer, db.ForeignKey(
                                       'students.id'), primary_key=True),
                                   db.Column('interest_id', db.Integer, db.ForeignKey(
                                       'interests.interest_id'), primary_key=True)
                                   )


class TimeOption(db.Model):
    """This table is used to store all available time slots for
    students to choose from for their PennChats meetings.
    There are two many to one relationships between this table and the WeeklySignUp table."""
    # how do we input data to this table?

    __tablename__ = 'time_options'

    time_id = db.Column(db.Integer, primary_key=True)
    time_option = db.Column(db.Text, nullable=False, unique=True)

    # many to one relationships
    # calling WeeklySignUp.primetime will refer to the primary time preference associated with the form
    prim_time_signups = db.relationship(
        'WeeklySignUp', foreign_keys='WeeklySignUp.prime_time_id', backref='primetime')
    # calling WeeklySignUp.sectime will refer to the secondary time preference associated with the form
    sec_time_signups = db.relationship(
        'WeeklySignUp', foreign_keys='WeeklySignUp.sec_time_id', backref='sectime')

    def __init__(self, time):
        self.time = time

    def __repr__(self):
        return f"This is the time option of {self.time_option} with the time ID of {self.time_id}."


class NetworkingGoal(db.Model):
    """This table is used to store the all networking goals for
    students to choose from for their PennChats meetings.
    Currently contains only two goals: match by class, match by interest.
    There are two many to one relationships between this table and the WeeklySignUp table."""
    # how do we input data to this table?

    __tablename__ = 'networking_goals'

    networking_goal_id = db.Column(db.Integer, primary_key=True)
    networking_goal = db.Column(db.Text, nullable=False, unique=True)

    # many to one relationships
    # calling WeeklySignUp.primegoal will refer to the primary goal associated with the form
    prim_goal_signups = db.relationship(
        'WeeklySignUp', foreign_keys='WeeklySignUp.prime_networking_goal_id', backref='primegoal')
    # calling WeeklySignUp.secgoal will refer to the secondary goal preference associated with the form
    sec_goal_signups = db.relationship(
        'WeeklySignUp', foreign_keys='WeeklySignUp.sec_networking_goal_id', backref='secgoal')

    def __init__(self, networking_goal):
        self.networking_goal = networking_goal

    def __repr__(self):
        return f"This is the networking goal of {self.networking_goal} with the ID of {self.networking_goal_id}."

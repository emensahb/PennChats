#models.py
from pennchatsproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(student_id):
    return Student.query.get(student_id)


class Student(db.Model, UserMixin):
    """Creates a model that represents a student.
    nullable=False means it will be compulsory to set the value for that column.
    index=True indicates that the column will be indexed.
    There is a many to many relationship between student and current courses,
    past courses, interests, and groups."""


    __tablename__ = 'students'

    #id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, primary_key=True, nullable=False) # not sure if we can just use student_id as primary key here.
    password_hash = db.Column(db.String(128))
    username = db.Column(db.String(64),unique=True,index=True)
    firstname = db.Column(db.Text, nullable=False)
    lastname = db.Column(db.Text, nullable=False)
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    linkedin = db.Column(db.Text)
    cohort = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    country = db.Column(db.Text)
    bio = db.Column(db.Text)

    currentcourses = db.relationship('currentcourses', secondary=current_courses_record, backref='currentstudents')
    pastcourses = db.relationship('pastcourses', secondary=past_courses_record, backref='paststudents')
    interests = db.relationship('interests', secondary=student_interest_record, backref='students')
    matchingpreferences = db.relatinoship('MatchingPreference', backref='student') # calling MatchingPreference.student will refer to the student associated with the matching preference instance

    firstchoicecourse #one to many, new course table
    secondchoicecourse #one to many

    firstchoiceinterests #one to many
    secondchoiceinterests #one to many

    def __init__(self, student_id, password, firstname, lastname, email):
        self.student_id = student_id
        self.password_hash = generate_password_hash(password)
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"This is a registered student by the name of {self.firstname} {self.lastname}, with a student_id of {self.student_id}."


class MatchingPreference(db.Model):
    """This table will store information of the matching preferences of a student on a given week.
    There is a one to many relationship between this table and the student table, the primetime table,
    the sectime table, primenetworkinggoal table, and the secnetworkinggoal table."""

    __tablename__ = 'matchingpreferences'

    matching_preference_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'), nullable=False)
    prime_time_id = db.Column(db.Integer, db.ForeignKey('primetimeoptions.time_id'), nullable=False)
    sec_time_id = db.Column(db.Integer, db.ForeignKey('secondarytimeoptions.time_id'), nullable=False)
    prime_networking_goal_id = db.Column(db.Integer, db.ForeignKey('primenetworkinggoals.networking_goal_id'), nullable=False)
    sec_networking_goal_id = db.Column(db.Integer, db.ForeignKey('secondarynetworkinggoals.networking_goal_id'), nullable=False)

    def __init__(self, student_id, prime_time_id, sec_time_id, prime_networking_goal_id, sec_networking_goal_id):
        self.student_id = student_id
        self.prime_time_id = prime_time_id
        self.sec_time_id = sec_time_id
        self.prime_networking_goal_id = prime_networking_goal_id
        self.sec_networking_goal_id = sec_networking_goal_id

    def __repr__(self):
        return f"This is a matching preference form filled out by a student with the ID of {self.student_id}, with the prime time pref ID of {self.prime_time_id} and the sec time pref ID of {self.sec_time_id}, with the prime goal ID of {self.prime_networking_goal_id} and the sec goal ID of {self.sec_networking_goal_id}."


class CurrentCourse(db.Model):
    """This table is used to store all MCIT Online courses
    that is currently being taken by students.
    Course id is the actual MCIT online course ID number.
    There is a many to many relationship between this table and the student table."""
    # how do we input data to this table?

    __tablename__ = 'currentcourses'

    #id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Text, primary_key=True, unique=True, nullable=False) # not sure if we can just use course_id as primary key here
    course_name = db.Column(db.Text, nullable=False)
    #students = db.relationship('student', secondary=current_courses_record, backref='currentcourses') # calling student.currentcourses will return all past courses of this student

    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def __repr__(self):
        return f"This is the current course of {self.course_name} with the course ID of {self.course_id}."


current_courses_record = db.Table('StudentCurrentCourses',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('currentcourses.course_id'), primary_key=True)
)


class PastCourse(db.Model):
    """This table is used to store all MCIT Online courses
    that has been taken by students in the past.
    This table is created to differentiate from current courses table
    that records current courses student is taking.
    There is a many to many relationship between this table and the student table."""
    # how do we input data to this table?

    __tablename__ = 'pastcourses'

    #id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Text, primary_key=True, unique=True, nullable=False) # not sure if we can just use course_id as primary key here
    course_name = db.Column(db.Text, nullable=False, unique=True)
    #students = db.relationship('student', secondary=past_courses_record, backref='pastcourses') # calling student.pastcourses will return all past courses of this student

    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def __repr__(self):
        return f"This is the past course of {self.course_name} with the course ID of {self.course_id}."


past_courses_record = db.Table('StudentPastCourses',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('pastcourses.course_id'), primary_key=True)
)


class Interest(db.Model):
    """This table is used to store all interests we plan to provide as options for students to choose from
    when they fill out their user profile.
    There is a many to many relationship between this table and the student table."""
    # how do we input data to this table?

    __tablename__ = 'interests'

    interest_id = db.Column(db.Integer, primary_key=True)
    interest_name = db.Column(db.Text, nullable=False, unique=True)

    def __init__(self, interest_name):
        self.interest_name = interest_name

    def __repr__(self):
        return f"This is the interest of {self.interest_name} with the interest ID of {self.interest_id}."


student_interest_record = db.Table('StudentInterests',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('interest_id', db.Integer, db.ForeignKey('interests.interest_id'), primary_key=True)
)


class PrimeTime(db.Model):
    """This table is used to store all available time slots for
    students to choose from as their primary/ideal times for their PennChats meetings.
    There is a many to one relationship between this table and the matching preference table."""
    # how do we input data to this table?

    __tablename__ = 'primetimeoptions'

    time_id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Text, nullable=False, unique=True)
    matchingpreferences = db.relatinoship('MatchingPreference', backref='primetime') # calling MatchingPreference.primetime will refer to the primary time preference associated with the matching preference instance

    def __init__(self, time):
        self.time = time

    def __repr__(self):
        return f"This is the primary time option of {self.time} with the time ID of {self.time_id}."


class SecTime(db.Model):
    """This table is used to store all available time slots for
    students to choose from as their secondary times for their PennChats meetings.
    There is a many to one relationship between this table and the matching preference table."""
    # how do we input data to this table?

    __tablename__ = 'secondarytimeoptions'

    time_id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Text, nullable=False, unique=True)
    matchingpreferences = db.relatinoship('MatchingPreference', backref='sectime') # calling MatchingPreference.sectime will refer to the secondary time preference associated with the matching preference instance

    def __init__(self, time):
        self.time = time

    def __repr__(self):
        return f"This is the secondary time option of {self.time} with the time ID of {self.time_id}."


class PrimeNetworkingGoal(db.Model):
    """This table is used to store the all networking goals for
    students to choose from as their primary networking goal for their PennChats meetings.
    Currently contains only two goals: match by class, match by interest.
    There is a many to one relationship between this table and the matching preference table."""
    # how do we input data to this table?

    __tablename__ = 'primenetworkinggoals'

    networking_goal_id = db.Column(db.Integer, primary_key=True)
    networking_goal = db.Column(db.Text, nullable=False, unique=True)
    matchingpreferences = db.relatinoship('MatchingPreference', backref='primegoal') # calling MatchingPreference.primegoal will refer to the primary networking goal associated with the matching preference instance

    def __init__(self, networking_goal):
        self.networking_goal = networking_goal

    def __repr__(self):
        return f"This is the primary networking preference of {self.networking_goal} with the ID of {self.networking_goal_id}."


class SecNetworkingGoal(db.Model):
    """This table is used to store the all networking goals for
    students to choose from as their secondary networking goal for their PennChats meetings.
    Currently contains only two goals: match by class, match by interest.
    There is a many to one relationship between this table and the matching preference table."""
    # how do we input data to this table?

    __tablename__ = 'secondarynetworkinggoals'

    networking_goal_id = db.Column(db.Integer, primary_key=True)
    networking_goal = db.Column(db.Text, nullable=False, unique=True)
    matchingpreferences = db.relatinoship('MatchingPreference', backref='secgoal') # calling MatchingPreference.secgoal will refer to the secondary networking goal associated with the matching preference instance

    def __init__(self, networking_goal):
        self.networking_goal = networking_goal

    def __repr__(self):
        return f"This is the secondary networking preference of {self.networking_goal} with the ID of {self.networking_goal_id}."


class Group(db.Model):
    """This table is used to store all pairings of students and their courses tables.
    There is a many to many relationship between this table and the student table,
    because a student will be assigned to different groups when they sign up for
    chats multiple times."""
    # how do we input data to this table?

    __tablename__ = 'groupings'

    group_id = db.Column(db.Integer, primary_key=True)
    students = db.relationship('students', secondary=grouping_record, backref='groupings')

    def __init__(self):
        pass # not sure how to initialize a group, given that there is no other attribute than student objects
             # how do I pass in a statement in the algorithm to initialize a group object?


grouping_record = db.Table('student_groupings',
    db.Column('group_id', db.Integer, db.ForeignKey('groupings.group_id'), primary_key=True)
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True)
)


class Meeting(db.Model):
    """This table describes all the meetings that has been set up.
    The final output of the matching algorithm will be a list of Meeting objects.
    There is a one-to-one relationship between the Group table and this table."""
    # how do we input data to this table?

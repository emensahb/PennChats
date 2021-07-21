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

    student_id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    country = db.Column(db.Text)
    bio = db.Column(db.Text)
    linkedin = db.Column(db.Text)
    # profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')

    # many to many relationships
    # other interests on form
    interests = db.relationship('Interest', secondary='student_interests', backref='student')

    # next week
    next_week = db.relationship('WeeklySignUp', backref='student')

    cohort = db.relationship('Cohort', secondary='student_cohorts', backref='student')
    networking_goal = db.relationship('NetworkingGoal', secondary='student_networking_goals', backref='student')

    # Whether they are participating in the weekly meeting or not
    def __init__(self, email, username, student_id, password):
        self.username = username
        self.student_id = student_id
        self.password_hash = generate_password_hash(password)
        self.email = email

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"{self.firstname}  {self.lastname} has email: {self.email} and student ID: {self.student_id}"


class WeeklySignUp(db.Model):
    # should be an edit sheet that will pull in from last week and when they hit submit repopulates
    """
    A list of students who are signed up to chat this week
    """

    # Ensures that table will be named students in plural vs singular like the model name

    __tablename__ = 'weekly_signups'
    id = db.Column(db.Integer, primary_key=True)
    next_week = db.Column(db.Text)  # time stamp for when student submits week meet form
    student_id = db.Column(db.Integer, db.ForeignKey("students.student_id"), primary_key=True)

    def __init__(self, next_week):
        self.next_week = next_week

    def __repr__(self):
        return f"Meetings for the week starting: {self.next_week}"

    # if we want to know the number of students participating this week
    def count_students(self):
        print("Students participating in Penn Chats this week")
        student_count = 0
        for weekly_signup in self.weekly_signups:
            student_count += 1
        return student_count


class Class(db.Model):
    """This table is used to store all MCIT Online courses
    class id is the actual MCIT online course ID number.
    There are several relationships between this table and the Student table."""
    # how do we input data to this table?
    # for reference why I commented out students:
    # https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many
    # see using backref

    __tablename__ = 'classes'

    # id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, primary_key=True, nullable=False)
    class_name = db.Column(db.Text, nullable=False)

    def __init__(self, class_id, class_name):
        self.class_id = class_id
        self.class_name = class_name

    def __repr__(self):
        return f" {self.class_id} - {self.class_name} "


class StudentClass(db.Model):
    # should be an edit sheet that will pull in from last week and when they hit submit repopulates
    """
    An Association table between students and classes
    """

    # Ensures that table will be named students in plural vs singular like the model name

    __tablename__ = 'student_classes'
    student_id = db.Column(db.Integer, db.ForeignKey("students.student_id"), primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.class_id"), primary_key=True)
    enrolled = db.Column(db.Text)  # true/false
    taken = db.Column(db.Text)  # true/false
    class_match = db.Column(db.Text)  # class to match on. true/false

    def __init__(self, student_id, class_id, enrolled, taken, class_match):
        self.student_id = student_id
        self.class_id = class_id
        self.enrolled = enrolled
        self.taken = taken
        self.class_match = class_match

    def __repr__(self):
        return f"Student:{self.student_id} - for class: {self.class_id}"


class Interest(db.Model):
    """This table is used to store all interests we plan to provide as options for students to choose from
    when they fill out their user profile.
    There is a many to many relationship between this table and the student table."""
    # how do we input data to this table?

    __tablename__ = 'interests'

    id = db.Column(db.Integer, primary_key=True)
    interest_name = db.Column(db.Text, nullable=False, unique=True)

    def __init__(self, interest_name):
        self.interest_name = interest_name

    def __repr__(self):
        return f"Interest: {self.id}. {self.interest_name}"


class StudentInterest(db.Model):
    # should be an edit sheet that will pull in from last week and when they hit submit repopulates
    """
    An association table between students and interests
    """

    __tablename__ = 'student_interests'
    student_id = db.Column(db.Integer, db.ForeignKey("students.student_id"), primary_key=True)
    interest_id = db.Column(db.Integer, db.ForeignKey("interests.id"), primary_key=True)
    primary_interest = db.Column(db.Text, nullable=False, primary_key=True)  # True/False
    secondary_interest = db.Column(db.Text, nullable=False, primary_key=True)  # True/False

    def __init__(self, student_id, interest_id, primary_interest, secondary_interest):
        self.student_id = student_id
        self.interest_id = interest_id
        self.primary_interest = primary_interest
        self.secondary_interest = secondary_interest

    def __repr__(self):
        return f"Student:{self.student_id} - Primary Interest: {self.primary_interest} " \
               f"- Secondary Interest:{self.secondary_interest} "


class Cohort(db.Model):
    """This is a list of cohorts ever to exist on MCIT Online"""
    # how do we input data to this table?
    # for reference why I commented out students:
    # https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many
    # see using backref

    __tablename__ = 'cohorts'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    cohort_name = db.Column(db.Text, nullable=False)

    def __init__(self, id, cohort_name):
        self.id = id
        self.cohort_name = cohort_name

    def __repr__(self):
        return f" {self.id} - {self.cohort_name} "


cohort = db.Table('student_cohorts',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('cohort_id', db.Integer, db.ForeignKey('cohorts.id'), primary_key=True)
)


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
        return f"Time preference: {self.id}. {self.time}"


class StudentTimePreference(db.Model):
    # should be an edit sheet that will pull in from last week and when they hit submit repopulates
    """
    An association table between students and their time preferences
    """

    # Ensures that table will be named students in plural vs singular like the model name

    __tablename__ = 'student_time_preferences'
    student_id = db.Column(db.Integer, db.ForeignKey("students.student_id"), primary_key=True)
    time_preference_id = db.Column(db.Integer, db.ForeignKey("time_preferences.id"), primary_key=True)
    prim_time = db.Column(db.Text, nullable=False, primary_key=True)
    sec_time = db.Column(db.Text, nullable=False, primary_key=True)


class NetworkingGoal(db.Model):
    """This table is used to store the all networking goals for
    students to choose from for their PennChats meetings.
    Currently contains only two goals: match by class, match by interest.
    There are two many to one relationships between this table and the WeeklySignUp table."""
    # how do we input data to this table?

    __tablename__ = 'networking_goals'

    id = db.Column(db.Integer, primary_key=True)
    networking_goal = db.Column(db.Text, nullable=False, unique=True)

    def __init__(self, networking_goal):
        self.networking_goal = networking_goal

    def __repr__(self):
        return f" Networking Goal: {self.id}. {self.networking_goal}"


student_networking_goal = db.Table('student_networking_goals',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('networking_goal_id', db.Integer, db.ForeignKey('networking_goals.id'), primary_key=True)

)



tp1 = TimePreference("Morning: 9am ET")
tp2 = TimePreference("Afternoon: 3pm ET")
tp3 = TimePreference("Evening: 7pm ET")
tp4 = TimePreference("Overnight: 1am ET")


# networking goals options
ng1 = NetworkingGoal("class")
ng2 = NetworkingGoal("interest")


# classes
c1 = Class(591, "Intro to Software Development")
c2 = Class(592, "Math Foundations of Computer Science")
c3 = Class(593, "Intro to Computer Systems")
c4 = Class(594, "Data Structures and Software Design")
c5 = Class(595, "Computer Systems Programming")
c6 = Class(596, "Algorithms & Computation")
c7 = Class(515, "Fundamentals of Linear Algebra & Optimization")
c8 = Class(547, "Software Analysis")
c9 = Class(549, "Wireless Communication for Mobile Networks")
c10 = Class(581, "Computer Vision & Computational Photography")

# interests
i1 = Interest("Artificial Intelligence & Machine Learning")
i2 = Interest("Blockchain")
i3 = Interest("Cybersecurity & Cryptography")
i4 = Interest("Data Science")
i5 = Interest("Game Design")
i6 = Interest("Interview Prep")
i7 = Interest("Mathematics for Computer Science")
i8 = Interest("Networking & Computer Systems")
i9 = Interest("Project Management")
i10 = Interest("Software Development")

# cohort
cht1 = Cohort(1, "Spring 2019")
cht2 = Cohort(2, "Fall 2019")
cht3 = Cohort(3, "Spring 2020")
cht4 = Cohort(4, "Fall 2020")
cht5 = Cohort(5, "Spring 2021")
cht6 = Cohort(6, "Fall 2021")

db.create_all()
db.session.add_all([tp1, tp2, tp3, tp4, ng1, ng2, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
                    i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, cht1, cht2, cht3, cht4, cht5, cht6])

# db.session.add_all([cht5, cht6])
db.session.commit()

# class TimeOption(db.Model):
"""This table is used to store all available time slots for
students to choose from for their PennChats meetings.
There are two many to one relationships between this table and the WeeklySignUp table.
"""
    # how do we input data to this table?

  #  __tablename__ = 'time_options'

  #  time_id = db.Column(db.Integer, primary_key=True)
 #   time_option = db.Column(db.Text, nullable=False, unique=True)

    # many to one relationships
  #  prim_time_signups = db.relationship('WeeklySignUp', foreign_keys='WeeklySignUp.prime_time_id', backref='primetime') # calling WeeklySignUp.primetime will refer to the primary time preference associated with the form
  #  sec_time_signups = db.relationship('WeeklySignUp', foreign_keys='WeeklySignUp.sec_time_id', backref='sectime') # calling WeeklySignUp.sectime will refer to the secondary time preference associated with the form

  #  def __init__(self, time):
      #  self.time = time

  #  def __repr__(self):
      #  return f"This is the time option of {self.time_option} with the time ID of {self.time_id}."
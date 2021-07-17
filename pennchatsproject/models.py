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
    current_classes = db.relationship('Class', secondary='current_classes', backref='student')
    classes_taken = db.relationship('Class', secondary='classes_taken', backref='student')
    interests = db.relationship('Interest', secondary='student_interests', backref='student')

    # Many to one relationships
    cohort = db.Column(db.Text)
    networking_goal = db.relationship('NetworkingGoal', secondary='networking_goals', backref='weekly_signup')
    prim_time = db.relationship('TimePreference', secondary='student_primary_time_preferences', backref='student')
    sec_time = db.relationship('TimePreference', secondary='student_secondary_time_preferences', backref='student')
    prim_interest = db.relationship('Interest', secondary='student_primary_interests', backref='student')
    sec_interest = db.relationship('Interest', secondary='student_secondary_interests', backref='student')
    class_to_match = db.relationship('Class', secondary='class_to_match', backref='student')

    # Whether they are participating in the weekly meeting or not
    week_meet =

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
    student_id = db.Column(db.Integer, db.ForeignKey("students.student_id"), primary_key=True)
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


class Class(db.Model):
    """This table is used to store all MCIT Online courses
    class id is the actual MCIT online course ID number.
    There are several relationships between this table and the Student table."""
    # how do we input data to this table?
    # for reference why I commented out students: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many
    # see using backref

    __tablename__ = 'classes'

    # id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, primary_key=True, nullable=False) # not sure if we can just use course_id as primary key here
    class_name = db.Column(db.Text, nullable=False)
    # students = db.relationship('Student', backref='course_to_match') # calling student.course_to_match will return all the course this student prefers to be matched with

    def __init__(self, class_id, class_name):
        self.class_id = class_id
        self.class_name = class_name

    def __repr__(self):
        return f" {self.class_id} - {self.class_name} "


current_classes = db.Table('current_classes',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('class_id', db.Integer, db.ForeignKey('classes.course_id'), primary_key=True)
)

courses_taken = db.Table('classes_taken',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('class_id', db.Integer, db.ForeignKey('classes.course_id'), primary_key=True)
)

courses_to_match = db.Table('class_to_match',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('class_id', db.Integer, db.ForeignKey('classes.class_id'), primary_key=True)
)


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
        return f"Interest: {self.interest_id}. {self.interest_name}"


student_interests = db.Table('student_interests',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('interest_id', db.Integer, db.ForeignKey('interests.id'), primary_key=True)
                             )

student_primary_interests = db.Table('prim_time',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('interest_id', db.Integer, db.ForeignKey('interests.id'), primary_key=True)
)

student_secondary_interests  = db.Table('sec_time',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('interest_id', db.Integer, db.ForeignKey('interests.id'), primary_key=True)
)


class Cohort(db.Model):
    """This table is used to store all MCIT Online courses
    Course id is the actual MCIT online course ID number.
    There are several relationships between this table and the Student table."""
    # how do we input data to this table?
    # for reference why I commented out students: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many
    # see using backref

    __tablename__ = 'cohorts'

    # id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Text, primary_key=True, nullable=False) # not sure if we can just use course_id as primary key here
    cohort_name = db.Column(db.Text, nullable=False)
    # students = db.relationship('Student', backref='course_to_match') # calling student.course_to_match will return all the course this student prefers to be matched with

    def __init__(self, course_id, course_name):
        self.id = id
        self.cohort_name = cohort_name

    def __repr__(self):
        return f" {self.id} - {self.cohort_name} "


cohorts = db.Table('cohort',
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

student_primary_time_preference = db.Table('prim_interest',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('time_id', db.Integer, db.ForeignKey('time_preferences.id'), primary_key=True)
)

student_secondary_time_preference  = db.Table('sec_interest',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('time_id', db.Integer, db.ForeignKey('time_preferences.id'), primary_key=True)

)



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

networking_goals = db.Table('networking_goal',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('networking_goals.id'), primary_key=True)
)




# class TimeOption(db.Model):
    """This table is used to store all available time slots for
    students to choose from for their PennChats meetings.
    There are two many to one relationships between this table and the WeeklySignUp table."""
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
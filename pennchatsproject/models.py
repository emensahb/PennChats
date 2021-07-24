from pennchatsproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many


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
    linkedin = db.Column(db.String)

    # profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')

    # many to many relationships
    class_enrolled = db.relationship('ClassEnrolled', secondary='students_classes_enrolled', backref='student')
    class_taken_id = db.relationship('ClassTaken', secondary='students_classes_taken', backref='student')
    matched_class = db.relationship('MatchedClass', secondary='students_matched_classes', backref='student')

    # other interests on form
    interests = db.relationship('Interest', secondary='students_interests', backref='student')
    matched_interest = db.relationship('MatchedInterest', secondary='students_matched_interests', backref='student')

    # One to many
    cohort = db.relationship('Cohort', backref='student')
    cohort_id = db.Column('cohort_id', db.Integer, db.ForeignKey('cohorts.id'))
    networking_goal = db.relationship('NetworkingGoal', backref='student')
    networking_goal_id = db.Column('networking_goal_id', db.Integer, db.ForeignKey('networking_goals.id'))

    weekly_signup = db.relationship('WeeklySignUp', secondary='students_weekly_signups', backref='student')
    weekly_signup_id = db.Column('weekly_signup_id', db.Integer, db.ForeignKey('weekly_signups.id'))
    # meetings = db.relationship('Meeting', backref='week_of_meeting')

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
    """
    A list of students who are signed up to chat this week
    """
    __tablename__ = 'weekly_signups'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.relationship("Student", backref='student')

    week_of_meeting = db.relationship("WeekOfMeeting", backref='weekly_signup')
    week_of_meeting_name = db.Column('week_of_meeting_name', db.Text, db.ForeignKey('week_of_meetings.week_of_meeting_name'))

    primary_time = db.relationship("PrimaryTimePreference", secondary='weekly_signups_primary_time_preferences', backref='weekly_signup')
    secondary_time = db.relationship("SecondaryTimePreference", secondary='weekly_signups_secondary_time_preferences', backref='weekly_signup')

    primary_interest = db.relationship("PrimaryInterest", secondary='weekly_signups_primary_interests', backref='weekly_signup')
    secondary_interest = db.relationship("SecondaryInterest", secondary='weekly_signups_secondary_interests', backref='weekly_signup')

    def __init__(self, week_of_meeting):
        self.week_of_meeting = week_of_meeting

    def __repr__(self):
        return f"Meetings for the week starting: {self.week_of_meeting}"

    # if we want to know the number of students participating this week
    def count_students(self):
        print("Students participating in Penn Chats this week")
        student_count = 0
        for weekly_signup in self.weekly_signups:
            student_count += 1
        return student_count


student_weekly_signup = db.Table('students_weekly_signups',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('weekly_signup_id', db.Integer, db.ForeignKey('weekly_signups.id'), primary_key=True)
)


class WeekOfMeeting(db.Model):
    """This table will store all the available weeks that students to sign up
        for PennChats. The table will be queried to provide options for students to
        fill out their WeeklySignUp forms.
        There is a many to one relationship between this table and the WeeklySignUp
        table."""

    __tablename__ = 'week_of_meetings'

    week_of_meeting_name = db.Column(db.Text, primary_key=True, nullable=False)

    # many to one relationship
    # weekly_signups = db.relationship('WeeklySignUp', backref='week_of_meeting')
    # meetings = db.relationship('Meeting', backref='week_of_meeting')
    # unmatched_students = db.relationship('UnmatchedStudents', backref='week_of_meeting')

    def __init__(self, week_of_meeting_name):
        self.week_of_meeting_name = week_of_meeting_name

    def __repr__(self):
        return f"Meeting week: {self.week_of_meeting_name}."


class ClassEnrolled(db.Model):
    """
    The list if classes the student is currently enrolled in
    Many-to-many-relationship with student class
    """

    __tablename__ = 'classes_enrolled'

    class_enrolled_id = db.Column(db.Integer, primary_key=True, nullable=False)
    class_enrolled_name = db.Column(db.Text, nullable=False)

    def __init__(self, class_enrolled_id, class_enrolled_name):
        self.class_enrolled_id = class_enrolled_id
        self.class_enrolled_name = class_enrolled_name

    def __repr__(self):
        return f" Class enrolled: {self.class_enrolled_id} - {self.class_enrolled_name} "


student_class_enrolled = db.Table('students_classes_enrolled',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('class_enrolled_id', db.Integer, db.ForeignKey('classes_enrolled.class_enrolled_id'), primary_key=True)
)


class ClassTaken(db.Model):
    """The list if classes the student has taken
        Many-to-many-relationship with student class
    """

    __tablename__ = 'classes_taken'
    class_taken_id = db.Column(db.Integer, primary_key=True, nullable=False)
    class_taken_name = db.Column(db.Text, nullable=False)

    def __init__(self, class_taken_id, class_taken_name):
        self.class_taken_id = class_taken_id
        self.class_taken_name = class_taken_name

    def __repr__(self):
        return f" Class taken: {self.class_taken_id} - {self.class_taken_name} "


student_classes_taken = db.Table('students_classes_taken',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('class_taken_id', db.Integer, db.ForeignKey('classes_taken.class_taken_id'), primary_key=True)
)


class MatchedClass(db.Model):
    """
    The list if classes the student wants to match on
    Many to many
    """

    __tablename__ = 'matched_classes'

    matched_class_id = db.Column(db.Integer, primary_key=True, nullable=False)
    matched_class_name = db.Column(db.Text, nullable=False)

    def __init__(self, matched_class_id, matched_class_name):
        self.matched_class_id = matched_class_id
        self.matched_class_name = matched_class_name

    def __repr__(self):
        return f" {self.matched_class_id} - {self.matched_class_name} "


student_matched_class = db.Table('students_matched_classes',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('matched_class_id', db.Integer, db.ForeignKey('matched_classes.matched_class_id'), primary_key=True)
)


class Interest(db.Model):
    """This table is used to store all interests we plan to provide as options for students to choose from
    when they fill out their user profile.
    There is a many to many relationship between this table and the student table."""
    # how do we input data to this table?

    __tablename__ = 'interests'
    id = db.Column(db.Integer, primary_key=True)
    interest_name = db.Column(db.Text, nullable=False, primary_key=True)

    def __init__(self, interest_name):
        self.interest_name = interest_name

    def __repr__(self):
        return f"Interest: {self.id}. {self.interest_name}"


class StudentInterest(db.Model):
    """
    An association table between students and interests
    """

    __tablename__ = 'students_interests'
    student_id = db.Column(db.Integer, db.ForeignKey("students.student_id"), primary_key=True)
    interest_id = db.Column(db.Integer, db.ForeignKey("interests.id"), primary_key=True)

    def __init__(self, student_id, interest_id):
        self.student_id = student_id
        self.interest_id = interest_id

    def __repr__(self):
        return f"Student:{self.student_id} - Interest: {self.interest_id}"


class PrimaryInterest(db.Model):
    """
    The primary interests students have chosen
    An association table between Primary Interest and students
    """

    __tablename__ = 'primary_interests'
    primary_interest_id = db.Column(db.Integer, primary_key=True)
    primary_interest_name = db.Column(db.Text, primary_key=True, nullable=False)

    def __init__(self, primary_interest_name):
        self.primary_interest_name = primary_interest_name

    def __repr__(self):
        return f" Primary Interest:{self.primary_interest_name}"


weekly_signup_primary_interest = db.Table('weekly_signups_primary_interests',
    db.Column('weekly_signup_id', db.Integer, db.ForeignKey('weekly_signups.id'), primary_key=True),
    db.Column('primary_interest_id', db.Integer, db.ForeignKey('primary_interests.primary_interest_id'), primary_key=True)
)


class SecondaryInterest(db.Model):
    """The secondary interests students have chosen"""

    __tablename__ = 'secondary_interests'
    id = db.Column(db.Integer, primary_key=True)
    secondary_interest_name = db.Column(db.Text, primary_key=True, nullable=False)

    def __init__(self, secondary_interest_name):
        self.secondary_interest_name = secondary_interest_name

    def __repr__(self):
        return f" Secondary Interest: {self.id} - {self.secondary_interest_name} "


weekly_signup_secondary_interest = db.Table('weekly_signups_secondary_interests',
    db.Column('weekly_signup', db.Integer, db.ForeignKey('weekly_signups.id'), primary_key=True),
    db.Column('secondary_interest', db.Integer, db.ForeignKey('secondary_interests.id'), primary_key=True)
)


class MatchedInterest(db.Model):
    """The list if interest the student wants to match on"""

    __tablename__ = 'matched_interests'
    id = id = db.Column(db.Integer, primary_key=True)
    matched_interest_name = db.Column(db.Text, primary_key=True, nullable=False)

    def __init__(self, matched_interest_name):
        self.matched_interest_name = matched_interest_name

    def __repr__(self):
        return f" {self.id} - {self.matched_interest_name} "


student_matched_interest = db.Table('students_matched_interests',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('matched_interest_id', db.Integer, db.ForeignKey('matched_interests.id'), primary_key=True)
)


class Cohort(db.Model):
    """This is a list of cohorts ever to exist on MCIT Online"""

    __tablename__ = 'cohorts'
    id = db.Column(db.Integer, primary_key=True)
    cohort_name = db.Column(db.Text, primary_key=True, nullable=False)

    def __init__(self, cohort_name):
        self.cohort_name = cohort_name

    def __repr__(self):
        return f"{self.id} - {self.cohort_name} "


class PrimaryTimePreference(db.Model):
    """The primary times preferences students have"""
    # how do we input data to this table?
    # for reference why I commented out students:

    # see using backref

    __tablename__ = 'primary_time_preferences'

    id = db.Column(db.Integer, primary_key=True)
    primary_time_preference_name = db.Column(db.Text, primary_key=True, nullable=False)

    def __init__(self, primary_time_preference_name):
        self.primary_time_preference_name = primary_time_preference_name

    def __repr__(self):
        return f" Primary Time Preference: {self.id} - {self.primary_time_preference_name} "


weekly_signup_primary_time_preference = db.Table('weekly_signups_primary_time_preferences',
    db.Column('weekly_signup', db.Integer, db.ForeignKey('weekly_signups.id'), primary_key=True),
    db.Column('primary_time_preference', db.Integer, db.ForeignKey('primary_time_preferences.id'), primary_key=True)
)


class SecondaryTimePreference(db.Model):
    """The secondary times preferences students have"""

    __tablename__ = 'secondary_time_preferences'

    id = id = db.Column(db.Integer, primary_key=True)
    secondary_time_preference_name = db.Column(db.Text, primary_key=True, nullable=False)

    def __init__(self, secondary_time_preference_name):
        self.secondary_time_preference_name = secondary_time_preference_name

    def __repr__(self):
        return f" Secondary Time Preference: {self.d} - {self.secondary_time_preference_name} "


weekly_signup_secondary_time_preference = db.Table('weekly_signups_secondary_time_preferences',
    db.Column('weekly_signup', db.Integer, db.ForeignKey('weekly_signups.id'), primary_key=True),
    db.Column('secondary_time_preference', db.Integer, db.ForeignKey('secondary_time_preferences.id'), primary_key=True)
)


class NetworkingGoal(db.Model):
    """This table is used to store the all networking goals for
    students to choose from for their PennChats meetings.
    Currently contains only two goals: match by class, match by interest.
    There are two many to one relationships between this table and the WeeklySignUp table."""
    # how do we input data to this table?

    __tablename__ = 'networking_goals'
    id = db.Column(db.Integer, primary_key=True)
    networking_goal = db.Column(db.Text, nullable=False, primary_key=True)

    def __init__(self, networking_goal):
        self.networking_goal = networking_goal

    def __repr__(self):
        return f" Networking Goal: {self.id}. {self.networking_goal}"


class Meeting(db.Model):
    """This table describes all the meetings that has been set up.
    A final output of the matching algorithm will be a list of Meeting objects.
    There is a many-to-many relationship between this table and the Student table."""

    __tablename__ = 'meetings'
    id = db.Column(db.Integer, primary_key=True)
    time_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer)
    interest_id = db.Column(db.Integer)

    # one to many relationship
    week_of_meeting = db.Column(db.String, db.ForeignKey('week_of_meetings.week_of_meeting_name'), primary_key=True, nullable=False)

    def __init__(self, week_of_meeting, time_id, course_id=None, interest_id=None):
        self.week_of_meeting = week_of_meeting
        self.time_id = time_id
        self.course_id = course_id
        self.interest_id = interest_id

    def __repr__(self):
        return f"Meeting instance. ID: {self.id}, meeting week: {self.week_of_meeting}, time_id: {self.time_id}, associated students: {self.students}."


# many to many association table
groupings = db.Table('groupings',
        db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
        db.Column('meeting_id', db.Integer, db.ForeignKey('meetings.id'), primary_key=True)

)


class UnmatchedStudents(db.Model):
    """This table records all the students who were not able to be matched.
    A final output of the matching algorithm will be a list of UnmatchedStudnets
    objects."""

    __tablename__ = 'unmatched_students'

    student_id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

    # one to many relationship
    week_of_meeting = db.Column(db.String, db.ForeignKey('week_of_meetings.week_of_meeting_name'), nullable=False)

    def __init__(self, week_of_meeting_name, student_id, email, firstname, lastname):
        self.week_of_meeting_name = week_of_meeting_name
        self.student_id = student_id
        self.email = email
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return f"Unmatched student: {self.firstname} {self.lastname}, {self.student_id}, and {self.email}. Unmatched week: {self.week_of_meeting_name}"



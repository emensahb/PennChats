from sqlalchemy import DateTime, func

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
    student_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
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

   # updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())
   # created_at = db.Column(DateTime(timezone=True),server_default=func.now())

    # profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')

    # many to many relationships
    class_enrolled = db.relationship('ClassEnrolled', secondary='students_classes_enrolled', backref='student')
    class_taken_id = db.relationship('ClassTaken', secondary='students_classes_taken', backref='student')
    interests = db.relationship('Interest', secondary='students_interests', backref='student')
    meetings = db.relationship('Meeting', secondary='groupings', backref='student')

    # ont-to-many relationships
    matched_class_num = db.Column(db.Integer, db.ForeignKey('matched_classes.matched_class_num'))
    cohort_name = db.Column(db.Text, db.ForeignKey('cohorts.cohort_name'))
    primary_interest_name = db.Column(db.Text, db.ForeignKey('primary_interests.primary_interest_name'))
    secondary_interest_name = db.Column(db.Text, db.ForeignKey('secondary_interests.secondary_interest_name'))
    networking_goal_name = db.Column(db.Text, db.ForeignKey('networking_goals.networking_goal_name'))

    # many-to-one relationships
    weekly_signup = db.relationship('WeeklySignUp', backref='student')

    def __init__(self, email, username, student_id, password):
        self.username = username
        self.student_id = student_id
        self.password_hash = generate_password_hash(password)
        self.email = email

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"{self.firstname}  {self.lastname} has email: {self.email} and student ID: {self.student_id}"


class WeekOfMeeting(db.Model):
    """This table will store all the available weeks that students to sign up
        for PennChats. The table will be queried to provide options for students to
        fill out their WeeklySignUp forms.
        There is a many torelationship between this table and the WeeklySignUp
        table."""

    __tablename__ = 'week_of_meetings'
    id = db.Column(db.Integer, primary_key=True, nullable=True, autoincrement=True)
    week_of_meeting_name = db.Column(db.Text, primary_key=True, unique=True, nullable=False)
    # weekly_signup = db.Column(db.Integer, db.ForeignKey('weekly_signup.id'), nullable=False)
    weekly_signup = db.relationship("WeeklySignUp", backref='week_of_meeting')
    # many to one relationship)
    # weekly_signups = db.relationship('WeeklySignUp', backref='week_of_meeting')
    # meetings = db.relationship('Meeting', backref='week_of_meeting')
    # unmatched_students = db.relationship('UnmatchedStudents', backref='week_of_meeting')

    def __init__(self, id, week_of_meeting_name):
        self.id = id
        self.week_of_meeting_name = week_of_meeting_name

    def __repr__(self):
        return f"Meeting week: {self.week_of_meeting_name}."


class WeeklySignUp(db.Model):
    """
    A list of students who are signed up to chat this week
    """
    __tablename__ = 'weekly_signups'

    id = db.Column(db.Integer, primary_key=True, nullable=True, autoincrement=True)
    week_of_meeting_name = db.Column(db.Text, db.ForeignKey('week_of_meetings.week_of_meeting_name'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))

    primary_time_preference = db.relationship("PrimaryTimePreference", backref='weekly_signup')
    secondary_time_preference = db.relationship("SecondaryTimePreference", backref='weekly_signup')

    def __init__(self, id, week_of_meeting_name, student_id):
        self.id = id
        self.week_of_meeting_name = week_of_meeting_name
        self.student_id = student_id

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
    The class the student wants to match on
    Many to One
    """

    __tablename__ = 'matched_classes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    matched_class_num = db.Column(db.Integer, unique=True, nullable=False)
    matched_class_name = db.Column(db.Text, unique=True, nullable=False)
    students = db.relationship('Student', backref='matched_class')

    def __init__(self, id, matched_class_num, matched_class_name):
        self.id = id
        self.matched_class_num = matched_class_num
        self.matched_class_name = matched_class_name

    def __repr__(self):
        return f"{self.matched_class_num} - {self.matched_class_name} "


class Interest(db.Model):
    """This table is used to store all interests we plan to provide as options for students to choose from
    when they fill out their user profile.
    There is a many to many relationship between this table and the student table."""
    # how do we input data to this table?

    __tablename__ = 'interests'

    id = db.Column(db.Integer, primary_key=True)
    interest_name = db.Column(db.Text, nullable=False, unique=True)

    def __init__(self, id, interest_name):
        self.id = id
        self.interest_name = interest_name

    def __repr__(self):
        return f"Interest: {self.id}. {self.interest_name}"


student_interest = db.Table('students_interests',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True),
    db.Column('interest_id', db.Integer, db.ForeignKey('interests.id'), primary_key=True)
)


class PrimaryInterest(db.Model):
    """
    The primary interests students have chosen
    An association table between Primary Interest and students
    """

    __tablename__ = 'primary_interests'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    primary_interest_name = db.Column(db.Text, primary_key=True, unique=True, nullable=False)
    students = db.relationship('Student', backref='primary_interest')

    def __init__(self, id, primary_interest_name):
        self.id = id
        self.primary_interest_name = primary_interest_name

    def __repr__(self):
        return f" Primary Interest:{self.primary_interest_name}"


# weekly_signup_primary_interest = db.Table('weekly_signups_primary_interests',
#    db.Column('weekly_signup_id', db.Integer, db.ForeignKey('weekly_signups.id'), primary_key=True),
#    db.Column('primary_interest_id', db.Integer,
#    db.ForeignKey('primary_interests.primary_interest_id'), primary_key=True)
#)


class SecondaryInterest(db.Model):
    """
    The secondary interests students have chosen
    """
    __tablename__ = 'secondary_interests'
    id = db.Column(db.Integer, primary_key=True)
    secondary_interest_name = db.Column(db.Text, unique=True, nullable=False)
    students = db.relationship('Student', backref='secondary_interest')

    def __init__(self, id, secondary_interest_name):
        self.id = id
        self.secondary_interest_name = secondary_interest_name

    def __repr__(self):
        return f" Secondary Interest: {self.id} - {self.secondary_interest_name} "


# weekly_signup_secondary_interest = db.Table('weekly_signups_secondary_interests',
#    db.Column('weekly_signup', db.Integer, db.ForeignKey('weekly_signups.id'), primary_key=True),
 #   db.Column('secondary_interest', db.Integer, db.ForeignKey('secondary_interests.id'), primary_key=True)
#)


class Cohort(db.Model):
    """This is a list of cohorts ever to exist on MCIT Online"""

    __tablename__ = 'cohorts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cohort_name = db.Column(db.Text, primary_key=True, unique=True, nullable=False)
    students = db.relationship('Student', backref='cohort')

    def __init__(self, id, cohort_name):
        self.id = id
        self.cohort_name = cohort_name

    def __repr__(self):
        return f"{self.cohort_name}"


class PrimaryTimePreference(db.Model):
    """The primary times preferences students have"""

    __tablename__ = 'primary_time_preferences'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    primary_time_preference_name = db.Column(db.Text, primary_key=True, nullable=False)
    weekly_signup_id = db.Column(db.Integer, db.ForeignKey('weekly_signups.id'), nullable=False)

    def __init__(self, id, primary_time_preference_name, weekly_signup_id):
        self.id = id
        self.primary_time_preference_name = primary_time_preference_name
        self.weekly_signup_id = weekly_signup_id 

    def __repr__(self):
        return f" Primary Time Preference: {self.id} - {self.primary_time_preference_name} "


# weekly_signup_primary_time_preference = db.Table('weekly_signups_primary_time_preferences',
#    db.Column('weekly_signup', db.Integer, db.ForeignKey('weekly_signups.id'), primary_key=True),
#    db.Column('primary_time_preference', db.Integer, db.ForeignKey('primary_time_preferences.id'), primary_key=True)
#)


class SecondaryTimePreference(db.Model):
    """The secondary times preferences students have"""

    __tablename__ = 'secondary_time_preferences'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    secondary_time_preference_name = db.Column(db.Text, unique=True, nullable=False)
    weekly_signup_id = db.Column(db.Integer, db.ForeignKey('weekly_signups.id'), nullable=False)

    def __init__(self, id, secondary_time_preference_name, weekly_signup_id):
        self.id = id
        self.secondary_time_preference_name = secondary_time_preference_name
        self.weekly_signup_id = weekly_signup_id

    def __repr__(self):
        return f" Secondary Time Preference: {self.id} - {self.secondary_time_preference_name} "


# weekly_signup_secondary_time_preference = db.Table('weekly_signups_secondary_time_preferences',
#    db.Column('weekly_signup', db.Integer, db.ForeignKey('weekly_signups.id'), primary_key=True),
#    db.Column('secondary_time_preference', db.Integer, db.ForeignKey('secondary_time_preferences.id'), primary_key=True)
#)


class NetworkingGoal(db.Model):
    """This table is used to store the all networking goals for
    students to choose from for their PennChats meetings.
    Currently contains only two goals: match by class, match by interest.
    There are two many to one relationships between this table and the WeeklySignUp table."""
    # how do we input data to this table?

    __tablename__ = 'networking_goals'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    networking_goal_name = db.Column(db.Text, nullable=False, unique=True)
    student = db.relationship('Student', backref='networking_goal')

    def __init__(self, id, networking_goal_name):
        self.id = id
        self.networking_goal_name = networking_goal_name

    def __repr__(self):
        return f" Networking Goal: {self.networking_goal_name}"


class Meeting(db.Model):
    """This table describes all the meetings that has been set up.
    A final output of the matching algorithm will be a list of Meeting objects.
    There is a many-to-many relationship between this table and the Student table."""

    __tablename__ = 'meetings'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    time_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer)
    interest_id = db.Column(db.Integer)

    # one to many relationship
    week_of_meeting = db.Column(db.String, db.ForeignKey('week_of_meetings.week_of_meeting_name'), primary_key=True, nullable=False)

    def __init__(self, id, week_of_meeting, time_id, course_id=None, interest_id=None):
        self.id = id
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
    firstname = db.Column(db.Text)
    lastname = db.Column(db.Text)

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


db.create_all()
# db.drop_all()
# db.drop("matched_classes")
# enrolled classes
ec1 = ClassEnrolled(591, "Intro to Software Development")
ec2 = ClassEnrolled(592, "Math Foundations of Computer Science")
ec3 = ClassEnrolled(593, "Intro to Computer Systems")
ec4 = ClassEnrolled(594, "Data Structures and Software Design")
ec5 = ClassEnrolled(595, "Computer Systems Programming")
ec6 = ClassEnrolled(596, "Algorithms & Computation")
ec7 = ClassEnrolled(515, "Fundamentals of Linear Algebra & Optimization")
ec8 = ClassEnrolled(547, "Software Analysis")
ec9 = ClassEnrolled(549, "Wireless Communication for Mobile Networks")
ec10 = ClassEnrolled(581, "Computer Vision & Computational Photography")

# taken classes
tc1 = ClassTaken(591, "Intro to Software Development")
tc2 = ClassTaken(592, "Math Foundations of Computer Science")
tc3 = ClassTaken(593, "Intro to Computer Systems")
tc4 = ClassTaken(594, "Data Structures and Software Design")
tc5 = ClassTaken(595, "Computer Systems Programming")
tc6 = ClassTaken(596, "Algorithms & Computation")
tc7 = ClassTaken(515, "Fundamentals of Linear Algebra & Optimization")
tc8 = ClassTaken(547, "Software Analysis")
tc9 = ClassTaken(549, "Wireless Communication for Mobile Networks")
tc10 = ClassTaken(581, "Computer Vision & Computational Photography")

# Matched classes
mc1 = MatchedClass(1, 591, "Intro to Software Development")
mc2 = MatchedClass(2, 592, "Math Foundations of Computer Science")
mc3 = MatchedClass(3, 593, "Intro to Computer Systems")
mc4 = MatchedClass(4, 594, "Data Structures and Software Design")
mc5 = MatchedClass(5, 595, "Computer Systems Programming")
mc6 = MatchedClass(6, 596, "Algorithms & Computation")
mc7 = MatchedClass(7, 515, "Fundamentals of Linear Algebra & Optimization")
mc8 = MatchedClass(8, 547, "Software Analysis")
mc9 = MatchedClass(9, 549, "Wireless Communication for Mobile Networks")
mc10 = MatchedClass(10, 581, "Computer Vision & Computational Photography")

# Interests
i1 = Interest(1, "Artificial Intelligence & Machine Learning")
i2 = Interest(2, "Blockchain")
i3 = Interest(3, "Cybersecurity & Cryptography")
i4 = Interest(4, "Data Science")
i5 = Interest(5, "Game Design")
i6 = Interest(6, "Interview Prep")
i7 = Interest(7, "Mathematics for Computer Science")
i8 = Interest(8, "Networking & Computer Systems")
i9 = Interest(9, "Project Management")
i10 = Interest(10,"Software Development")

# Primary Interests
pi1 = PrimaryInterest(1, "Artificial Intelligence & Machine Learning")
pi2 = PrimaryInterest(2, "Blockchain")
pi3 = PrimaryInterest(3, "Cybersecurity & Cryptography")
pi4 = PrimaryInterest(4, "Data Science")
pi5 = PrimaryInterest(5, "Game Design")
pi6 = PrimaryInterest(6, "Interview Prep")
pi7 = PrimaryInterest(7, "Mathematics for Computer Science")
pi8 = PrimaryInterest(8, "Networking & Computer Systems")
pi9 = PrimaryInterest(9, "Project Management")
pi10 = PrimaryInterest(10, "Software Development")

# Secondary Interests
si1 = SecondaryInterest(1, "Artificial Intelligence & Machine Learning")
si2 = SecondaryInterest(2, "Blockchain")
si3 = SecondaryInterest(3, "Cybersecurity & Cryptography")
si4 = SecondaryInterest(4, "Data Science")
si5 = SecondaryInterest(5, "Game Design")
si6 = SecondaryInterest(6, "Interview Prep")
si7 = SecondaryInterest(7, "Mathematics for Computer Science")
si8 = SecondaryInterest(8, "Networking & Computer Systems")
si9 = SecondaryInterest(9, "Project Management")
si10 = SecondaryInterest(10,"Software Development")


# cohort
cht1 = Cohort(1, "Spring 2019")
cht2 = Cohort(2, "Fall 2019")
cht3 = Cohort(3, "Spring 2020")
cht4 = Cohort(4, "Fall 2020")
cht5 = Cohort(5, "Spring 2021")
cht6 = Cohort(6, "Fall 2021")

# networking goals options
ng1 = NetworkingGoal(1, "class")
ng2 = NetworkingGoal(2, "interest")

# Primary Time preference
ptp1 = PrimaryTimePreference(1, "Morning: 9am ET", 1)
ptp2 = PrimaryTimePreference(2, "Afternoon: 3pm ET",2)
ptp3 = PrimaryTimePreference(3, "Evening: 7pm ET", 3)
ptp4 = PrimaryTimePreference(4, "Overnight: 1am ET",4)

# Secondary time preference
stp1 = SecondaryTimePreference(1, "Morning: 9am ET", 1)
stp2 = SecondaryTimePreference(2, "Afternoon: 3pm ET", 2)
stp3 = SecondaryTimePreference(3, "Evening: 7pm ET", 3)
stp4 = SecondaryTimePreference(4, "Overnight: 1am ET", 4)

st1 = Student("tester@tester.com", "test123", 123456, "test1234")  # student

wm1 = WeekOfMeeting(1, "Aug 2")
wm2 = WeekOfMeeting(2, "Aug 9")
wm3 = WeekOfMeeting(3, "Aug 16")
wm4 = WeekOfMeeting(4, "Aug 23")
wm5 = WeekOfMeeting(5, "Aug 30")
wm6 = WeekOfMeeting(6, "Sep 5")
wm7 = WeekOfMeeting(7, "Sep 12")
wm8 = WeekOfMeeting(8, "Sep 19")
wm9 = WeekOfMeeting(9, "Sep 26")
wm10 = WeekOfMeeting(10, "Oct 3")
wm11 = WeekOfMeeting(11, "Oct 10")
wm12 = WeekOfMeeting(12, "Oct 17")
wm13 = WeekOfMeeting(13, "Oct 24")
wm14 = WeekOfMeeting(14, "Oct 31")
wm15 = WeekOfMeeting(15, "Nov 7")
wm16 = WeekOfMeeting(16, "Nov 14")
wm17 = WeekOfMeeting(17, "Nov 21")
wm18 = WeekOfMeeting(18, "Nov 28")
wm19 = WeekOfMeeting(19, "Dec 5")
wm20 = WeekOfMeeting(20, "Dec 12")


#weekly signup
ws1 = WeeklySignUp(1, "Aug 2", 12346)
ws2 = WeeklySignUp(2, "Aug 9", 12346)
ws3 = WeeklySignUp(3, "Aug 16", 12346)
ws4 = WeeklySignUp(4, "Aug 23", 12346)
ws5 = WeeklySignUp(5, "Aug 30", 12346)
ws6 = WeeklySignUp(6, "Sep 5", 12346)
ws7 = WeeklySignUp(7, "Sep 12", 12346)
ws8 = WeeklySignUp(8, "Sep 19", 12346)
ws9 = WeeklySignUp(9, "Sep 26", 12346)
ws10 = WeeklySignUp(10, "Oct 3", 12346)


# db.session.add_all([mc1, mc2, mc3, mc4, mc5, mc6, mc7,
# mc8, mc9, mc10])  # matched classes
# db.session.add_all([pi1, pi2, pi3, pi4, pi5, pi6, pi7, pi8, pi9, pi10])  # primary interests
# db.session.add_all([si1, si2, si3, si4, si5, si6, si7, si8, si9, si10])  # secondary interests
# db.session.add_all([cht1, cht2, cht3, cht4, cht5, cht6])  # cohorts
# db.session.add_all([ng1, ng2])
# db.session.add_all([wm1, wm2, wm3, wm4, wm5, wm6, wm7, wm8, wm9, wm10, wm11, wm12,
# wm13, wm14, wm15, wm16, wm17, wm18, wm19, wm20])  # week meet
# db.session.add_all([ws1, ws2, ws3, ws4, ws5, ws6, ws7, ws8, ws9, ws10])  # weekly signup
# db.session.add_all([st1])
# db.session.add_all([ptp1, ptp2, ptp3, ptp4])  # primary time preferences
# db.session.add_all([stp1, stp2, stp3, stp4])  # secondary time preferences


db.session.commit()

print(PrimaryInterest.query.all())


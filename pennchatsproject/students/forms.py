# pennchatsproject/students/forms.py
# contains form classes that are used to create and update student profiles
# this will include all the forms Audra has in her forms.py file

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo  # URL
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from pennchatsproject.models import *


def cohort_query():
    return Cohort.query


def interest_query():
    return Interest.query


def course_query():
    return Course.query

class MultipleCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class ProfileForm(FlaskForm):

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State/Province', validators=[DataRequired()])
    country = StringField('Country/Territory', validators=[DataRequired()])
    linkedin = StringField('LinkedIn', validators=[URL()])
    bio = TextAreaField('Brief Bio (optional)')

    # Class
    class_list = ['CIT591: Introduction to Software Development',
                  'CIT592: Mathematical Foundations of CS',
                  'CIT593: Introduction to Computer Systems',
                  'CIT594: Data Structures & Software Design',
                  'CIT595: Computer Systems Programming',
                  'CIT596: Algorithms & Computation',
                  'CIS515: Math for Machine Learning',
                  'CIS521: Artificial Intelligence',
                  'CIS547: Software Analysis',
                  'CIS549: Wireless Communications',
                  'CIS550: Database & Information Systems',
                  'CIS581: Computer Vision & Photography',
                  'CIS520: Intro to Robotics',
                  'CIS582: Blockchains & Cryptography',
                  'ESE542: Statistics for Data Science']
    # Gets the list of courses from the DB
    # class_list = [x.course_id for x in Course.query.all()]
    # create value/label pairs (should both be str for name of class)
    class_tuples = [(x, x) for x in class_list]
    # current courses
    current_courses = MultipleCheckboxField(
        'Current Courses', choices=class_tuples)
    # past courses
    past_courses = MultipleCheckboxField('Past Courses', choices=class_tuples)
    # preferred course to be matched on
    course_id_to_match = SelectField(
        'Preferred course to be matched with',
        validators=[DataRequired()],
        choices=class_tuples,
    )

    # Interest
    interest_name_list = ['Artificial Intelligence & Machine Learning', 'Blockchain', 'Cybersecurity & Cryptography',
    'Data Science', 'Game Design', 'Interview Prep', 'Mathematics for Computer Science',
    'Networking & Computer Systems', 'Project Management', 'Software Development']
    interest_id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # interest_id_list = [x.interest_id for x in Interest.query.all()]
    # interest_name_list = [y.interest_name for y in Interest.query.all()]
    # create value/label pairs (should both be str for name of interest)
    interest_tuples = list(
        map(lambda x, y: (x, y), interest_id_list, interest_name_list))
    interests = MultipleCheckboxField('Interests', choices=interest_tuples)
    # preferred interest to be matched on
    interest_id_to_match = SelectField(
        'Preferred interest to be matched with',
        validators=[DataRequired()],
        choices=interest_tuples,
    )

    # Cohort
    cohort_list=[
    'Spring 2018',
    'Fall 2018',
    'Spring 2019',
    'Fall 2019',
    'Spring 2020',
    'Fall 2020',
    'Spring 2021',
    'Fall 2021'
    ]
    cohort_id_list = [1, 2, 3, 4, 5, 6, 7, 8]
    # Gets the list of courses from the DB
    # cohort_list = [x.cohort_name for x in Cohort.query.all()]
    # create value/label pairs (should both be str for name of cohort)
    cohort_tuples = list(
            map(lambda x, y: (x, y), cohort_id_list, cohort_list))
    cohort = MultipleCheckboxField('MCIT Cohort', choices=cohort_tuples)

    # Submit
    submit = SubmitField('Update Profile')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    student_id = StringField('Student ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'pass_confirm', message='Passwords must match!')])
    pass_confirm = PasswordField(
        'Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email):
        """this function will check to see if the given email has already been registered."""
        if Student.query.filter_by(email=self.email.data).first():
            raise ValidationError('This email has already been registered.')

    def validate_username(self, username):
        """this function will check to see if the given username has already been registered."""
        if Student.query.filter_by(username=self.username.data).first():
            raise ValidationError('This username is already taken.')

    def validate_student_id(self, student_id):
        """this function will check to see if the given student_id has already been registered."""
        if Student.query.filter_by(student_id=self.student_id.data).first():
            raise ValidationError(
                'This student ID has already been registered.')


class ProfileForm(FlaskForm):

    # Basic Info
    username = StringField('Username')
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    city = StringField('City')
    state = StringField('State/Province')
    country = StringField('Country/Territory')
    linkedin = StringField('LinkedIn')
    bio = TextAreaField('Brief Bio (optional)')

    # Course
    # Gets the list of courses from the DB & create class list to choose
    class_list = [x.course_id for x in Course.query.all()]
    class_tuples = [(x, x) for x in class_list]
    current_courses = QuerySelectMultipleField(
        query_factory=course_query, allow_blank=True, get_label='course_id')
    past_courses = QuerySelectMultipleField(
        query_factory=course_query, allow_blank=True, get_label='course_id')
    course_id_to_match = SelectField(
        'Preferred course to be matched with',
        validators=[DataRequired()],
        choices=class_tuples,
    )

    # Interest
    interest_id_list = [x.interest_id for x in Interest.query.all()]
    interest_name_list = [y.interest_name for y in Interest.query.all()]
    # create value/label pairs (should both be str for name of interest)
    interest_tuples = list(
        map(lambda x, y: (x, y), interest_id_list, interest_name_list))
    interests = QuerySelectMultipleField(
        query_factory=interest_query, allow_blank=True, get_label='interest_name')
    interest_id_to_match = SelectField(
        'Preferred interest to be matched with',
        validators=[DataRequired()],
        choices=interest_tuples,
    )

    # Cohort
    cohort_list = [x.cohort_name for x in Cohort.query.all()]
    cohort_tuples = [(x, x) for x in cohort_list]
    cohort = SelectField('MCIT Cohort', choices=cohort_tuples)
    # cohort = QuerySelectField(
    #     query_factory=cohort_query, allow_blank=True, get_label='cohort_name')

    # Submit
    submit = SubmitField('Update Profile')


class WeeklySignUpForm(FlaskForm):

    # week_meet list (hard-code for now)
    # week_meet_list = ['Aug 2', 'Aug 9', 'Aug 16',
    #                   'Aug 23', 'Aug 30', 'Sept 6', 'Sept 13',
    #                   'Sept 20', 'Sept 27']
    week_meet_list = [x.week_meet_name for x in WeekMeet.query.all()]
    # create value/label pairs (should both be str for week_meet)
    week_meet_tuples = [(x, x) for x in week_meet_list]
    # week_meet = DateTimeField('Week Meet', format='%Y-%m-%dT%H:%M:%S', default=datetime.today, validators=[DataRequired()])
    week_meet = SelectField(
        'Which week you would like to meet for PennChats? (Please do not submit more than one form for the same week)',
        validators=[DataRequired()],
        choices=week_meet_tuples,
    )

    # Prime Time & Sec Time
    # time_id_list = [1, 2, 3, 4]
    # time_option_list = ['Morning: 9am ET', 'Afternoon: 3pm ET', 'Evening: 7pm ET',
    #                     'Overnight: 1am ET']
    time_id_list = [x.time_id for x in TimeOption.query.all()]
    time_option_list = [y.time_option for y in TimeOption.query.all()]
    # create value/label pairs (should both be str for name of interest)
    time_tuples = list(
        map(lambda x, y: (x, y), time_id_list, time_option_list))
    prime_time_id = SelectField(
        'Ideal Time to meet',
        validators=[DataRequired()],
        choices=time_tuples,
    )
    sec_time_id = SelectField(
        'Alternative Time to meet',
        validators=[DataRequired()],
        choices=time_tuples,
    )

    # Prime Goal & Sec Goal
    # goal_id_list = [1, 2]
    # goal_name_list = ['Match by Course', 'Match by Interest']
    goal_id_list = [x.networking_goal_id for x in NetworkingGoal.query.all()]
    goal_name_list = [y.networking_goal for y in NetworkingGoal.query.all()]
    # create value/label pairs (should both be str for name of goal)
    goal_tuples = list(map(lambda x, y: (x, y), goal_id_list, goal_name_list))
    prime_networking_goal_id = SelectField(
        'Networking Goal',
        validators=[DataRequired()],
        choices=goal_tuples,
    )
    sec_networking_goal_id = SelectField(
        'Alternative Goal',
        validators=[DataRequired()],
        choices=goal_tuples,
    )

    # Submit
    submit = SubmitField('Sign Up for PennChats')

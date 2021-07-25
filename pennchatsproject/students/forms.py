# pennchatsproject/students/forms.py
# contains form classes that are used to create and update student profiles
# this will include all the forms Audra has in her forms.py file

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, widgets, SelectMultipleField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, URL
from wtforms import ValidationError

from flask_login import current_user
from pennchatsproject.models import Student

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
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def validate_email(self, email):
        """this function will check to see if the given email has already been registered."""
        if Student.query.filter_by(email=self.email.data).first():
            raise ValidationError('This email has already been registered.')

    def validate_username(self, field):
        """this function will check to see if the given username has already been registered."""
        if Student.query.filter_by(username=self.username.data).first():
            raise ValidationError('This username is already taken.')

    def validate_student_id(self, field):
        """this function will check to see if the given student_id has already been registered."""
        if Student.query.filter_by(student_id=self.student_id.data).first():
            raise ValidationError('This student ID has already been registered.')

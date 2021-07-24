# pennchatsproject/students/forms.py
# contains form classes that are used to create and update student profiles
# this will include all the forms Audra has in her forms.py file

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, widgets, SelectMultipleField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, URL
from wtforms import ValidationError

from flask_login import current_user
from pennchatsproject.models import *


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

    # def validate_username(self, field):
        # """this function will check to see if the given username has already been registered."""
       #  if Student.query.filter_by(username=self.username.data).first():
        #    raise ValidationError('This username is already taken.')

    def validate_student_id(self, field):
        """this function will check to see if the given student_id has already been registered."""
        if Student.query.filter_by(student_id=self.student_id.data).first():
            raise ValidationError('This student ID has already been registered.')


# Checkboxes
class MultipleCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


# Profile form
class ProfileForm(FlaskForm):

    # Class list
    #class_list = ['CIT591', 'CIT592', 'CIT593', 'CIT594', 'CIT595', 'CIT596', 'CIS515', 'CIS521', 'CIS547', 'CIS549',
                  # 'CIS550', 'CIS581', 'CIS520', 'CIS582', 'ESE542']

    matched_class_list = [x.id for x in MatchedClass.query.all()]  # Gets the list of classes from the DB

    # create value/label pairs (should both be str for name of class)
    matched_class_tuples = [(x, x) for x in matched_class_list]

    # first choice class
    primary_class = SelectField(
        'First choice class (for matching)',
        [DataRequired()],
        choices=matched_class_tuples,
    )

    # second choice class
    secondary_class = SelectField(
        'Second choice class (for matching)',
        [DataRequired()],
        choices=matched_class_tuples,
    )

    # create checkboxes for classes
    classes_checkboxes = MultipleCheckboxField('What classes have you taken?', choices=matched_class_tuples)

    current_class = MultipleCheckboxField('What classes are you currently taking?', choices=matched_class_tuples)

    first_name = StringField('First Name', validators = [InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    city = StringField('City', validators=[InputRequired()])
    state = SelectField(
        'State',
        choices=[
            ('New York', 'New York'),
            ('Texas', 'Texas'),
            ('NA', 'NA'),
        ]
    )

    country_list = ['United States', 'Canada', 'China']

    country_tuples = [(x, x) for x in country_list]

    country = SelectField(
        'Country',
        [DataRequired()],
        choices=country_tuples
    )

    # Interest list
    # interest_list = ['Artificial Intelligence & Machine Learning', 'Blockchain', 'Cybersecurity & Cryptography',
                     # 'Data Science', 'Game Design', 'Interview Prep', 'Mathematics for Computer Science',
                     # 'Networking & Computer Systems', 'Project Management', 'Software Development']

    primary_interest_list = [x.interest_name for x in PrimaryInterest.query.all()]  # Gets the list of classes from the DB
    # create value/label pairs (should both be str for name of class)
    primary_interest_tuples = [(x, x) for x in primary_interest_list]

    primary_interest = SelectField(
        'Primary interest',
        [DataRequired()],
        choices=primary_interest_tuples,
    )

    secondary_interest_list = [x.interest_name for x in SecondaryInterest.query.all()]  # Gets the list of classes from the DB
    # create value/label pairs (should both be str for name of class)
    secondary_interest_tuples = [(x, x) for x in secondary_interest_list]
    secondary_interest = SelectField(
        'Secondary interest',
        [DataRequired()],
        choices=secondary_interest_tuples,
    )

    interest_list = [x.interest_name for x in Interest.query.all()]  # Gets the list of classes from the DB
    # create value/label pairs (should both be str for name of class)
    interest_tuples = [(x, x) for x in interest_list]
    other_interests = MultipleCheckboxField('Additional Interests', choices=interest_tuples)

    cohort = SelectField(
        'Cohort',
        [DataRequired()],

        choices=[x.cohort_name for x in Cohort.query.all()]

        #choices=[
           # ('Spring 2018', 'Spring 2018'),
           # ('Fall 2018', 'Fall 2018'),
           # ('Spring 2019', 'Spring 2019'),
           # ('Fall 2019', 'Fall 2019'),
           # ('Spring 2020', 'Spring 2020'),
           # ('Fall 2020', 'Fall 2020'),
           # ('Spring 2021', 'Spring 2021'),
           # ('Fall 2021', 'Fall 2021'),
        #]
    )

    linkedin = StringField('LinkedIn', validators=[URL()])
    bio = StringField('Bio (optional)', validators=[InputRequired()])

    submit = SubmitField('Sign Up')


# Next week meet form
class NextForm(FlaskForm):
    matching = SelectField(  # Networking Goal
        'I would like to be matched by: ',
        [DataRequired()],
        choices=[x.networking_goal for x in NetworkingGoal.query.all()]

       # choices=[
          #  ('classes', 'class.'),  # should classes be ranked?
           # ('interest', 'interest'),
       # ]
    )

    primary_time = SelectField(  # Next week
        'First meeting time preference',
        [DataRequired()],

        choices=[x.time for x in PrimaryTimePreference.query.all()]

        #choices=[
         #   ('morning', 'Morning: 9am ET'),  # should classes be ranked?
          #  ('afternoon', 'Afternoon: 3pm ET'),
          #  ('evening', 'Evening: 7pm ET'),
          #  ('overnight', 'Overnight: 1am ET'),
       # ]
    )

    secondary_time = SelectField(  # Next week
        'Second meeting time preference',
        [DataRequired()],

        choices=[x.time for x in SecondaryTimePreference.query.all()]

        # choices=[
        #    ('morning', 'Morning: 9am ET'),  # should classes be ranked?
         #   ('afternoon', 'Afternoon: 3pm ET'),
         #   ('evening', 'Evening: 7pm ET'),
         #   ('overnight', 'Overnight: 1am ET'),
         #   ]
        )

    match = SubmitField("Match me for next week's chat!")
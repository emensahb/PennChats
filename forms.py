from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, widgets, SelectMultipleField
from wtforms.validators import InputRequired, DataRequired, URL


# Checkboxes
class MultipleCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


# Sign Up form
class SignUpForm(FlaskForm):

    # dummy sign up
    email = StringField('Email', validators = [InputRequired()])
    password = StringField('Password', validators = [InputRequired()])
    confirm_password = StringField('Confirm Password', validators=[InputRequired()])

    # dummy login
    login = SubmitField('Login')

    # Class list
    class_list = ['CIT591', 'CIT592', 'CIT593', 'CIT594', 'CIT595', 'CIT596', 'CIS515', 'CIS521', 'CIS547', 'CIS549',
                  'CIS550', 'CIS581', 'CIS520', 'CIS582', 'ESE542']


    # create value/label pairs (should both be str for name of class)
    class_tuples = [(x, x) for x in class_list]

    # first choice class
    primary_class = SelectField(
        'First choice class (for matching)',
        [DataRequired()],
        choices=class_tuples,
    )

    # second choice class
    secondary_class = SelectField(
        'Second choice class (for matching)',
        [DataRequired()],
        choices=class_tuples,
    )

    # create checkboxes for classes
    class_checkboxes = MultipleCheckboxField('What classes have you taken?', choices=class_tuples)

    current_class = MultipleCheckboxField('What classes are you currently taking?', choices=class_tuples)

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
    interest_list = ['Artificial Intelligence & Machine Learning', 'Blockchain', 'Cybersecurity & Cryptography',
                     'Data Science', 'Blockchain', 'Game Design', 'Interview Prep', 'Mathematics for Computer Science',
                     'Networking & Computer Systems', 'Project Management', 'Software Development']

    # create value/label pairs (should both be str for name of class)
    interest_tuples = [(x, x) for x in interest_list]

    primary_interest = SelectField(
        'Primary interest',
        [DataRequired()],
        choices=interest_tuples,
    )

    secondary_interest = SelectField(
        'Secondary interest',
        [DataRequired()],
        choices=interest_tuples,
    )

    other_interests = MultipleCheckboxField('Additional Interests', choices=interest_tuples)

    cohort = SelectField(
        'Cohort',
        [DataRequired()],
        choices=[
            ('Spring 2018', 'Spring 2018'),
            ('Fall 2018', 'Fall 2018'),
            ('Spring 2019', 'Spring 2019'),
            ('Fall 2019', 'Fall 2019'),
            ('Spring 2020', 'Spring 2020'),
            ('Fall 2020', 'Fall 2020'),
            ('Spring 2021', 'Spring 2021'),
            ('Fall 2021', 'Fall 2021'),
        ]
    )

    linkedin = StringField('LinkedIn', validators=[URL()])
    bio = StringField('Bio (optional)', validators=[InputRequired()])

    primary_time = SelectField(
        'First meeting time preference',
        [DataRequired()],
        choices=[
            ('morning', 'Morning: 9am ET'), # should classes be ranked?
            ('afternoon', 'Afternoon: 3pm ET'),
            ('evening', 'Evening: 7pm ET'),
            ('overnight', 'Overnight: 1am ET'),
        ]
    )

    secondary_time = SelectField(
        'Second meeting time preference',
        [DataRequired()],
        choices=[
            ('morning', 'Morning: 9am ET'), # should classes be ranked?
            ('afternoon', 'Afternoon: 3pm ET'),
            ('evening', 'Evening: 7pm ET'),
            ('overnight', 'Overnight: 1am ET'),
            ('na', 'NA'),
        ]
    )

    matching = SelectField(
        'Please choose your preference in being matched',
        [DataRequired()],
        choices=[
            ('classes', 'I would like to be matched by class.'), # should classes be ranked?
            ('interest', 'I would like to be matched by interest'),
        ]
    )

    submit = SubmitField('Sign Up')


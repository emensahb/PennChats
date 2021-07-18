# pennchatsproject/students/forms.py
# contains form classes that are used to create and update student profiles
# this will include all the forms Audra has in her forms.py file

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipileField, widgets
from wtforms.validators import DataRequired, Email, EqualTo, NotEqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from datetime import datetime

from flask_login import current_user
from pennchatsproject.models import Student


class MultipleCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


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
    submit = SubmitField('Register!')

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
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    student_id = StringField('Student ID', validators=[DataRequired()])
    firstname = StringField('First Name')
    lastname = StringField('Last Name')
    city = StringField('City')
    state = StringField('State')
    country = StringField('Country')
    cohort = StringField('Cohort')
    bio = StringField('Bio')
    linkedin = StringField('LinkedIn Link')
    profile_picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])
                                                                      submit=SubmitField(
                                                                          'Update Profile')

                                                                      #Course list
                                                                      course_list=['CIT591', 'CIT592', 'CIT593', 'CIT594', 'CIT595', 'CIT596',
                                                                                   'CIS515', 'CIS521', 'CIS547', 'CIS549', 'CIS550', 'CIS581',
                                                                                   'CIS520', 'CIS582', 'ESE542']

                                                                      # create value/label pairs (should both be str for name of course)
                                                                      course_tuples=[
                                                                          (x, x) for x in course_list]

                                                                      # Interest list
                                                                      interest_labels=['Artificial Intelligence & Machine Learning', 'Blockchain', 'Cybersecurity & Cryptography',
                                                                                       'Data Science', 'Game Design', 'Interview Prep', 'Mathematics for Computer Science',
                                                                                       'Networking & Computer Systems', 'Project Management', 'Software Development']

                                                                      # Interest values (interest_ids)
                                                                      interest_values=['1', '2', '3',
                                                                                       '4', '5', '6', '7',
                                                                                       '8', '9', '10']

                                                                      # create value/label pairs (zipping them together, and making them a tuple)
                                                                      # did this because interest name cannot be passed as interest_id
                                                                      interest_tuples=tuple(
                                                                          zip(interest_labels, interest_values))

                                                                      # many to many relationships
                                                                      current_courses=MultipleCheckboxField(
            'What courses are you currently taking?', choices=course_tuples)
        past_courses=MultipleCheckboxField(
            'What courses have you taken?', choices=course_tuples)
        interests=MultipleCheckboxField(
            'What are your interests?', choices=interest_tuples)

        # one to many relatinoships
        course_id_to_match=SelectField(
        'Preferred course for matching',
        [DataRequired()],
        choices=course_tuples,
    )

        interest_id_to_match=SelectField(
        'Preferred interest for matching',
        [DataRequired()],
        choices=interst_tuples,
    )

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


        class NextWeekForm(FlaskForm):

        # week_meet list
        week_meet_list=['Aug 2', 'Aug 9', 'Aug 16',
                        'Aug 23', 'Aug 30', 'Sept 6', 'Sept 13',
                        'Sept 20', 'Sept 27']

        # week_meet values (week_meet_ids)
        # week_meet_values = ['1', '2', '3',
        #                  '4', '5', '6', '7',
        #                  '8', '9', '10']

        # create value/label pairs (should both be str for week_meet)
        week_meet_tuples=[(x, x) for x in week_meet_list]

        # week_meet = DateTimeField('Week Meet', format='%Y-%m-%dT%H:%M:%S', default=datetime.today, validators=[DataRequired()])

        week_meet=SelectField(
        'Preferred week for matching',
        [DataRequired()],
        choices=week_meet_tuples,
    )

        prime_time=SelectField('Ideal time', validators=[DataRequired()])
        sec_time=SelectField('Secondary time', validators=[DataRequired(), NotEqualTo(
            'prime_time', message='Secondary time must be different from Ideal time.')])
        networking_goal=SelectField(
            'Matching Preference', validators=[DataRequired()])
        submit=SubmitField('Sign Up')

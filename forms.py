from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired, DataRequired, URL

class SignUpForm(FlaskForm):

    # dummy signup page
    email = StringField('Email', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])
    confirm_password = StringField('Cofirm Password', validators=[InputRequired()])
    submit = SubmitField('Sign Up')

    # dummy login page
    login = SubmitField('Login')

    # create a profile
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
    country = SelectField(
        'Country',
        [DataRequired()],
        choices=[
            ('Canada', 'Canada'),
            ('United States', 'United States'),
        ]
    )
    linkedin = StringField('LinkedIn', validators=[URL()])


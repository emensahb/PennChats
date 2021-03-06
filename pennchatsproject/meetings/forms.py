# pennchatsproject/meetings.forms.py
# contains form classes that are used to generate matches and initialize
# meetings

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms import ValidationError
from flask_login import current_user
from pennchatsproject.models import *


class GenerateMeetingForm(FlaskForm):

    week_meet_list = [x.week_meet_name for x in WeekMeet.query.all()]
    # week_meet_list = ['Aug 2', 'Aug 9', 'Aug 16',
    #                   'Aug 23', 'Aug 30', 'Sept 6', 'Sept 13',
    #                   'Sept 20', 'Sept 27']
    week_meet_tuples = [(x, x) for x in week_meet_list]
    week_meet = SelectField(
        'Select week to match students',
        validators=[DataRequired()],
        choices=week_meet_tuples,
    )

    submit = SubmitField('Generate Meetings')

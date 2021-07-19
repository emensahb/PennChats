# pennchatsprojectmeetings/forms.py
# contains form that is used to generate meetings

from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, widgets, SelectMultipleField
from wtforms.validators import DataRequired
from wtforms import ValidationError

from pennchatsproject.models import *


class GenerateMeetingForm(FlaskForm):
    meeting_week = SelectField(
        'Match meeting for the week of: ',
        [DataRequired()],
        # choices=[x.week_meet for x in WeeklySignUp.query.all()]

        choices=[('Aug 2', 'Aug 2'),
                 ('Aug 9', 'Aug 9'),
                 ('Aug 16', 'Aug 16'),
                 ('Aug 23', 'Aug 23'),
                 ('Aug 30', 'Aug 30'),
                 ]
    )

    submit = SubmitField('Generate Meetings!')

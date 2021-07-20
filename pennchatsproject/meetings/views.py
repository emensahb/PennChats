# pennchatsproject/meetings/views.py
# Jimmy's portion
# contains routing code for x views:
# generate matches, view matches meetings & unmatched students, student-meeting view etc.

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from pennchatsproject import db
# from werkzeug.security import generate_password_hash, check_password_hash
from pennchatsproject.models import *
from pennchatsproject.meetings.matchingalgo import *


meetings = Blueprint('meetings', __name__)


# generate meetings
@meetings.route('/generate', methods=["POST", "GET"])
def generate():
    form = GenerateMeetingForm()

    if form.validate_on_submit():
        # pass the data submitted on the form to week_meet
        week_meet = form.week_meet.data
        # call the main algorithm with the week_meet variable
        matched_meetings, unmatched_students = match_students(week_meet)
        # add new meeting and student objects to session
        for meeting in matched_meetings:
            db.session.add(meeting)
        for student in unmatched_students:
            db.session.add(student)
        # commit new meeting and student object to session
        db.session.commit()
        return redirect(url_for('meetings.results'))
    
    return render_template("generate_meeting.html")

# view results
@meetings.route('/results/<int:week_meet_id>')
def results(week_meet):
    
    # use some query language to grab specific meetings and unmatched students
    
    return render_template('results.html')

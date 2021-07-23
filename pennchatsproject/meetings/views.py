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
# accessible only by admins by typing extension
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
            student_id = student.student_id
            email = student.email
            first_name = student.first_name
            last_name = student.last_name
            # initialize unmatched student object
            unmatched_student = UnmatchedStudents(
                week_meet, student_id, email, first_name, last_name)
            db.session.add(unmatched_student)
        # commit new meeting and unmatched_student objects to session
        db.session.commit()
        return redirect(url_for('meetings.results'))

    return render_template("generate_meeting.html")


# view results
    # accessible only by admins by typing extension
    # currently showing all existing meetings and unmatched students
    # filter func to be added in future updates to filter by week and date
@meetings.route('/results')
def results():

    # use some query language to grab specific meetings and unmatched students
    meetings = Meeting.query.all()
    unmatched_students = UnmatchedStudents.query.all()

    return render_template('results.html', meetings=meetings, unmatched_students=unmatched_students)

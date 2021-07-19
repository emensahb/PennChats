# pennchatsproject/meetings/views.py
# Jimmy's portion
# contains routing code for x views:
# generate matches, view matches meetings & unmatched students, student-meeting view etc.

from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from pennchatsproject import db
from pennchatsproject.models import *
from pennchatsproject.meetings.forms import GenerateMeetingForm
# from pennchatsproject.setup import *
from pennchatsproject.meetings.matchingalgo_easy import *


meetings = Blueprint('meetings', __name__)


# generate meetings
@meetings.route('/generate', methods=["POST", "GET"])
def generate():
    form = GenerateMeetingForm()

    if form.validate_on_submit():
        meeting_week = form.meeting_week.data

        # some other code

        return redirect(url_for('meetings.view'))

    return render_template("generate_meetings.html", form=form)

# algorithm


@meetings.route('/')
def match_students(meeting_week):
    """This is the main function that contains the logic of
    the easy version algorithm, helper funtions are called in this function.
    Returns two lists:
    list of matched meetings and list of unmatched students"""

    # initialize final output lists
    matched_meetings = []
    unmatched_students = []

    # read the forms by calling the form finder helper function
    forms = form_finder(meeting_week)

    # sort by primary time selection by calling helper function
    prim_time_dict = sort_into_dict_two_args(forms, 'prime_time_id')

    # for each key:value pair in the dictionary
    for key, val in prim_time_dict.items():

        # if list size is greater than one
        if len(val) > 1:
            # call the student_id_list_into_student_list helper function
            student_list = student_id_list_into_student_list(val)
            # initialize a Group object with this list of student objects
            group = Group(student_list)
            # print test
            print("New group formed: " + group)
            # initialize a Meeting object with the group object and the key
            meeting = Meeting(group, key)
            # print test
            print("New meeting formed: " + meeting)
            # append Meeting object to list of matched meetings
            matched_meetings.append(meeting)

        # if list size is equal to one
        else:
            # get the student object in the list
            student = student_id_list_into_student_list(val)[0]
            # unmatched student print test
            print("Unmatched student for size=1: " + student)
            # add the student to the list of unmatched students
            unmatched_students.append(student)

    # output two lists
    return matched_meetings, unmatched_students

from pennchatsproject.models import *
from pennchatsproject import db


def match_students(week_meet):
    """This is the main function that contains the logic of
    the easy version algorithm, helper funtions are called in this function.
    To be called after all students have submitted their forms for the 
    given week_meet, matches students into groups based on prime_time_id
    and creates Meeting objects and updates to database.
    Returns two lists:
    list of matched meetings and list of unmatched students"""

    # initialize final output lists
    matched_meetings = []
    unmatched_students = []

    # read the forms by calling the form finder helper function
    forms = form_finder(week_meet)

    # sort by primary time selection by calling helper function
    prim_time_dict = sort_into_dict(forms, 'prime_time_id')

    # for each key:value pair in the dictionary
    for key, val in prim_time_dict.items():

        # if list size is greater than one
        if len(val) > 1:
            # initialize a Meeting object with the time_id stored in the key
            meeting = Meeting(key)
            # call the student_id_list_into_student_list helper function
            student_list = student_id_list_into_student_list(val)
            # for each student in list, create association to meeting
            for student in student_list:
                meeting.students.append(student)
            # print test
            print("New meeting formed: " + meeting)
            # commit new Meeting object to database
            db.session.commit()
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
            # store the student into a unmatched student table in the database

    # output two lists
    return matched_meetings, unmatched_students


def form_finder(week_meet, student_id=None):
    """This is a helper function to query the forms by a given week.
    Returns a list of forms"""

    signup_forms_list = WeeklySignUp.query.filter_by(
                        week_meet=week_meet, student_id=student_id).all()

    return signup_forms_list


def sort_into_dict(signup_forms_list, criteria_id):
    """This is a helper function that takes in a list of
    WeeklySignUp forms, and the sorting criteria_id.
    The function returns a dictionary with key:value pairing where
    the key is the sorting criteria id, and the value being a list of
    Student objects."""

    # initialize an empty list
    criteria_id_list = []

    # iterate through the forms list, read the criteria_id of each form and
    # append it to the empty list
    for form in signup_forms_list:
        # Mix-ups may happen here depends on what gets passed into form.criteria_id
        # criteria_id_list.append(form.prime_time_id) - use in case of error
        criteria_id_list.append(form.criteria_id)

    # print test
    print("Here is a list of all of the ids of the specified criteria in the list of forms (may contain duplicates): " + criteria_id_list)

    # cast the list into a set to get unique criteria_ids
    criteria_id_set = set(criteria_id_list)

    # initialize an empty list to store tuples
    criteria_tuples_list = []

    # iterate thru each criteria_id of the set, initialize a tuple of
    # (criteria_id, []), and append to empty list
    for criteria_id in criteria_id_set:
        criteria_tuples_list.append((criteria_id, []))

    # print test
    print("Here is a list of tuples with empty lists: " + criteria_tuples_list)

    # create the dictionary for output by calling the dict function
    criteria_id_dict = dict(criteria_tuples_list)

    # print test
    print("This should be an empty dict with all criteria_ids setup as keys: " + criteria_id_dict)

    # iterate thru each form again to add student_ids to the dictionary
    # according to the criteria_id key
    for form in signup_forms_list:
        criteria_id_dict[form.criteria_id].append(form.student_id)
        # criteria_id_dict[form.prime_time_id].append(form.student_id)

    # print test
    print("This should be a populated dict after appendings, before output of helper function: " + criteria_id_dict)

    # output dictionary
    return criteria_id_dict


def student_id_list_into_student_list(student_id_list):
    """This helper function turns a list of student_ids into
    a list of student objects, correlated to the student_id.
    Will be calling the query method of the Student table.
    Returns a list of student objects."""

    # initialize empty list as return list
    student_list = []

    # iterate through each student_id stored in the list
    for student_id in student_id_list:
        # read and grab the student object from the student table
        student = Student.query.get(student_id)
        # print test
        print("Queried student: " + student)
        # append the student object to the return list
        student_list.append(student)

    return student_list

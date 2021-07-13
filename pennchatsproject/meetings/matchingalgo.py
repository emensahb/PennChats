from pennchatsproject.models import Group, Student, Meeting

def main():
    """This is the main function that runs the algorithm."""

    # import user information into a list
    all_forms = WeeklySignUp.query.all() # returns a list of weekly signup form objects

    # if list is empty, output N/A, exit program
    if len(all_forms) == 0:
        print("No one signed up this week. No matched meetings and no unmatched students.")
        matched_meetings = []
        unmatched_students = []
        return matched_meetings, unmatched_students
    # if list is not empty, proceed to next step

    #################################################
    ###### sort by primary time selection ###########
    #################################################

    # sort by primary time selection
        # for loop: for each student object in list, read todo the primary_time_selection_id of the student
        # put the student object into a todo PRIME TIME SELECTION DICTIONARY
        # with the primary_time_selection_id as key, and a list of student objects as value
    else:
        # initialize final output lists
        matched_meetings = []
        unmatched_students = []

        # initiate prime time selection list
        prime_time_list = []

        # read prime_time_id of each form from each week's weekly signup
        for form in all_forms:
            prime_time_id = form.prim_time
            prime_time_list.append(prime_time_id)

        # cast the prime_time_list into a set to get unique values
        prime_times = set(prime_time_list)

        # initialize an empty list
        prime_time_tuples_list = []

        # iterate thru each time in prime_times, create a tuple prime_time_id as first item, and an empty list as second item
        for time in prime_times:
            prime_time_tuples_list.append((time, []))

        # create the prime_time_dict dictionary from this list of tuples using the dict function
        prime_time_dict = dict(prime_time_tuples_list)

        # iterate through each form and update the dictionary with student_ids according to the prim_time key
        for form in all_forms:
            prime_time_dict[form.prim_time].append(form.student_id)

        # check how many students are in each time selection group
        # for each key,val pair in the prime_time_dict,
        for key, val in prime_time_dict.items():
            # if size between 2-5, initialize todo a new Group object with all student objects
            if 1<len(val)<6:
                # initialize empty list to store student objects
                students = []
                for student_id in val:
                    # read and grab the student object from the student table by passing in the student_id
                    student = Student.query.get(student_id)
                    # append student object to the list
                    students.append(student)
                # initialize a group object using the list of students
                group = Group(students)
                # initialize a meeting object using the group object and and the primary_time_selection_id used to group these students
                meeting = Meeting(group, key)
                # add this Meeting object to a LIST OF MATCHED MEETINGS
                matched_meetings.append(meeting)
            # if size = 1, add the student to todo a LIST OF UNMATCHED STUDENTS
            elif len(val)==1:
                student = Student.query.get(val[0])
                unmatched_students.append(student)
            # if size > 5, proceed to next step to sort by primary networking goal

            # sort students by primary networking goal
                # for loop: for each student object in the given time selection group, read todo the primary_networking_goal_id
                # of the student, and put the student object into a todo PRIME NETWORKING GOAL DICTIONARY
                # with the primary_networking_goal_id as key, and a list of student objects as value
                # (there will likely be only two keys in this dictionary: match by class & match by interest)

            else:
            

    # sort students by primary networking goal
        # for loop: for each student object in the given time selection group, read todo the primary_networking_goal_id
        # of the student, and put the student object into a todo PRIME NETWORKING GOAL DICTIONARY
        # with the primary_networking_goal_id as key, and a list of student objects as value
        # (there will likely be only two keys in this dictionary: match by class & match by interest)

    # further sort students by type of primary networking goal
        # for loop if condition: for each key in the PRIME NETWORKING GOAL DICTIONARY, compare the primary_networking_goal_id...
            # if the key = "match by class", do the following:
                # for loop: for each student object in the "match by class" list, read the todo first choice class (for matching) id
                # and put the student into a todo SHARED COURSE DICTIONARY
                # with the key being the first choice course_id
                # and the value being a list of students who all have the same course as first choice class
            # if the key = "match by interest", do the following:
                # for loop: for each student object in the "match by interest" list, read the todo first choice primary interest id
                # and put the student into a todo SHARED INTEREST DICTIONARY
                # with the key being the first choice primary interest_id
                # and the value being a list of students who have the same interest as first choice interest

    # check how many students are in each key:value set in the two dictionaries
        # for loop: for each key:value pairing in the two dictionaries above, count the size of the value list
        # if condition:
            # if size between 2-5, initialize a new Group object with all students in the list
                # using the Group object created, the primary_time_selection_id, the course_id/interest_id used to further
                # sort the students, initialize a new Meeting object, and add it to todo the LIST OF MATCHED MEETINGS
            # if size = 1, add the student to todo the LIST OF UNMATCHED STUDENTS
            # if size > 5, proceed to next step to sort by secondary networking goal

    # sort students by secondary networking goal
        # for loop: for each student object in the given time selection group, read todo the secondary_networking_goal_id
        # of the student, and put the student object into a todo SECONDARY NETWORKING GOAL DICTIONARY
        # with the secondary_networking_goal_id as key, and a list of student objects as value
        # (there will likely be only two keys in this dictionary: matchc by class & match by interest)

    # repeat "further sort students by type of primary networking goal" from above and check the number of students in each key:value set

    # check how many students are in each key:value set in the two dictionaries
        # for loop: for each key:value pairing in the two dictionaries above, count the size of the value list
        # if condition:
            # if size between 2-5, initialize a new Group object with all students in the list
                # using the Group object created, the primary_time_selection_id, the first_choice_class id and the first_choice_interest id
                # initialize a new Meeting object, and add it to todo the LIST OF MATCHED MEETINGS
            # for all other sizes, add to todo the LIST OF UNMATCHED STUDENTS

###################################################
###### sort by secondary time selection ###########
###################################################

    # sort by secondary time selection
        # for loop: for each student object in the LIST OF UNMATCHED STUDENTS, read todo the secondary_time_selection_id of the student
        # put the student object into a todo SECONDARY TIME SELECTION DICTIONARY
        # with the secondary_time_selection_id as key, and a list of student objects as value

    # repeat the same steps as "sort by primary time selection", only to switch the primary_time_selection_id to
    # secondary_time_selection_id

    # at the end of the steps, we will have todo the LIST OF MATCHED MEETINGS
    # and todo the LIST OF UNMATCHED STUDENTS
    # we then do the following:

###################################################
##### final iteration for unmatched students ######
###################################################

    # For loop & if condition:
        # for each student in the LIST OF UNMATCHED STUDENTS, read the primary_time_selection_id and the secondary_time_selection_id,
        # from the LIST OF MATCHED MEETINGS, find Meetings that have the same time attributes and store in a list
            # for each Meeting in this list, read the other attributes of the meeting
                # if any attribute (course, interest) is present in the todo student's profile (read from a table of student's courses/interests or do a query)
                # add the student to this Meeting (by updating the Group object)
                # and remove the student from the LIST OF UNMATCHED STUDENTS
        # at the end of iteration, OUTPUT LIST OF MATCHED MEETINGS and LIST OF UNMATCHED STUDENTS

###################################################
########## safety check algorithm #################
###################################################

    # This extra part of algorithm is used to make sure the same groups do not keep being matched together

    # For loop & if condition:
        # for each meeting in the LIST OF MATCHED MEETINGS, read the group attribute of the meeting.
        # if the group is identical to a group that was matched previously (need to define what equal means for the group object)
            # then add the students in this group to the LIST OF UNMATCHED STUDENTS
            # and remove this meeting object from the LIST OF MATCHED MEETINGS

    # Optional: rerun the final iteration for unmatched students code block again to match unmatched students


if __name__ == '__main__':
    main()

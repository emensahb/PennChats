class Student():
    """This is a class representing a Student object.
    It will include methods that can be performed on a student."""

    # A student gets instantiated with four parameters
    def __init__(self, student_id, firstname, lastname, email):
        self.student_id = student_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    # A student will be represented by the following String message
    def __repr__(self):
        return f"Student name:{self.firstname} {self.lastname}, ID:{self.student_id}, Email:{self.email}"


def main():
    """This is the main function that runs the algorithm."""

    # import user information into a list
    all_students = Student.query.all() # maybe I need to import a module/package here so I can call the query.all() method

        # read all students who would like to be matched into a list from todo STUDENT_WHO_WANT_MATCHED_TABLE
        # all_students = Student.query.all()

    # if list is empty, output N/A, exit program
    if len(all_students) == 0:
        print("The student list is empty. No matched meetings and no unmatched students.")
        matched_meetings = []
        unmatched_students = []
        return matched_meetings, unmatched_students
    # if list is not empty, proceed to next step
    else:
        # what is it a list of? A list of student_ids? some sort of data object? what info does the list contain? (e.g. name, time_preference, email?)
        # initialize an empty student list
        student_list = []
        # initialize student object first? how? how to go about naming the variables? do I store them into another list?
        for item in all_students:
            student = Student(firstname='John', lastname='Doe', student_id=001, email='jdoe@email.com')
            student_list.append(student)

#################################################
###### sort by primary time selection ###########
#################################################

    # sort by primary time selection
        # for loop: for each student object in list, read todo the primary_time_selection_id of the student
        # put the student object into a todo PRIME TIME SELECTION DICTIONARY
        # with the primary_time_selection_id as key, and a list of student objects as value
        

    # check how many students are in each time selection group
        # for loop: for each key in the PRIME TIME SELECTION DICTIONARY, count the number of student objects
        # if conditional statement:
            # if size between 2-5, initialize todo a new Group object with all student objects
                # using the Group object created, and the primary_time_selection_id used to group these students as parameters,
                # initialize todo a new Meeting object, and add this Meeting object to a LIST OF MATCHED MEETINGS
            # if size = 1, add the student to todo a LIST OF UNMATCHED STUDENTS
            # if size > 5, proceed to next step to sort by primary networking goal

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

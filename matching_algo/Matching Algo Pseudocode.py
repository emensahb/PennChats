def main():
    """This is the main function that runs the algorithm. Pseudocode for now."""

    # import user information
        # read all students who would like to be matched into a list from todo STUDENT_WHO_WANT_MATCHED_TABLE
        # all_students = Student.query.all()

    # check if list is empty
        # if list is empty, output N/A, exit program
        # if list is not empty, proceed to next step
        # if all_students.size > 0, proceed

    # sort by primary time selection
        # for loop: for each student object in list, read todo the primary_time_selection_id of the student
        # from the STUDENT TABLE, put the student object into a todo PRIME TIME SELECTION DICTIONARY
        # with the primary_time_selection_id as key, and a list of student objects as value

    # check how many students are in each time selection group
        # for loop: for each key in the PRIME TIME SELECTION DICTIONARY, count the number of student objects
        # if conditional statement:
            # if size between 2-5, initialize todo a new Group object with all student objects
                # using the Group object created, and the primary_time_selection_id used to group these students as parameters,
                # initialize todo a new Meeting object, and add this Meeting object the final outouot list of finalized groupings
            # if size = 1, add the student to todo a LIST OF UNMATCHED STUDENTS
            # if size > 5, proceed to next step to sort by primary networking goal

    # sort students by primary networking goal
        # for loop: for each student object in the given time selection group, read todo the primary_networking_goal_id
        # of the student, and put the student object into a todo PRIME NETWORKING GOAL DICTIONARY
        # with the primary_networking_goal_id as key, and a list of student objects as value
        # (there will likely be only two keys in this dictionary: sort by class & sort by interest)

    # further sort students by type of primary networking goal
        # for loop if condition: for each key in the PRIME NETWORKING GOAL DICTIONARY, compare the primary_networking_goal_id...
            # if the key = "sort by class", do the following:
                # for loop: for each student object in the "sort by class" list, lookup the courses the student is currently taking
                # from the todo COURSES_ENROLLED_BY_STUDENT TABLE, and put the student into a SHARED COURSE DICTIONARY
                # with the key being the course_id of the first course of the COURSES_ENROLLED_BY_STUDENT TABLE
                # and the value being a list of students who are currently enrolled in the given course
            # if the key = "sort by interest", do the following:
                # for loop: for each student object in the "sort by interest" list, lookup the interests of the student
                # from the todo INTEREST_BY_STUDENT TABLE, and put the student into a SHARED INTEREST DICTIONARY
                # with the key being the interest_id of the first interest of the INTEREST_BY_STUDENT TABLE
                # and the value being a list of students who have the same interest

    # check how many students are in each key:value set in the two dictionaries
        # for loop: for each key:value pairing in the two dictionaries above, count the size of the value list
        # if conditional statement:
            # if size between 2-5, initialize a new Group object with all students in the list
                # using the Group object created, the primary_time_selection_id, the course_id/interest_id used to further
                # sort the students, initialize a new Meeting object, and add it to todo a new LIST OF MATCHED MEETINGS FOR PRIMARY TIME
            # if size = 1, add the student to todo a LIST OF UNMATCHED USERS FROM PRIMARY TIME SELECTION
            # if size > 5, proceed to next step to sort by secondary networking goal

    # sort students by secondary networking goal
        # for loop: for each student object in the given time selection group, read todo the secondary_networking_goal_id
        # of the student, and put the student object into a todo SECONDARY NETWORKING GOAL DICTIONARY
        # with the secondary_networking_goal_id as key, and a list of student objects as value
        # (there will likely be only two keys in this dictionary: sort by class & sort by interest)

    # repeat "further sort students by type of primary networking goal" from above and check the number of students in each key:value set
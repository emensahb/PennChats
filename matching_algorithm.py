"""
Pseudocode for the matching algorithm
"""

def main():
    """This is the main function that runs the algorithm.
    """

    # import user information
        # read from the table that lists all students who would like to be matched

    # initialize user object
        # get the student IDs from the table of students who would like to be matched
        # for each ID as key identifier, read student info from table that stores student info
        # initialize a student object with student ID, course info, interest info and selection preferences
        # store these student objects to a new list

    # check if list is empty
        # if list is empty, output N/A, exit program
        # if list is not empty, proceed to next step

    # sort by primary time selection
        # create a new list that stores all primary time selections that exists in the list of students
        # for each student object in list, read the primary time selection info of the student
            # if the time selection does not exist in the list of primary time selections, add that primary time selection to the list
            # if the time selection already exists, add that student object to that group

if __name__ = "__main__":
    main()
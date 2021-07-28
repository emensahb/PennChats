from pennchatsproject.models import *
from pennchatsproject import db
############################################
#   CREATE ALL THE TABLES IN THE MODEL     #
############################################

db.create_all()

# time options
t1 = TimeOption("Morning: 9am ET")
t2 = TimeOption("Afternoon: 3pm ET")
t3 = TimeOption("Evening: 7pm ET")
t4 = TimeOption("Overnight: 1am ET")


# networking goals
n1 = NetworkingGoal("Match by Course")
n2 = NetworkingGoal("Match by Interest")


# week meet
w1 = WeekMeet("Aug 2")
w2 = WeekMeet("Aug 9")
w3 = WeekMeet("Aug 16")
w4 = WeekMeet("Aug 23")
w5 = WeekMeet("Aug 30")
w6 = WeekMeet("Sept 6")
w7 = WeekMeet("Sept 13")
w8 = WeekMeet("Sept 20")
w9 = WeekMeet("Sept 27")


# courses
c1 = Course("CIT591", "Intro to Software Development")
c2 = Course("CIT592", "Math Foundations of Computer Science")
c3 = Course("CIT593", "Intro to Computer Systems")
c4 = Course("CIT594", "Data Structures and Software Design")
c5 = Course("CIT595", "Computer Systems Programming")
c6 = Course("CIT596", "Algorithms & Computation")
c7 = Course("CIS515", "Fundamentals of Linear Algebra & Optimization")
c8 = Course("CIS547", "Software Analysis")
c9 = Course("CIS549", "Wireless Communication for Mobile Networks")
c10 = Course("CIS550", "Database & Information Systems")
c11 = Course("CIS581", "Computer Vision & Computational Photography")
c12 = Course("CIT520", "Intro to Robotics")
c13 = Course("CIT582", "Blockchains & Cryptography")
c14 = Course(
    "ESE542", "Statistics for Data Science: An Applied Machine Learning Course")


# interests
i1 = Interest("Artificial Intelligence & Machine Learning")
i2 = Interest("Blockchain")
i3 = Interest("Cybersecurity & Cryptography")
i4 = Interest("Data Science")
i5 = Interest("Game Design")
i6 = Interest("Interview Prep")
i7 = Interest("Mathematics for Computer Science")
i8 = Interest("Networking & Computer Systems")
i9 = Interest("Project Management")
i10 = Interest("Software Development")


# cohorts
co1 = Cohort("Spring 2019")
co2 = Cohort("Fall 2019")
co3 = Cohort("Spring 2020")
co4 = Cohort("Fall 2020")
co5 = Cohort("Spring 2021")
co6 = Cohort("Fall 2021")


db.session.add_all([t1, t2, t3, t4, n1, n2, c1, c2, c3, c4, c5, c6, c7, c8, c9,
                 c10, c11, c12, c13, c14, i1, i2, i3, i4, i5, i6, i7, i8, i9,
                 i10, co1, co2, co3, co4, co5, co6, w1, w2, w3, w4, w5, w6,
                 w7, w8, w9])

#db.session.add_all([t1, t2, t3, t4, n1, n2, c1, c2, c3, c4, c5, c6, c7, c8, c9,
                   #c10, c11, c12, c13, c14, i1, i2, i3, i4, i5, i6, i7, i8, i9,
                   #i10, co1, co2, co3, co4, co5, co6, w1, w2, w3, w4, w5, w6,
                   #w7, w8, w9])
db.session.commit()

# time_options = TimeOption.query.all()
# networking_goals = NetworkingGoal.query.all()
# interests = Interest.query.all()
# cohorts = Cohort.query.all()
# courses = Course.query.all()
# week_meets = WeekMeet.query.all()
#
# print(time_options)
# print(networking_goals)
# print(interests)
# print(cohorts)
# print(courses)
# print(week_meets)

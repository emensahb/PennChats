from pennchatsproject.models import *
############################################
#   CREATE ALL THE TABLES IN THE MODEL     #
############################################

db.create_all()

# time preferences options
tp1 = TimePreference("Morning: 9am ET")
tp2 = TimePreference("Afternoon: 3pm ET")
tp3 = TimePreference("Evening: 7pm ET")
tp4 = TimePreference("Overnight: 1am ET")


# networking goals options
ng1 = NetworkingGoal("class")
ng2 = NetworkingGoal("interest")


# classes
c1 = Course(591, "Intro to Software Development")
c2 = Course(592, "Math Foundations of Computer Science")
c3 = Course(593, "Intro to Computer Systems")
c4 = Course(594, "Data Structures and Software Design")
c5 = Course(595, "Computer Systems Programming")
c6 = Course(596, "Algorithms & Computation")
c7 = Course(515, "Fundamentals of Linear Algebra & Optimization")
c8 = Course(547, "Software Analysis")
c9 = Course(549, "Wireless Communication for Mobile Networks")
c10 = Course(581, "Computer Vision & Computational Photography")

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

# cohort
cht1 = Cohort(1, "Spring 2019")
cht2 = Cohort(2, "Fall 2019")
cht3 = Cohort(3, "Spring 2020")
cht4 = Cohort(4, "Fall 2020")
cht5 = Cohort(5, "Spring 2021")
cht6 = Cohort(6, "Fall 2021")

db.session.add_all([tp1, tp2, tp3, tp4, ng1, ng2, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
                    i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, cht1, cht2, cht3, cht4, cht5, cht6])

# db.session.add_all([cht5, cht6])
db.session.commit()

# time_preferences = TimePreference.query.all()
# networking_goals = NetworkingGoal.query.all()
# interests = Interest.query.all()
# cohorts = Cohort.query.all()
# classes = Class.query.all()

# print(time_preferences)
# print(networking_goals)
# print(interests)
# print(cohorts)
# print(classes)

# Penn Chats
Penn Chats is a project inspired by LunchClub (https://lunchclub.com/), a platform that facilitates online social networking,
created for the student community of MCIT Online, an online master's program offered at the University of Pennsylvania.
The project aims to provide an easy way for the student community, where members are spread across different geographies, to form connections amongst one another.

The project outcome is a web application that pairs students given a predetermined set of criteria such as time availability, enrolled coursework 
and career aspirations. These categories will come with pre-populated options for students to select from.

Upon receiving matching preferences from users, the application will put students into groups and notify them via email of the date and time they would meet.

## User Experience
A new user would interact with the website in the following ways:
1. Create a new account
2. Update user profile
3. Submit a form that contains matching preferences
4. Be notified of matches
5. Return to website to see matching result
6. Check profiles of peers

## User Interface
The website employs the Blueprint library in Flask and is broken down into three components: core, students, meetings.

### Core
Includes the home page and about us page

### Students
Includes the register, login, logout, edit profile, sign-up for Penn Chats, and Student Profile pages

### Meetings
Includes the generate and results pages

## The Database
Main entities of the database include:
- Students
- Courses
- Interests
- Time Options
- Networking Goals
- Weekly Signups
- Meetings
- Unmatched Students

## Technology
Penn Chats is developed using Python and the Flask web framework, with ProsgreSQL as the back-end database solution. 

## The Algorithm
The design principles of the algorithm:
1. Set the number of students per meeting to 2-5 people
2. Prioritize primary time preference & networking goal
3. Handle unmatched students separately

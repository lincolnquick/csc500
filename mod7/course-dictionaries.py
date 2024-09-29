# Lincoln Quick
# CSC 500 Module 7 - Critical Thinking Assignment
# 09/21/2024

# Creating Python Programs
# Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the courses meet. 
# The dictionary should have the following key-value pairs:
# Key-Value Pairs: Room Number
# Course Number (key)
# Room Number (value)


# The program should also create a dictionary containing course numbers and the names of the instructors that teach each course. 
# The dictionary should have the following key-value pairs:
# Key-Value Pairs: Instructors
# Course Number (key)
# Instructor (value)

# The program should also create a dictionary containing course numbers and the meeting times of each course. 
# The dictionary should have the following key-value pairs:
# Key-Value Pairs: Meeting Time
# Course Number (key)
# Meeting Time (value)

# The program should let the user enter a course number and then it should display the course's room number, 
# instructor, and meeting time.

# Create a dictionary containing course numbers and the room numbers of the rooms where the courses meet.
course_room = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# Create a dictionary containing course numbers and the names of the instructors that teach each course.
course_instructor = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Create a dictionary containing course numbers and the meeting times of each course.
course_time = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Let the user enter a course number and then display the course's room number, instructor, and meeting time.
course_number = input("Enter a course number: ")

# Display the course's room number, instructor, and meeting time.
print("Room Number:", course_room[course_number])
print("Instructor:", course_instructor[course_number])
print("Meeting Time:", course_time[course_number])

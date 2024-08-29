# Lincoln Quick
# CSC 500, Module 3, Discussion
# 2024-08-29

# "Identify three real-life scenarios in which an array could be used for storing information. 
# Provide a sample code segment that illustrates how to store data in an array for one of your outlined scenarios. 
# Provide a rationale for your response. 
# In response to your peers, provide constructive feedback on strategies and rationales that were posted. 
# Include additional code segments if applicable."


# Scenario 1: Reading List
# An array could be used to store a reading list of titles the reader wishes to read.
reading_list = ['Interview with the Vampire', 'Game of Thrones', 'The Man in the High Castle', 'Digital Fortress', 'Red White and Royal Blue']
print('Current reading list: {}'.format(reading_list))
# Rationale: An array is a good choice for this scenario because it allows for easy access to the 
# list of titles in a single variable. Items can be added, removed, or accessed by index as needed.


# Scenario 2: Assignment Grades
# An array could be used by a student to store their grades for each assignment in a course.
import array as arr
grades = arr.array('f', [95.5, 94.0, 100.0, 92.5, 89.5])
print('Current grades: {}'.format(grades))

average_grade = sum(grades) / len(grades)
print('Average grade: {}'.format(average_grade))
# Rationale: An array is a good choice for this scenario because it allows the student to store each 
# completed grade and quickly calculate the average grade for the course.


# Scenario 3: Shopping List
# An array could be used to store a shopping list of items the shopper needs to purchase.
shopping_list = ['milk', 'eggs', 'bread', 'sausage', 'cheese', 'soda']
print('Current shopping list: {}'.format(shopping_list))
# Rationale: An array is a good choice for this scenario because it allows the shopper to keep track of each item
# they need to purchase in a single variable. Items can be added, removed, or accessed by index as needed.
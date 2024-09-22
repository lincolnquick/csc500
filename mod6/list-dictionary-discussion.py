# Lincoln Quick
# CSC 500: Module 6 Discussion
# 2024-09-19

# "The list and dictionary object types are two of the most important and often used types in a Python program. 
# What are some ways to insert, update, and remove elements from lists and dictionaries? 
# Why would you choose one data type over another? 
# Provide code examples demonstrating the usages of both data types."

# List example
my_list = [1, 2, 3, 4, 5]

# Append an item to the end of the list
my_list.append(6)

# Insert an item at a specific index
my_list.insert(0, 0)

# Update an item at a specific index
my_list[0] = -1

# Remove an item by value
my_list.remove(-1)

# Pop an item by index
popped_item = my_list.pop(0)

# Remove an item by index
del my_list[0]

# Dictionary example
my_dict = {"CSC500": "Principles of Programming", "CSC501": "Management for the Computer Science Professional", 
           "CSC502": "Ethical Leadership in Software Development", 
           "CSC505": "Principles of Software Development"}

# Add a new entry
my_dict["CSC506"] = "Design and Analysis of Algorithms"

# If the key already exists, updates the value
my_dict["CSC500"] = "Principles of Programming in Python"

# Remove an entry by key using pop
popped_item = my_dict.pop("CSC506")

# Remove an entry by key using del
del my_dict["CSC505"]



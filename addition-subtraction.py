# CSC500 Module 1 Critical Thinking Assisgnment
# Part 1:
# Write a Python program to find the addition and subtraction of two numbers.
# Ask the user to input two numbers (num1 and num2). Given those two numbers, 
# add them together to find the output. Also, subtract the two numbers to find the output.

# Ask the user to input two numbers
user_num1 = int(input("Enter the first number: "))
user_num2 = int(input("Enter the second number: "))

# Calculate the addition and subtraction of the two numbers
addition = user_num1 + user_num2
subtraction = user_num1 - user_num2

# Display the results
print(f"The sum of {user_num1} and {user_num2} is {addition}")
print(f"The difference of {user_num1} and {user_num2} is {subtraction}")


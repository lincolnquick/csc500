# Lincoln Quick
# CSC 500: Module 5 Critical Thinking Assignment Part 1
# 2024-09-15
# "Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
# The program should first ask for the number of years. The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month. 
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
# After all iterations, the program should display the number of months, the total inches of rainfall, 
# and the average rainfall per month for the entire period."

# Get the number of years
years = int(input("Enter the number of years: "))

# Initialize variables
total_rainfall = 0
total_months = years * 12


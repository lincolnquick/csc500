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

# Loop through each year
for year in range(1, years + 1):
    # Loop through each month
    for month in range(1, 13):
        # Get the rainfall for the month
        rainfall = float(input(f"Enter the inches of rainfall for year {year}, month {month}: "))
        total_rainfall += rainfall

# Calculate the average rainfall
average_rainfall = total_rainfall / total_months

# Display the results
print("\nResults:")
print(f"Number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month: {average_rainfall}")
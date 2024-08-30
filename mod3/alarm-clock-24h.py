# Lincoln Quick
# CSC 500, Module 3, Critical Thinking Assignment Part 2
# 2024-08-29

# "Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
# Write a Python program to solve the general version of the above problem. Ask the user for 
# the time now (in hours) and then ask for the number of hours to wait for the alarm. 
# Your program should output what the time will be on a 24-hour clock when the alarm goes off."

# Get the time now (in hours) from the user
current_time = int(input('Enter the current time (in hours): '))

# Get the number of hours to wait for the alarm from the user
hours_till_alarm = int(input('Enter the number of hours to wait for the alarm: '))

# Calculate the time the alarm will go off (current time + hours till alarm)
alarm_time = (current_time + hours_till_alarm) % 24

# Also format the time in standard 12-hour clock format
if alarm_time == 0:
    standard_hour = 12
    period = 'AM'
elif alarm_time == 12:
    standard_hour = 12
    period = 'PM'
elif alarm_time > 12:
    standard_hour = alarm_time - 12
    period = 'PM'
else:
    standard_hour = alarm_time
    period = 'AM'

# Display the time the alarm will go off in 24-hour and 12-hour clock formats
# Display the time the alarm will go off
print('The alarm will go off at {0} hours ({1}:00 {2})'.format(alarm_time, standard_hour, period))


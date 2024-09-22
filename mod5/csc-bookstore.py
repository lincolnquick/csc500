# Lincoln Quick
# CSC 500: Module 5 Critical Thinking Assignment Part 2
# 2024-09-15
# "The CSU Global Bookstore has a book club that awards points to its students based on the number of books 
# purchased each month. The points are awarded as follows:
# --If a customer purchases 0 books, they earn 0 points.
# --If a customer purchases 2 books, they earn 5 points.
# --If a customer purchases 4 books, they earn 15 points.
# --If a customer purchases 6 books, they earn 30 points.
# --If a customer purchases 8 or more books, they earn 60 points.
# Write a program that asks the user to enter the number of books that they have purchased this month 
# and then display the number of points awarded."

# Get the number of books purchased
books = int(input("Enter the number of books purchased this month: "))

# Determine the number of points awarded;
# made assumptions about the number of books purchased for odd number of books
if books <= 1:
    points = 0  # If a customer purchases 0-1 books, they earn 0 points
elif books <= 3:
    points = 5  # If a customer purchases 2-3 books, they earn 5 points
elif books <= 5:
    points = 15  # If a customer purchases 4-5 books, they earn 15 points
elif books <= 7:
    points = 30  # If a customer purchases 6-7 books, they earn 30 points
else:
    points = 60 # If a customer purchases 8 or more books, they earn 60 points

# Display the number of points awarded
if books == 1:
    print(f"\nNumber of points awarded: {points} for purchasing 1 book this month.")
else:
    print(f"\nNumber of points awarded: {points} for purchasing {books} books this month.")
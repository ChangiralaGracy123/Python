# Name: Gracy Changirala
# Instructor: Mani Naveen Karini
# Subject: Python Programming
# Date: 29-01-2024

# A program that displays my personal information

# Exercise-1
print("Name: Gracy Changirala")
print("City of Birth: Hyderabad")
print("Favorite Sports Team: RCB")
print("Undergraduate Major: B.com Computer Application")


# A Program that displays an ouput for the given formula of the car's miles per gallon (MPG)

# Exercise-2
# Get input from the user
miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the gallons of gas used: "))

# Calculate MPG
mpg = miles_driven / gallons_used

# Display the result with formatted output
print('The MPG is ${:,.2f}'.format(mpg))
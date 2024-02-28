# Filename: Week-1 Program.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program that converts Fahrenheit temperatures to Celsius.
# Last changed: 29-01-2024


# Exercise 3: Fahrenheit to Celsius Converter

# Prompt the user to enter temperature in Fahrenheit
fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius using the conversion formula C = (F - 32) × 5⁄9
celsius_temperature = (fahrenheit_temperature - 32) * 5 / 9

# Display the converted temperature in Celsius
print(f"{fahrenheit_temperature}°F is equal to {celsius_temperature:.2f}°C")


#Output Description: The program will prompt the user to enter a temperature in Fahrenheit, waiting for the user's input. After the user enters the temperature, the program will calculate the equivalent temperature in Celsius using the conversion formula. The program will then print the original Fahrenheit temperature and the calculated Celsius temperature to the console.Both temperatures will be displayed with two decimal places for clarity.
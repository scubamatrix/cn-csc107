# A program to calculate the surface area of a cone by Wonder Student
# Load the math module to get pi and the sqrt function
import math

# Introduce the program
print("This program determines the surface area of a cone.")

# Get the Data
height = float(input("Enter the height of the cone in inches: "))
radius = float(input("Enter the radius of the cone in inches: "))

# Calculate the surface area
area = math.pi * radius * (radius + math.sqrt(height ** 2 + radius **2))

# Print the output
print("The surface area of the cone is {:.2f} square inches.".format(area))

#!/usr/bin/env python3
"""
cone.py

A program to calculate the surface area of a cone.

Author: Jeff Holmes
Date: 01/06/2024
Version: 1.0
Python: 3.11.6
"""
# Load math module to get pi and the sqrt functions
import math

# Introduce the program
print("This program determines the surface area of a cone.")

# Get the input (data) from user
height = float(input("Enter the height of the cone in inches: "))
radius = float(input("Enter the radius of the cone in inches: "))

# Calculate the surface area
area = math.pi * radius * (radius + math.sqrt(height ** 2 + radius ** 2))

# Print the output
print("The surface area of the cone is {:.2f} square inches.".format(area))

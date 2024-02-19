#!/usr/bin/env python3
"""
cone_area.py

A program to calculate the surface area of a cone.

Author: Jeff Holmes
Date: 01/06/2024
Version: 1.0
Python: 3.11.6
"""
import math
import os
import sys


def cone_area():
    """
    Calculate the surface area of a cone.
    """
    # Introduce the program
    print("This program determines the surface area of a cone.")

    # Get the Data
    height = float(input("Enter the height of the cone in inches: "))
    radius = float(input("Enter the radius of the cone in inches: "))

    # Calculate the surface area
    area = math.pi * radius * (radius + math.sqrt(height ** 2 + radius **2))

    # Save formatted output to variable
    # error_message = "The surface area of the cone is {:.2f} square inches.".format(area))

    # Print the output
    print(f"The surface area of the cone is {area:.2f} square inches.")


cone_area()
print("\nDone!")


#!/usr/bin/env python3
"""
hello.py

A program template for easy reference.

Author: Jeff Holmes
Date: 01/06/2024
Version: 1.0
Python: 3.11.6
License: MIT License (optional)

References:
  [Common Header Format in Python](https://www.delftstack.com/howto/python/common-header-python/#google_vignette)
  [Docstrings in Python Tutorial](https://www.datacamp.com/tutorial/docstrings-python)
"""
import math
import os
import sys


def compute_area():
    """
    Calculate the surface area of a cone.
    """
    # Introduce the program
    print("\nThis program determines the surface area of a cone.")

    # Get the Data
    height = float(input("Enter the height of the cone in inches: "))
    radius = float(input("Enter the radius of the cone in inches: "))

    # Calculate the surface area
    area = math.pi * radius * (radius + math.sqrt(height**2 + radius**2))

    # Save formatted output to variable
    # error_message = "The surface area of the cone is {:.2f} square inches.".format(area))

    # Print the output
    print(f"The surface area of the cone is {area:.2f} square inches.")


def hello(name: str):
    """
    Here is some sample code.
    """
    # Get name of program file for logging
    prog_name = os.path.basename(__file__)
    basename, extension = os.path.splitext(prog_name)
    prog_name = basename

    print(f"Hello {name}")
    print(f"program: {prog_name}")


def main():
    """
    The main driver for the program.
    """
    hello("Jeff")
    compute_area()


# The driver function (confirm that code is under main function)
if __name__ == "__main__":
    main()
    print("\nDone!")

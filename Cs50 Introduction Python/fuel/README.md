
#Fraction Analyzer
This simple Python script takes a fraction as input, calculates its percentage value, and categorizes it into fuel levels. The user is prompted to input a fraction in the form of x/y. The script then converts the numerator (x) and denominator (y) to integers, calculates the percentage (z), and categorizes the fuel level based on the percentage.

##Usage
Run the script in a Python environment.
Enter a fraction when prompted (e.g., 3/4).
The script will output the corresponding fuel level category.
Fuel Level Categories
F: Fuel - if the percentage is near 99% or above.
E: Empty - if the percentage is near 1% or below.
Percentage value in other cases.
##Example
bash

Fraction: 3/4
75%
##Handling Input Errors
The script handles the following input errors:

If the input is not in the form of x/y, the script will prompt the user again.
If there is a ZeroDivisionError, indicating an attempt to divide by zero, the user will be prompted again.
If there is a ValueError during the conversion of the numerator or denominator to an integer, the user will be prompted again.

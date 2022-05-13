# Takes a number as an input from the user and prints out the following information:
# (1) The absolute value of the number.
# (2) The floor of the number using the math module (e.g., floor(3.75) is 3).
# (3) The number rounded to 2 decimal places.

from math import floor
number = float(input("Please enter a number.\n"))
absNumber = abs(number)
floorNumber = floor(number)
roundedNumber = round(number, 2)

print(f"Absolute value: {absNumber}, Floor: {floorNumber}, Rounded to 2 decimal places: {roundedNumber}")

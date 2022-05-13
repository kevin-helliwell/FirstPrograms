from math import factorial
from math import log2

# Asks for user input on favorite month/day.
# Converts input to necessary types for later function calls.
# Corrects user input in case month is entered in all caps or all lowercase.
# Prints in specified format.
favMonthStr = str(input("Please enter the name of your favorite month.\n"))
favMonthStrCorrected = favMonthStr.lower().capitalize()
favDayInt = int(input("Please enter your favorite day of the month.\n"))
print(f"{favMonthStrCorrected} {favDayInt}, 2020")

# Checks whether month input is alphanumeric and prints corresponding boolean value.
isMonthAlphanumeric = favMonthStr.isalpha()
print(f"Is the month alphanumeric? {isMonthAlphanumeric}")

# Converts day input back to string and counts number of 2's.
# Stores number of 2's in a variable, and prints its value.
numberOfTwosDay = str(favDayInt).count("2")
print(f"How many 2's? {numberOfTwosDay}")

# Uses the factorial function from math module to calculate the factorial of the day provided from user input.
# Ex. September 2, 2020 -> factorial(2)
factorialDay = factorial(favDayInt)
print(f"Factorial: {factorialDay}")

# Uses the log base 2 function from math module to calculate the log base 2 of the day provided from user input.
# Ex. September 1, 2020 => log2(1)
logDay = log2(favDayInt)
print(f"Log base 2: {logDay}")

"""
Project:     Data Types Notes
Author:      Mr. Buckley
Last update: 8/25/2018
Description: Goes over comments, int, float, str, and type casting  
"""

# *** COMMENTS ***
# This is a comment (with a "#")
# Comments are only for the user's eyes, the program doesn't read them.
# Describe what sections of code do with a comment.
"""
This is a
multiline comment
"""

# *** DATA TYPE: INTEGER ***
# TODO: An integer number (no decimal)

integer = 5
print(integer)
print(type(integer))

# *** DATA TYPE: FLOAT ***
# TODO: A decimal number

decimal = 3.14159
print(decimal)
print(type(decimal))

# *** DATA TYPE: STRING ***
# TODO: A string of characters enclosed in quotes

string = "Fegettaboutit 5 times"
print(string)
print(type(string))

# *** TYPE CASTING ***
# This converts one type to another

# TODO: Cast float to int

decimal = 3.141597462890
dec_to_int = int(decimal)
print(dec_to_int)
print(type(dec_to_int))

# TODO: Cast int to string

number = "6"
print(int(number) + 2)

# TODO: Cast number string to int SKIPPED

# TODO: Input demo (str to float)

print("give me a decimal and I'll ad 1 to it")

numbers = float(input())
print(numbers + 1)
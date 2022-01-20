# best practice is to put all import statements at the top
import math 

# this is a one line comment
# a comment is "code" that is ignored by Python
# we use comments to document our code

"""
this is a multi
line comment
AKA a block comment
"""

print("hello world")

# VARIABLES
x = 5 # read this is as "x is assigned 5" or "x stores 5"
# NOT "x equals 5"
# a variable stores a value
# a value has a data type
# a data type defines a range of values
# example: the int data type (short for integer) represents whole numbers
print(x)
print(type(x))
# let's say we want to reassign x a different value
x = 5.5
print(x)
print(type(x))
# example: the float data type (short for floating point number) represents
# numbers with fractional parts (AKA decimals)
x = "hello"
# example: the string data type represents a sequence of characters
print(x)
print(type(x))
x = "5"
print(x)
print(type(x))

# OPERATORS
# PEMDAS: parens, exponents, multiplication, division, addition, subtraction
# * is multiplication
print(4 * 5)
# / is floating point division (the "normal" division)
print(5 / 2)
# // is integer division (the whole number result of floating point division)
print(5 // 2) 
# ** is exponentiation (power)
print(2 ** 5) # if multiple **, they evaluate right to left
# we can also use the pow() function from the math module
# need to import the math module to use it
# (aside: a .py file AKA a module AKA script)
print(math.pow(2, 5))

# GETTING USER INPUT
# print("Enter your favorite number: ")
# favorite_number = input()
# print("Your favorite number is:", favorite_number)
# print("Your favorite number doubled is:", favorite_number * 2, sep="*")
# print(type(favorite_number))
# print("hello" * 2, end="~~~~~~~") # sep and end are called keyword arguments
# print("here")
# # let's say, we really do want to double the favorite number
# # we need to "convert" favorite_number the string to an int (or float)
# # this is called type conversion and there are built-in functions to do this
# favorite_number_int = int(favorite_number)
# print(favorite_number_int, type(favorite_number_int))
# print("Your favorite number doubled is:", favorite_number_int * 2)

# FORMATTING (decimal numbers)
# a few ways to do this
# 1. C style (old skool)
print(math.pi)
# round math.pi to 2 decimal places
print("%.2f" %(math.pi))
# 2. Pythonic way (new skool)
print("{:.2f}".format(math.pi))
# 3. use the built-in function round()
# round() actually rounds the number (and you could store it as such)
print(round(math.pi, 2))

# CONDITIONALS (aka if statements)
# if some condition (AKA boolean condition) is true:
#    then execute some code (AKA body)
x = 7
if x == 6: # note: == is the equality operator (= assignment operator)
    print("x is 6")
    # this the body
    # the body only executes when the value stored in x is equal to 6
    # i.e. the boolean condition evaluates to true
    # note standard indentation is 1 tab = 4 spaces
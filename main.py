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
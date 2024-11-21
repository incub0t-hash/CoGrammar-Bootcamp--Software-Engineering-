# I will first list the set of variables in the code
# I will then specify what I want to convert each to using comments
# I will then convert each to the specified class 
# I will then print out the variables each on a seperate line

#List of Variables

# Convert this to integer

num1 = 99.23

# Convert this to a Float

num2 = 23

# Convert this to a String

num3 = 150

# Convert this to Integer

string1 = "100"

# Code to convert each variable

# Int() casts variable as Integer

num4 = int(num1)

# Float() casts variable as a float

num5 = float(num2)

# Str() casts variable as a string

string2 = str(num3)

# See Line 26

num6 = int(string1)

# First time around i just did the cast command and variable name, must remember to create a new variable name for each  conversion i.e NewVariable = Cast() else will print the un casted/converted variable 
# After seeing the model answer it can also be done with the orignal variable name as such num1 = string(num1) etc and so on
# can use the type([variable name here]) to print variable class type

# This section will print each on a new line

print(num4)
print(num5)
print(string2)
print(num6)


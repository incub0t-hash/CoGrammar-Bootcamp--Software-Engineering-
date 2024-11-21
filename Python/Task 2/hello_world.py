# Code for Auto-graded task 1
# I will first ask for the user to input their name using name variable and the input command
# Then I will print this output
# I will then ask for their age using age variable
# Then I will also print this along with their name
# Then I will print hello world 

# Asking for user input

name = input("Hi, please tell me your name?")
age = input("Please tell me your age.")

# I will now print out the inputted data

print("Hi, Your name is "+name+" and you are "+age+" years old")

# This can also be written as follows:

print("{} is {} years old!".format(name, age))

# The {} brackets can be use to specify the alloted place for data to be updataed and the format function can specify in which order this data is input into the print statement

# I will now print Hello World

print("Hello World!")
# ask user to input a sentence

str_manip = input("Please enter a sentence:")

# print sentence

print(str_manip)

# calcualte the length of the sentence

print(f"This sentence is {len(str_manip)} characters long including spaces")

# find last letter

last_char = str_manip[-1]

# replace it with @

str_replaced = str_manip.replace(last_char,"@") 

# do not use str.replace use variableName.replace

print(str_replaced)

# print the last 3 characters backwards

print(str_manip[-1:-4:-1])

# create 5 letter word using first three chars and last two chars

new_word = str_manip[0:3]+str_manip[-2:]
print(new_word)
# ask for user input

num1 = input("Please enter you first choice for a number?")
num2 = input("Please enter you second choice for a number?")
num3 = input("Please enter you third choice for a number?")

num1_int = int(num1)
num2_int = int(num2)
num3_int = int(num3)

# print all inputs

print(f"The numbers you chose were {num1}, {num2} and {num3}")

# print the sum of all numbers

sum = num1_int+num2_int+num3_int
print(f"The sum of all numbers={sum}")

# print first minus second

minus = num1_int-num2_int
print(f"The first number minus the second ={minus}")

# print third number multiplied by first

multi = num3_int*num1_int
print(f"The third number multiplied by the first number ={multi}")

# print sum of all three numbers divided by the third

div = float(sum/num3_int)
print(f"The sum of all numbers divided by the third ={div}")
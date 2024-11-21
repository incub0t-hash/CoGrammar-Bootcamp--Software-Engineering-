# create a loop that continualy asks for user to input a number

num = int()
# we will define the variables needed for number average here for use later

num_sum = num
total_num_input = 0

while num != -1: # in math i know =/= means is not equal to, looked up coding equivalent 
    num = int(input("PLease enter a number"))
    num_sum = num_sum + num # every time the user inputs a value it will add it to the sum
    total_num_input = total_num_input+ 1 # every time the user inputs a number we add 1 to input count
    if num == 0:
        print("0 is not a valid choice")
        total_num_input= total_num_input-1 # entering 0 or -1 will never be included in our average calculation during the loop
    elif num !=0:
        print(f"Total numbers inputted is currenlty {total_num_input} and the total sum is currentl {num_sum}")

# upon loop break we work out the average 
# we never counted 0 or -1 so its really just dividing one variable by another 
 
num_avg = num_sum/total_num_input
print(f"The total average of all inputted numbers is{num_avg}")
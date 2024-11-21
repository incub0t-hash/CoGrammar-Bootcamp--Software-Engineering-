# create a loop to create an arrow pattern
# i think this can be done with a simple length check and splicing
# first we define pattern

pattern = ""

# create a loop to print * adding a * each time 

for x in range(5):    
        print(pattern)
        if len(pattern)<5:
            pattern+="*"   
# once we get half wa through the arrow we want to remove *
print(pattern)

#while attempting to do this as one loop the remove char section struggled so i opted for a while loop instead
# loop to remove char

while len(pattern)>1:
    pattern = pattern[:-1]
    print(pattern)

# ask for users time for each event

swim = int(input("Please enter the time it took to complete the swimming section in minutes:"))
cycle = int(input("Please enter the time it took to complete the cycling section in minutes:"))
run = int(input("Please enter the time it took to complete the running section in minutes:")) 

# calculate total time taken

total_min = swim+cycle+run
print(f"The total time taken to complete the triathlon was {total_min} minutes.")

# calculate award and displa award

if total_min < 101: print("Based on this time ou have been awarded Honary Colours.")
if total_min > 100 and total_min < 106: print("Based on this time ou have been awarded Honary half Colours.")
if total_min > 105 and total_min < 111: print("Based on this time ou have been awarded Honary Scroll.")
if total_min < 110: print("Based on this time ou have been not won any award.")
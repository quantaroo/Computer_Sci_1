
#CPCS230-03
#Assignment 1 Seconds
import math
print("A day has 86,000 seconds")

#Ask the user for the second range 1 to 86,000

seconds1 = int(input("Please input a random amount of seconds from 1 to 860000(no commas):"))

#Calculate the amount of
seconds2 = seconds1 % (860000)
hour = seconds2 // 3600
seconds2 %= 3600
minutes = seconds2 // 60
seconds2 %= 60

#print results
print("With", seconds1,"second(s), it would make", hour,"hour(s)")
print(minutes,"minute(s) and", seconds2,"second(s)")

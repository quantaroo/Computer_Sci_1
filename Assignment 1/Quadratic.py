
#CPCS230-03
#Assignment 1 Quadratic
import math

print("We will now solve for the quadratic formula")

#Ask user for 'a', 'b', and 'c' for the Quadratic formula
print("Please imput 'a' 'b' and 'c' for the quadratic formula")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

#Calculate for the two answers
answer_1 = (-b + math.sqrt((math.pow(b,2)) - (4 * a * c))) / (2 * a)
answer_2 = (-b - math.sqrt((math.pow(b,2)) - (4 * a * c))) / (2 * a)
answer_1 = round(answer_1,2)
answer_2 = round(answer_2,2)

#print answer to user
print("With imputs a:", a, "b:", b, "c:", c)
print("The answer is either", answer_1, "or", answer_2)


#CPCS230-03
#Assignment 2 Quadratic
import math

print("We will now solve for the quadratic formula")

#Ask user for 'a', 'b', and 'c' for the Quadratic formula
print("Please imput 'a' 'b' and 'c' for the quadratic formula")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

#Calculate for the two answers
square_root = (math.pow(b,2)) - (4 * a * c)                #Take the square root out of the equation
if a != 0:
    if square_root >= 0:                                   #if square root is not negative proceed
        answer_1 = (-b + math.sqrt(square_root) / (2 * a)) #Calculate the first answer
        answer_2 = (-b - math.sqrt(square_root) / (2 * a)) #Calculate the second answer
        answer_1 = round(answer_1,2)                       #round first answer
        answer_2 = round(answer_2,2)                       #round second answer
        print("With imputs a:", a, "b:", b, "c:", c)       #print answer
        print("The answer is either", answer_1, "or", answer_2)
    else:                                                  #print if square root is negative
        print("With imputs a:", a, "b:", b, "c:", c)
        print("The square root has a negative number inside it.")
        print("This will cause an undefined expression")
else:                                                      #print if 'a' is 0
    print("With 'a' being", a, "this will cause a zero in the denominator")
    print("This will cause an undefined expression")

#CPCS230-03
#Homework Assignment 4

#Alternade.py

#explain to the user what an alternade is
print()
print("Today we will make or split an alternade. :)")
print()
print("An Alternade is a word in which its letters, taken alternatively in a strict sequence,")
print("and used in the same order as the original word, make up at least two other")
print("words. All letters must be used, but the smaller words are not necessarily")
print("of the same length. For example, a word with seven letters where every second")
print("letter is used will produce a four-letter word and a three-letter word.")
print("i.e. theorem term hoe")
print()
print("P.S. no uppercase, whitespace, numbers, or symbols please. You will be prompted to try again.")
print()
#Request input from user
decision = input("destruction or construction? :")
#Create a constant for the while loop
i = 0
#The loop to check what input for decision
while i == 0:
    if decision == "destruction":
        lowercase = 0                                                   #Flags for decision structure
        symbols = 0
        print()
        word1 = input("What is the alternade that we want to split? :") #Input from user for spliting the alternade
        print()
        while lowercase != 1 or symbols != 1:                           #While loop to check for Uppercase, whitepace, symbols,
            if symbols == 0:                                            #Check for symbols, whitespace, or numbers
                if word1.isalpha() == True:
                    symbols += 1
                else:                                                   #If there is symbols whitespace, or numbers promp for another entry
                    print("Your entry has non alphabet symbols, a whitespace or numbers. Try Again.")
                    word1 = input("What is the alternade that we want to split? :")
            else:                                                       #Chech for uppercase letters
                if word1.islower() == True:
                    lowercase += 1
                else:                                                   #If there is uppercase letters promp for another entry
                    print("Your entry has uppercase letters. Try Again.")
                    word1 = input("What is the alternade that we want to split? :")
        else:                                                           #If while loop is good we can start spliting the alternade
            even = word1[::2]                                           #Get the even letters.
            odd = word1[1::2]                                           #Get the odd letters.
            print("With your word :", word1,"your two words are :", even, "and ", odd)
            print()                                                     #Put it all together for the user
            i += 1                                                      #Close the overall while loop
    elif decision == "construction":
        symbols1 = 0                                                    #Flags for the construction structure
        lowercase1 = 0
        symbols2 = 0
        lowercase2 = 0
        print()
        word2 = input("What is the first word? :")                      #Input for first word
        word3 = input("What is the second word? :")                     #Input for second word
        print()
        while lowercase1 != 1 or symbols1 != 1 or lowercase2 != 1 or symbols2 != 1: #While loop to check both words for flags
            if symbols1 == 0:                                           #Checks for first word for symbols, whitespace, or number
                if word2.isalpha() == True:
                    symbols1 += 1
                else:                                                   #If symbols, whitespace, or numbers; promps user
                    print("Your 1st entry has non alphabet symbols, a whitespace or numbers. Try Again.")
                    print()
                    word2 = input("What is the first word? :")
                    word3 = input("What is the second word? :")
                    print()
            elif lowercase1 == 0:                                       #Checks for first word for uppercase
                if word2.islower() == True:
                    lowercase1 += 1
                else:                                                   #If there is uppercase promps user
                    print("Your 1st entry has uppercase letters. Try Again.")
                    print()
                    word2 = input("What is the first word? :")
                    word3 = input("What is the second word? :")
                    print()
            elif symbols2 == 0:                                         #Checks symbols, whitespace, and numbers for second word
                if word3.isalpha() == True:
                    symbols2 += 1
                else:                                                   #If symbols, whitespace, or number promps user
                    print("Your 2nd entry has non alphabet symbols, a whitespace or numbers. Try Again.")
                    print()
                    word2 = input("What is the first word? :")
                    word3 = input("What is the second word? :")
                    print()
            else:                                                       #Checks uppercase for second word
                if word3.islower() == True:
                    lowercase2 += 1
                else:                                                   #If uppercase, promps user
                    print("Your 2nd entry has uppercase letters. Try Again.")
                    print()
                    word2 = input("What is the first word? :")
                    word3 = input("What is the second word? :")
                    print()
        else:                                                           #If all flags are good we can start puting the two words together
            word4 = ''                                                  #Set an open variable for word4
            if len(word2) % 2 == 0 and len(word3) % 2 == 0 and len(word2) == len(word3): #Checks for even number of letters in both words
                for a in range(len(word2)):                             #Cycle through each number of letters for both
                    word4 += word2[a] + word3[a]                        #Adds the two letters from each word sequentially to word4
                print("With your first word :", word2,"and your second word :", word3)
                print("We made the word :", word4)                      #Output results to user
                print()
                i += 1                                                  #Close the overall while loop
            else:                                                       #If entry is not even or have different even numbers, promps user
                print("One of your entries had an odd number of letters or not the same length as the other. Please try again.")
    else:                                                               #If decision entry is not construction or destruction, promps user
        print("That wasn't one of the choices")
        print()
        decision = input("destruction or construction? :")

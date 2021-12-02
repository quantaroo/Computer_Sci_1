#CPCS230-03
#Assignment 5

def couple_name(name_1,name_2):                         #Couple function with both variables
    '''Puts first split and second split together to make one name'''
    name_1 = name_1.lower()                             #makes all lowercase for first and second entry
    name_2 = name_2.lower()
    fname=str(first_split(name_1))                      #Runs first split function on first entry
    sname=str(last_split(name_2))                       #Runs second split function on second entry
    result=fname+sname                                  #Puts the two results from both functions to make one word
    print()
    print("Your new name is :", result.capitalize())    #Outputs the result and also capitalizes the first letter to make it proper

def first_split(name):                                  #First split function
    '''Takes the first entry and converts it to a mergible form'''
    vowels = "AaEeIiOoUu"                               #reference for call back for vowels
    for i in range(1,len(name)):                        #Loops through characters to find first vowel and then returns the first chunck of word with leading constant
        c = name[i]
        if c in vowels:
            name1= name[:i+2]
            break
    return name1

def last_split(name):                                   #Second split function
    vowels = "AaEeIiOoUu"                               #Reference for call back for vowels
    if name[0] in vowels:                               #if there is a vowel on the first character, returns the whole name
        return name
    elif len(name)<=3:                                  #if there is less than 3 characters, return the last 2 characters
        return name[1:]
    else:                                               #for loop to find the first vowel and skip two character spots over and return the last portion
        for i in range(1,len(name)):
            c=name[i]
            if c in vowels:
                name2 = name[i+2:]
                return name2
                break
print()                                                             #Introduces the user
print("We will now make a new name with two given names ^.^ ")
print()                                                             #First input from user
name_1 = str(input("Please enter the first name :"))
print()                                                             #Second input from user
name_2 = str(input("Please enter the second name :"))
i = 0
symbols1 = 0                                                        #Flags for the construction structure
symbols2 = 0
while i == 0:
    while symbols1 != 1 or symbols2 != 1:                           #While loop to check both words for flags
        if symbols1 == 0:                                           #Checks for first word for symbols, whitespace, or number
            if name_1.isalpha() == True:
                symbols1 += 1
            else:                                                   #If symbols, whitespace, or numbers; promps user
                print("Your 1st entry has non alphabet symbols, a whitespace or numbers. Try Again.")
                print()
                name_1 = str(input("Please enter the first name :"))
                print()
                name_2 = str(input("Please enter the second name :"))
                print()
        else:                                                       #Checks symbols, whitespace, and numbers for second word
            if name_2.isalpha() == True:
                symbols2 += 1
            else:                                                   #If symbols, whitespace, or number promps user
                print("Your 2nd entry has non alphabet symbols, a whitespace or numbers. Try Again.")
                print()
                name_1 = str(input("Please enter the first name :"))
                print()
                name_2 = str(input("Please enter the second name :"))
                print()
    else:                                                           #If all flags are good we can start putting the two words together
        couple_name(name_1,name_2)
        print()
        i += 1

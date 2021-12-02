#CPCS230-03
#Assignment 5

def complement(DNA_String):         #Create the function for complement
    '''Function that changes DNA to its complement DNA sequence'''
    comp = ""                       #Create empty string to put complemented looped characters
    for x in DNA_String:            #Create for loop for complement DNA character
        if x == 'A':                #if and elif statements to check each possible character
            comp = comp + 'T'
        elif x == 'T':
            comp = comp + 'A'
        elif x == 'C':
            comp = comp + 'G'
        else:
            comp = comp + 'C'
    return comp                     #Function gives the result from the for loop comp

def reverse_complement(DNA):        #Create the function for the reverse complement
    '''Function that changes DNA to its reverse complement DNA sequence'''
    DNA = DNA[::-1]                 #Reverse the DNA input entry
    Reverse_DNA = complement(DNA)   #Runs the reverse DNA throu the complement function
    return Reverse_DNA              #Function gives the result from the complement function


#Input on which transformation the user wants
choice = str(input("What do you want to do with your DNA, 'complement' or 'reverse_complement'? :"))
print()
#Constant for while loop
z = 0
#While loop for correction entry form choice input
while z == 0:
    #if statement to check for complement input
    if choice == 'complement':
        #constant for while loop
        i = 0
        #input on what characters for DNA sequence
        DNA_String = str(input("What is the DNA Sequence (only 'A','T','C','G'(total of 4 characters)) :"))
        #transform input to upper case
        DNA_String = DNA_String.upper()
        #while loop to check for correct input
        while i == 0:
            #If conditions of ACTG and 4 characters are true, run the complement function
            if ('A' in DNA_String or 'T' in DNA_String or 'C' in DNA_String or 'G' in DNA_String) and len(DNA_String) == 4:
                print("With your DNA entry :", DNA_String)
                print("Your compliment is :", complement(DNA_String))
                #satify both while loops
                i = 1
                z = 1
            #elif statement to check for 4 characters, statement and re entry of input of DNA sequence
            elif len(DNA_String) != 4:
                print("You did not put the valid amount of character entries. Please try again. (^_^) ")
                print()
                DNA_String = str(input("What is the DNA Sequence (only 'A','T','C','G'(total of 4 characters)) :"))
                DNA_String = DNA_String.upper()
            #else to check for ATCG, statement and re entry of input of DNA sequence
            else:
                print("You did not put the write letter entries. Please try again. (^_^) ")
                print()
                DNA_String = str(input("What is the DNA Sequence (only 'A','T','C','G'(total of 4 characters)) :"))
                DNA_String = DNA_String.upper()
    #Check if entry is reverse complement
    elif choice == 'reverse_complement':
        #constant for while loop
        i = 0
        #input for the reverse complement DNA sequence
        DNA = str(input("What is the DNA Sequence you want to reverse? (only 'A','T','C','G'(total of 4 characters)) :"))
        #transform input to upper case
        DNA = DNA.upper()
        ##while loop to check for correct input
        while i == 0:
            #If conditions of ACTG and 4 characters are true, run the reverse complement function
            if ('A' in DNA or 'T' in DNA or 'C' in DNA or 'G' in DNA) and len(DNA) == 4:
                print("With your DNA entry :", DNA)
                print("Your reverse complement is :", reverse_complement(DNA))
                #satify both while loops
                i = 1
                z = 1
            #elif statement to check for 4 characters, statement and re entry of input of DNA sequence
            elif len(DNA) != 4:
                print("You did not put the valid amount of character entries. Please try again. (^_^) ")
                print()
                DNA = str(input("What is the DNA Sequence you want to reverse? (only 'A','T','C','G'(total of 4 characters)) :"))
                DNA = DNA.upper()
            #else to check for ATCG, statement and re entry of input of DNA sequence
            else:
                print("You did not put the write letter entries. Please try again. (^_^) ")
                print()
                DNA = str(input("What is the DNA Sequence you want to reverse? (only 'A','T','C','G'(total of 4 characters)) :"))
                DNA = DNA.upper()
    #If entry is not either of the two, statement and re entry
    else:
        print("That wasn't one of the choices. Please try again. (^_^)")
        print()
        choice = str(input("What do you want to do, 'complement' or 'reverse_complement'? :"))

#CPCS 230-03
#Assignment 7

def read_to_list(input_file):
    '''Takes the input file and generates a list of words'''
    while True:                                                                 #while loop to check for file input error FileNotFoundError
        try:
            input_file = open(input_file, 'r')
            break
        except FileNotFoundError:
            print("invalid file name.")
            input_file = input("What is the file you want to input? : ")
    input_str = input_file.read()                                               #generates one long string from file
    input_list = input_str.split()                                              #splits the string into a list, divided by whitespace
    output_list = []                                                            #empty output list
    for word in input_list:                                                     #for loop to strip words of punctuations and append the list to the output list
        word = word.strip('-.,?!\"\'')
        if word != "":
            output_list.append(word)
    input_file.close()                                                          #closes the input file
    return output_list

def write_five(output_list,file_name):
    '''takes the output list divids the list by 5 word lines and prints those lines on to a created file'''
    five_words = []                                                             #empty 5 word list
    output_file = open(file_name, 'w')                                          #creates the file that the usere inputed
    for i in range(0, len(output_list), 5):                                     #A loop that makes a list of five word strings for the entire output list
        five_words.append(" ".join(output_list[i:i+5]))
    for line in five_words:                                                     #writes the line from the five word list to the output file
         output_file.write(line)
         output_file.write("\n")
    output_file.close()                                                         #closes the output file
    return

input_file = input("What is the file you want to input? : ")                    #input from user on the file name to input
output_list = read_to_list(input_file)                                          #run function on creating string list from input file
output_file = input("What is the file name you want to create? : ")             #input from user on output file name
write_five(output_list,output_file)                                             #run function to print the 5 word lines onto the new output file

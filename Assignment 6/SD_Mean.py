
def obtain_numbers():
    '''obtains the numbers from the user'''
    numbers = []                                             #empty list to put the numbers
    i = 0                                                    #constant for the while loop
    while i == 0:                                            #while loop to help loop through entries
        imp_num = input('Enter a positive number (Enter a negative number to quit): ')
        while imp_num == '' or imp_num.isalpha() == True:    #check for enter space and alphabet characters(if alpha and number will have error)
            print("Invalid response. Try again")
            imp_num = input('Enter a positive number (Enter a negative number to quit): ')
        else:
            imp_num = int(imp_num)
            if imp_num < 0:                                  #if entry is negative it returns the whole list and ends loop
                return numbers
            elif imp_num > -1:                               #if entry is 0 or greater enters the entry to the list
                numbers.append(imp_num)
            else:                                            #if entry isn't an integer, returns the user to the top of the loop
                print("Invalid response. Try again")

def print_sorted(numbers):
    '''Takes a list of integers as input and prints them in sorted order'''
    numbers.sort()                                           #sorts the list from smallest to greatest
    print("Here is your sorted list: ", numbers)             #print the result from result
    print()
    return numbers                                           #returns the sorted list

def compute_mean(numbers):
    '''Takes a list of integers as input and returns the mean (average) of the list'''
    total = sum(numbers)                                     #totals the sum of the list
    return total / len(numbers)                              #returns the average (total / number of entries)

def compute_variance(numbers):
    '''Takes a list of integers as input and returns the variance of the list.'''
    mean = compute_mean(numbers)                             #sets mean to the average of the entry list
    variance = 0                                             #variance set at initial 0 for the for loop
    for i in numbers:                                        #create a for loop to add up the upper portion of the variance equation
        variance += (i - mean) ** 2
    return variance / len(numbers)                           #returns the variance / number of entries in the list to complete the equation

def compute_standard_dev(variance):
    '''Takes the variance as input and returns the standard deviation'''
    return variance ** 0.5                                   #returns the square root of the variance to get the standard deviation

numbers = obtain_numbers()                                   #executes the function to get the list of numbers and setting it to numbers
print_sorted(numbers)                                        #executes the function for sorting and printing the sorted list
variance = compute_variance(numbers)                         #executes the function to compute the variance and setting it to variance
print("Mean              : ", round(compute_mean(numbers),4))#prints out the mean and rounded it out 4 decimal spaces
print()
print("Variance          : ", round(variance, 4))            #print out the variance and rounded it out 4 decimals spaces
print()                                                      #print out the standard deviation and rounded it out 4 decimal spaces
print("Standard Deviation: ", round(compute_standard_dev(variance),4))
print()

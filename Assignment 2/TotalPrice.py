#CPCS230-03
#Assignment 2 TotalPrice

print("We will find the total price of an item given a tax")

#User Input for price of item
price_item = float(input("Please enter the price of the item: "))

#Calculate the total price of the item after tax with if statement
if price_item >= 0:                                                      #Check price is positive
    tax = float(input("Please enter the tax: "))                         #User input for tax
    if tax >= 0:                                                         #Check price is positive
        total_price = round(((price_item * (tax*0.01)) + price_item),2)  #Calculate total price
        print("With the given price of the item $", price_item,"and the tax rate of:", tax,"%")
        print("The total price for the item is: $", total_price)         #print results
    else: print("Tax should be positive")                                #print if tax is negative
else: print("Price should be positive")                                  #print if price is negative

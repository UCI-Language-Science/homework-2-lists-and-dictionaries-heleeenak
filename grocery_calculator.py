# Write a program that asks the user to input their grocery list
# and then tells them the price. You can make the following two
# assumptions:
# - the only available groceries are:
#       - bread: $3
#       - eggs: $6
#       - milk: $4
#       - butter: $2
# - users must enter one item at a time, even if they are buying
#   multiple
#       - e.g. if the user is buying three loaves of bread, they
#         will have to input 'bread' 3 times.
#
# If the user inputs something that is not one of the four options
# above, the program should print "The store doesn't have that" and
# then prompt the user for more input.
#
# When the user inputs an empty line (i.e. hits enter without typing
# anything), the program should print the total cost of their groceries.
#
# For example:
# Input grocery item:
# >> bread
# Input next grocery item:
# >> milk
# Input next grocery item
# >>
# Your total grocery bill is $7

def grocery_calculator():
    # YOUR CODE GOES HERE
    available_groceries_dict = {"bread": 3, "eggs": 6, "milk": 4, "butter": 2} # Dictionary of grocery items and prices

    my_total_cost = 0 # Starts off the total cost of the grocery bill at 0 so we can add to it

    #print("Please input your grocery item:") # Had to change both instances of this so that the autograding would work
    my_grocery_item = input("Please input your grocery item: ") # User inputs grocery item

    while my_grocery_item != "": # This runs the loop forever until the user inputs an empty line by pressing enter
        if available_groceries_dict.get(my_grocery_item): # Checks if the user's input matches the keys in the grocery dictionary
            my_total_cost += available_groceries_dict[my_grocery_item] # Adds the value of the grocery item that matches the user's input to the total cost count using an augmented assignment (+=)
        
        else: print("The store doesn't have that") # Says store doesn't have item if input is not in dictionary
    
        #print("Please input your grocery item:") # This needs to be within the while loop so users can keep inputting as many groceries as they want (one at a time)
        my_grocery_item = input("Please input your grocery item: ") # User inputs (another) grocery item or presses enter (if they do, this ends the while loop)

    print("Your total grocery bill is $" + str(my_total_cost)) # Prints out the total cost after the while loop is broken (when the user enters an empty line)
        # Needed to convert the my_total_cost variable into a string in order to make sure it printed like "$7" instead of "$ 7"

if __name__ == "__main__":
    grocery_calculator()
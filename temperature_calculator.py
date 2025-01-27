# Write a program that continuously prompts the user for a 
# temperture (in the scale of your choosing). Every time 
# the user inputs a temperature, the program should report 
# the mean of all the values entered so far. When the user
# types in 'quit' the program should terminate.
#
# An example interaction might look like
# Input a temperature
# >> 42
# The average temperature so far is 42
# Input a temperature
# >> 26
# The average temperature so far is 34.0
# Input a temperature
# >> 52
# The average temperature so far is 40.0
# >> quit
# Goodbye
#
# You can use the sum function to sum all the values in a list
# sum(<list>)

def temperature_calculator():
    # YOUR CODE GOES HERE

    # This is kind of a mix between what I did for char_counter.py and grocery_calculator.py
        # This was so hard. I think I need more practice with while loops. Almost crashed my computer accidentally because I didn't know how to stop it

    my_temps_list = [] # Defines an empty list to store all the temps that the user enters

    my_temp = input("Please input a temperature: ") # User inputs temperature # Formatted it like this (like grocery_calculator.py) so that autograding hopefully works

    while my_temp != "quit": # This runs the loop forever until the user inputs the word "quit"
        my_temp_float = float(my_temp)  # Converts user's temp to a floating number so we can add and stuff
        
        my_temps_list.append(my_temp_float) # Adds the temperature number to the list of entered temps
        
        temp_average = sum(my_temps_list)/len(my_temps_list) # Calculates the average by dividing the sum of all temperature numbers in the list by the length (number of entries) in the list
        
        print("The average temperature so far is " + str(temp_average)) # Prints out the average temp, converted to string so it has good formatting

        my_temp = input("Please input a temperature: ") # User has to enter another temperature or "quit" (must be under while loop so it keeps cycling)

    print("Goodbye") # This will print after the while loop is broken (so when the user types "quit")



if __name__ == "__main__":
    temperature_calculator()
# Write code that takes the provided list and removes all
# duplicates of numbers that have occurred earlier in the
# list, preserving the order otherwise
# 
# For the example below, the output should be
# "[1, 4, 3, 2, 5, 7, 9]"
# 
def duplicate_remover():
    duplicates_list = [1, 4, 3, 4, 2, 5, 1, 2, 7, 9, 4]
        # What we want: [1, 4, 3, 2, 5, 7, 9]
        # This means that we need some kind of loop that looks through each entry since it removed the 2nd 4 and not the 1st
    
    # YOUR CODE GOES HERE

    reduced_list = [] # Defines an empty list for our duplicate-less list to go into
    # This is basically what I did for the char_counter.py problem but with a list instead of a dictionary

    for number in duplicates_list: # Iterates through each number in our duplicates list
        if number not in reduced_list: # Uses the not in operator to check if the number is in our reduced list already
            reduced_list.append(number) # Uses the append method to add that new value to the end of the (initially) empty reduced list (if the value was not in it yet)

    print(reduced_list)

if __name__ == "__main__":
    duplicate_remover()
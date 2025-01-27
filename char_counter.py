# Write a program that asks the user to input a string and then
# prints out the counts of each character used in the string.
#
# For example, if the input string is 'hello, world!' the output
# should be something like
#
# 'h': 1
# 'e': 1
# 'l': 3
# 'o': 2
# ',': 1
# ' ': 1
# 'w': 1
# 'r': 1
# 'd': 1
# '!': 1
#
# You don't have to match this format exactly, but it's important
# for the autograder that the message you print contains
# each of the character/count pairs in the following format.
# 
# '<character>': <count>
#
# You should get input from the user using the input function. Your
# code should work for arbitrary strings, including the empty string.

def char_counter():
    # YOUR CODE GOES HERE
    print("Please enter a string:") 
    my_string = input() # User enters string
    # Note from class: tuple("hello world") splits up the string "hello world" into a tuple of individual characters

    my_list = list(my_string) # Converts the string into a list
    #print(my_list)

    character_counts = {} # Defines an empty dictionary for us to store our character counts in

    for char in my_list: # Goes through each character in the list version of our string 
        if character_counts.get(char) != None: # Checks if our dictionary contains each character (if get returns a value that is not equal to None)
            character_counts[char] = character_counts[char] + 1 # Add a vote for each unique character and put it in the dictionary

        else: # Otherwise... (when get returns a value equal to None, so no instance of that character exists in the dictionary yet)
            character_counts[char] = 1 # Sets the count equal to 1 (starts off the character count at 1 for each character in the list)

    print(character_counts)


if __name__ == "__main__":
    char_counter()
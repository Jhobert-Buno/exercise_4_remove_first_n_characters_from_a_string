# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.


# pseudocode

# ask for the word
word = input("Input Word: ")

# ask for the n 
nth_number = int(input("Input Number: "))

# functions
def remove_characters (word, nth_number):
    print("Original Word: ", word)
    remove_string = word[nth_number:]

    return remove_string

print("New Word: ", remove_characters(word, nth_number))


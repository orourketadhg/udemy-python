# challenge

# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

stringInput = set(input("enter a string: "))

vowels = {"a", "e", "i", "o", "u", " "}

stringInput.difference_update(vowels)
print(sorted(stringInput))

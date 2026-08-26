# Some examples of the variables:
name = "Jack"
print(name)

name = "Jose"
print(name)

# First Way to do the code (Split everyting into variables)
name = input("Whats your name?\n")
words_numbers = len(name)
print(f"Your name has:{words_numbers} words!")


# Second way to do the code (The same code but this one is just in one line)
print(f"Your name has:{len(input('Whats your name?\n'))} words!")

# Some examples of the names that you can put in the variables
n = "Jose"
l = len(n)
print(l)

username_of_this_person = "JoseAntonio"  # Additionally, whenever you want to put a space in the text, you must use an underscore.
lenght = len(username_of_this_person)

name = "Jose"
length = len(name)
print(length)

username_of_this_person = "JoseAntonio"
lenght = len(
    username_of_this_person
)  # Another think that is correct to use is to put numbers on your variables but in a specific way (like this: lenght23948349 )
# But you must never put the number before the text (like this: 1083438472lenght), because otherwise it will cause an error called *NameError*.

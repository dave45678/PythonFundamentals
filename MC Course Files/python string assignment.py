# Your next assignment is to type in the while loop below and append all your answers 
# to a variable named history. History will be a string. We'll learn about lists next.
# For now, just append to the string.
# and show history after the user quits

# We previously looked at the for loop. Another type of loop is the while loop.
# The while loop will repeat a set of instructions endlessly until something
# prompts it to quit. The technical term for that is a sentinel. Think of the sentinel
# as a railroad crossing or a traffic light. You keep going until it says stop. (While light is green...)
# Here is a while loop for getting input from a user

while True:
    answer = input("Enter a movie you like or press 'q' to quit: ")
    if answer.lower() == 'q':
        break
    else:
        print("You entered " + answer)

print("You will now exit the program.")

# After you complete the above assignment then add a counter to the movies
# and print the counter along with the movie name.
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

'''
A string is a sequence of zero or more characters. 

The len() function returns the number of characters in its string argument. 
Each character occupies a position in the string. 
The positions range from 0 to the length of the string minus 1.
A string is immutable. This means it does not change once it is created.

The subscript operator [] can be used to access a character at a given position in a string.
The operand or index inside the subscript operator can be used to access a character at a given position 
in a string. The operand or index inside the subscript operator must be an integer expression whose value
is less than the string's length.

A subscript operator can also be used for slicing - to fetch a substring from a string.
Use the subscript operator as myString[3:5]


'''
s = "This is my string"
i = 0
numberSpaces = 0
print(len(s))
# print the character at the 4th position
print(s[4])
print("Printing the subscript from 5 to 10: " + s[5:10])

for eachCharacter in range(len(s)-1,-1,-1):
    print(s[eachCharacter],end="")
    if s[eachCharacter]==" ":
        numberSpaces += 1
    if s[eachCharacter].lower() == 'i':
        i +=1
        
print("\n")
print("There are " + str(i) + " i's in the string")
print("There are " + str(numberSpaces) + " spaces.")

'''
String Assignment
Using the information above and what you have learned so far 
write  a loop that counts the number of spaces in a string
write a program that prompts a user for input and counts 
the number of occurrences for each letter. 
Print out a summary as follows:
A to E - 7 occurrences
F to J - 2 occurrences
K to O - 7 occurrences
P to T - 3 occurrences
U to Z - 5 occurrences
'''
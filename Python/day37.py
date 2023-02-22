# Day37 - Slice it Up!

# May the force be with you as you slice it up! Create your Star Wars name with string slicing.

""" String Slicing
Aren't strings brilliant? Yes, yes they are.

However, sometimes we might want to take part of a string to use it somewhere else. Sometimes, we might want to look at just the first letter of a string or chop it into chunks.

To do this, we use string slicing.

A string isn't just one big lump of text. In fact it's a list of individual characters. This means that we can use indexing just like we did with lists waaay back on Day 32.

By giving our program an index, we can specify which part of the string to chop out. 🪓🪓

Pssst... When you see '#' followed by green text, these are comments for you. The computer will ignore it.

Slicing
To slice a single character from a string, you use the index of that character in square brackets [] just like you'd use with a list! Gasp!

👉 Let's see what happens: """

myString = "Hello there my friend."
print(myString[0])

# This code outputs the 'H' from 'Hello'

""" To slice more than one character, you use two indices (yes that is the plural form of 'index'): the start character and one after your desired end character.

👉 Let's try it: """

myString = "Hello there my friend."
print(myString[6:11])

# This code outputs 'there'.

# 👉 Leaving the first index blank defaults to 'start from index 0'.

myString = "Hello there my friend."
print(myString[12:])
# This code outputs 'my friend.'.

""" The Secret Third Argument
Adding a third argument to the square brackets [] specifies the gap left between characters.

👉 Try to print every other character in the word 'hello': """

myString = "Hello there my friend."
print(myString[0:6:2])

# This code outputs 'Hlo' (every second character from 'Hello').

# 👉 Can you print every third character in the whole string?

myString = "Hello there my friend."
print(myString[::3])

# This code outputs 'Hltrmfe!' (every third character from the whole string).

""" Using a negative number in the third argument can be super useful. It starts the slice from the end of the string instead of the beginning.

👉 Can you print the string backwards?! """

myString = "Hello there my friend."
print(myString[::-1])

#This code reverses the string, outputting '.dneirf ym ereht olleH'

""" Play around with this third secret argument. What else can you do?

Split
👉 split lets us split a string into a list of individual words by separating it at the space characters. """

myString = "Hello there my friend."
print(myString.split())

""" #This code outputs ['Hello', 'there', 'my', 'friend.']

What can you split? """

myString = "Hello there my friend."
print(myString[0:5])

""" It won't stop printing the same character
👉 What is the problem here? """

myString = "Hello there my friend."
print(myString[0:4:1])

myString = "Hello there my friend."
print(myString[0:11])

myString = "Hello there my friend."
print(myString[0:11:1])

""" 👉 Day 37 Challenge
This is the challenge you're looking for. This program will generate your Star Wars Name.

Ask the user to input their first & last names.
Slice the first 3 letters of the first name.
Slice the first 3 letters of the last name (surname).
Join them together. Ideally change the case so that it looks good - think fStrings or .upper()/.lower(). This is the user's Star Wars first name.
Now ask the user for their mother's maiden name and the city where they were born. (Maiden name is the last name they had before they got married. If you are not sure, make up a last name.)
Combine the first two letters of the maiden name with the last 3 letters of the city to make the user's Star Wars last name. Remember, fStrings and .upper()/.lower().
Finally, print them both as part of a sentence.
🥳 Extra points for getting all the inputs with just one input command and the split function.

Example:

🌟Star Wars Name Generator🌟

Input your first name > David

Input your lastname > Morgan

Input your mother's maiden name > Jones

Input the city where you were born > Cardiff

Your Star Wars name is Davmor Joiff

Hints:

To get charaters from the beginning of a string, leave the first argument blank. ex: [:3] gets the first 3 characters.
To get charaters from the end of a string, make the first argument a negative number for how many charaters to get. Leave the last argument blank. ex: [-5:] gets the last 5 characters.
fString formatting uses .title for first character capitalization and .lower for all lower case.
Use fStrings to join the sliced characters to a new variable as you get the correct characters from each string.
For extra points, get the user to input all info at once separated by spaces. """


print("STAR WARS NAME GENERATOR")

all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()

first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")
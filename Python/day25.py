# Send it Back

# The `return` command will allow you to really start building some epic, automated video games.

""" Return Command

Let's go deeper into subroutines. Can they send information back to the main part of the program?

Let's do this with the return command.

The return command sends some information back to the part of the code that called it. This means the function call is replaced with whatever was returned.

We saw this before with importing libraries and random numbers. We could use the random number wherever we wanted.

Pin Picker
This subroutine creates a random pin number for us. This subroutine (called pinPicker) has the parameter called number (how many numbers I want to have in this pin). Then, there is a string (called pin) that is empty and a for loop that is used to create a defined amount of random numbers. The variable number controls how many times the loop will add the new number to the pin. This is done through += and concatenating new values. We will cast the random number as a string so it can be concatenated together.

Then...the magic...we return the pin.

👉 Let's see what happens:

#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have

def pinPicker(number):
  import random
  pin = "" #this is the empty string
  for i in range(number): #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
  return pin
    
pinPicker(4) #4 means we want 4 random numbers

Nothing happens? Why?

The line pinPicker(4) that calls for a 4 digit pin is being replaced by a 4 digit pin. (That's great, but I don't see that happening...)

We are not telling the computer to do anything with the string that was created. How do we make the string appear?

With print of course!

👉 Let's assign a variable to pinPicker:

myPin = pinPicker(4)

👉 Now print it out:

print(myPin)

👉 That was quite a doozy. Take time to pause and really try this code out. """

def area_square(side1, side2):
  area = side1 * side2
  return area

area = area_square(4, 12)
print(area)

""" 👉 Day 25 Challenge
Let's extend Day 24's project and create a health stats generator for a character in a video game.

Create a subroutine that rolls a dice of any size and returns that number.
Then, create a second subroutine that rolls one six-sided dice and one eight-sided dice.
Multiply the number from the six-sided dice and eight-sided dice together and return that subroutine as a character's health stats for a video game.
Print out the character's health stats.
Add a loop to give the user the option to generate health stats for another character.
(We genuinely see this in video games!)

🥳 Extra points if you ask for the character's name and double extra points if you use different colors!

⚔️ Character Stats Generator ⚔️

Name your warrior: Agnes
Their health is: 20hp

Name your warrior: Ian
Their health is: 6hp

Name your warrior: Penelope
Their health is: 48hp

Hints:
Import your library first.

Create one subroutine for a dice of any number and return it.

Create a subroutine that rolls a dice with numbers 1-6 and a dice with numbers 1-8 and multiplies the two numbers together. Return that subroutine.

Ask the user to name their character and print that character's health stats.

Create a while loop to allow the user to generate a new character's health stats.
"""

#25% Complete...
#Go You! 🎊 Tell us what you think of 100 Days of Code on Replit with this short survey.

import random

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health

print("⚔️Character stats generator⚔️")
  

haveACharacter = "yes"

while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = str(roll_6_and_8())
  print("Their health is ", health,"hp" ) 
  haveACharacter = input("Want to create another character?")

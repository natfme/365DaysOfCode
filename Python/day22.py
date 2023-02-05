# Day 22 - Use other people's code

# ----------------------------- Libraries -------------------------------

# Let's be sneaky and learn how to use other people's code to make your life easier.

"""
Libraries

Libraries are collections of code that other people have written. Video games often use massive libraries (for example: game engines) to create the epic water reflections, 3-D graphics, etc.

We are going to start a bit smaller by just generating random numbers. (After all, random numbers are the basis of most games).

Random library
We can use a library by writing import and then the library name.

This should always be one of the first lines of code.

👉 Let's import a library that will generate random numbers: (Does this look familiar from Day 14's Rock, Paper, Scissors game?)


import random

How random works
In the code below, I have created a variable, 'myNumber'. I am making it equal to a random number given to me by the randint (random integer) library. I add the lowest number (1) and the highest number (100) that can be picked and the computer will generate a number at random.

import random
myNumber = random.randint(1,100)
print(myNumber)

👉 Give it a try!

What do I do with libraries?
In the past, we had to hardcode the value users were looking for (remember the higher or lower guessing game...).

With random, we can generate a number that even we don't know. (Sounds similar to gaming, huh?)

import random

myNumber = random.randint(1,100)
print(myNumber)

import random

for i in range(10):
  myNumber = random.randint(1, 100)
  print(myNumber)"""

# 👉 Day 22 Challenge

"""
Copy and paste your code from Day 18.

We are going to make a change to this project:

Make the number generator completely random between 1 and 1,000,000. Now, the game will always have the user guess a random number each time (now the user can't cheat...)
"""

from random import randint, random

print("Guess the Number")
print("One-Million-To-One")
print("Picking a number between 0 and 1,000,000")
number1 = randint(0,1000000)
counter = 1

while True :
    number = int(input("What is your guess: "))
    if number < number1 -1000:
        print("Too low")
        print()
        counter += 1
        continue
    elif number > number1 + 1000:
        print("Too high")
        print()
        counter += 1
        continue
    else:
        print("Correct!")
        print()
        break

print(f"It took you {counter} guess to get it correct!")

# Hints

"""
* Remember to import your library first and do NOT add it in the loop.
* You can keep a lot of Day 18's code, but need to add the random library.
"""

print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")

import random
attempt = 1
myNumber = random.randint(1,1000000)

while True: 
  user_guess = int(input("Pick a number between 1 and 1,000,000: "))
  if user_guess < myNumber:
    print("That number is too low. Try again!")
    attempt += 1
  elif user_guess > myNumber:
    print("That number is too high. Try again!")
    attempt += 1
    continue
  elif user_guess == myNumber:
    print("You are a winner! 🥳🥳")
    break 
    exit()
  else:
    print("That is not a number I recognize.")
print("It took you", attempt, "attempt(s) to get the correct answer.")
# Day 18 - Guess the Number

# Build a 'Guess the Number' game where the user has to read your mind and guess the number you are thinking...

"""
👉 Day 18 Challenge

We are going to build a "Guess the Number" guessing game.

You are going to use a while loop and some of the concepts from the past few days.

1. Start by picking a number between 0 and 1,000,000. This will be your first variable.

Hint: Essentially, what do you want the correct number to be. Create a variable for that number.

2.<Create a while loop to keep asking the user to guess your number.

3. If they are too low, tell them "too low." If they guess too high tell, them "too high."

Hint: You will need to include if statements here with logical operators. Include the correct number variable you created at the beginning in these if statements.

4. If the user guesses correctly, tell them they are a winner (maybe add a fun emoji too!)

Hint: If they are a winner, they need to get out of the loop. How do you do that?

5. Count the number of attempts it took for the user to guess number. Make sure you only show that after they get the answer correct.

Hint: Create a counter before the while loop and print the number of attempts after the user is a winner. Don't forget to count attempts using += in the loop.

Extra challenge: If the user types a negative number, exit program.
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

#---------------------------------------------------------------------------

print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")

correct_number = 2300
attempt = 1

while True:
  user_guess = int(input("Pick a number between 1 and 1,000,000: "))
  if user_guess < 0:
    print("Now we'll never know what the answer is …")
    exit()
  if user_guess < correct_number:
    print("That number is too low. Try again!")
    attempt += 1
  elif user_guess > correct_number:
    print("That number is too high. Try again!")
    attempt += 1
    continue
  elif user_guess == correct_number:
    print("You are a winner! 🥳🥳")
    break 
  else:
    print("That is not a number I recognize.")
print("It took you", attempt, "attempt(s) to get the correct answer.")
# Day 16 - Make it Stop!

# Whoops. You made an accidental infinite loop...and nightmare. Introducing..."while True"...to make it stop.

"""
while True Loop
On Day 15, you learned how to create a while loop. However, there are a lot of moving parts that can turn the while loop into an accidental infinite loop...and a nightmare.

Introducing the while True loop...

👉Let's try it out.
What do you think the below code does?

Remember you can use the big Stop button on the top if your program does not end.

while True:
  print("This program is running")
print("Aww, I was having a good time 😭")
This type of loop only has two conditions: True and False. Make note of the capital "T" and "F".

Fun Fact

A Boolean Loop has two values: True or False. Impress your friends and tell them you know how to use a Boolean Loop.

In this loop, I am saying to the computer:

"while True is True...do this over and over again."

Yes, we made an infinite loop, but hold on...

Make it stop
There is a way to stop the loop with the word break. This exits the loop and stops all code at that point. Even if there is more code written after break that is inside the loop.

After break, the computer jumps out of the loop to the next unindented line of code.

👉 Let's try it out
Run the code below and notice how the loop will continue until break. Then the next line of unindented code will run.

while True:
  print("This program is running")
  goAgain = input("Go again?: ")
  if goAgain == "no":
    break
print("Aww, I was having a good time 😭")

Name Error
👉 What is the error here?

counter = 0
while true:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")

Syntax Error
👉 What about this one? What happens when you hit run?

counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
addAnother = input("Add another? ")
if addAnother == "no":
  break
print("Bye!")

Fix My Code
👉 Try and fix this code which is full of errors.
"""

while True:
  color = input("Enter a color: ")
  if color == "red":
    break
  else:
    print("Cool color!")
print("I don't like red")

"""
The word 'true' needs to be capitalized for a while True loop.
The if statement needs ==.
There is an indention error with break.

👉 Day 16 Challenge
Create a "Name the Lyrics" game. Write your favorite song lyrics with a word or two missing. The user has to figure out the correct song lyric in as few attempts as possible. Find the true lyric master among you!

Example
Fill in the blank lyrics!
(Type in the blank lyrics and see if you are as cool as me.)

Never going to ______ you up.
put
Nope, try again.

Never going to ______ you up.
let
Nope, try again.

Never going to ______ you up.
give

Well done! It only took you 3 attempts.

Hint

Think of your while True loop as a replacement for the if statement.
Place your break after the code identifying the correct lyric answer.
"""

print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()

counter = 1
while True:
  lyrics = input("I don't wanna ______ a thing. ")
  if lyrics == "miss" or lyrics == "Miss":
    print("You got it!")
  else:
    print("Nope! Try again!")
    counter +=1
  if lyrics == "miss":
    break
print("Thanks for playing!")

print("You got the correct lyrics in", counter, "attempt(s).")
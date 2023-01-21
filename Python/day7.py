#Nesting Dolls Code
#Like nesting dolls, nest 'if' statements within 'if' statements. Create a game to find true fans of your favorite show.

""" Nesting
Nesting is where we put an if statement within an if statement using the power of indenting. The second if statement within the first if statement must be indented and its print statement needs to be indented one more time. """

tvShow = input("What is your favorite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favorite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
  else:
    print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")

order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger":
    print("Thank you.")
    cheese = input("Do you want cheese?")
    if cheese == "yes":
      print("You got it.")
    else: 
      print("No cheese it is.")
elif order == "pizza":
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes":
    print("We will add pepperoni.")
  else:
    print("Your pizza will not have pepperoni.")

#👉 Day 7 Challenge
#Fake Fan Question Generator

"""Wanna find out if someone else is a true superfan of the same show, movie or interest as you? Create a program that asks what someone is interested in and includes nested if statements to ask annoying follow-up questions to see if someone is the real deal!

Make sure you include multiple if/elif statements and nested if statements too!"""

favWriter = input("What is your favorite writer? ")
if favWriter == "Tolkien":
  print("wow, seriously?")
  faveCharacter = input("Who is your favorite character? ")
  if faveCharacter == "Aragon":
    print("Right answer")
  else:
    print("Nah, Aragon's the greatest")
elif favWriter == "George R.R Martin":
  print("Aww, it's a good writer")
else:
  print("Yeah, that's cool and all…")

#Day 8 - Affirmation Generator

#Project day! Show the world some love with an affirmation generator. Send good vibes each day with a personalized message.

""" Day 8 Challenge
Affirmations (or insults) Generator
Today's focus is using all the skills you have learned so far:

input and output
concatenation
if statements
nested if statements
Build a custom affirmations generator to give the user a customized affirmation each day of the week.

Make sure you ask the user for their name, the current day of the week, and a few of their favorite things. All of this information should be used to help you build your affirmations.

Day 8 Challenge

Affirmations (or insults) Generator
Today's focus is using all the skills you have learned so far:

input and output
concatenation
if statements
nested if statements
Build a custom affirmations generator to give the user a customized affirmation each day of the week.

Make sure you ask the user for their name, the current day of the week, and a few of their favorite things. All of this information should be used to help you build your affirmations.

Use concatenation to generate the affirmation.

If affirmations are not your jam, then you could do a daily joke or insult. Please don't be mean. Keep it light and funny.

Final challenge: Can you create if statements that do not care about capital or lowercase letters of names.
"""

print("""You look nice today

Today you're going to make an impact and change the world!

Keep on keeping going!""")

print("""Alright Baldy? How\'s tricks?

Dude, lose my phone number!

Not you again. Can you stop tapping your finders on my keyboard please?""")

print("Wholesome Positivity Machine")

print()

name = print("Who are you?")

print("waht do you want to achive?")

print("On a scale of 1 - 10 How do you feel today? (1: 😭, 10: 🥳)" )

print("""Hey {name}, keep your chin up! Today you're going to Tech people to code! in the most amazing way, simply by being you - YOU ROCK!""")

print("Mean Old Insult Machine")
      
name = print("Who are you?")

print("How mcuh hair do you have on your head?")

print("""On a scale of 1 - 10 How bald are you? (1: 🧑 10: 🥚)""")

print("""Hey {name} - yeah thought I wouldn\'t know you were because you didn\'t capitalise properly! Well get that egg-head and dry your eyes because some amazing insults are a-comimg...""")

#------------------------------------------------------------------------------
print("Hello. Welcome to your daily affirmation generator.")
name = input("What is your name?")

if name =="Mark" or name == "mark":
 DOW = input("What is the day of the week?")
 if DOW == "monday" or DOW == "Monday":
   print("It is going to be a great Monday", name)
 if DOW == "tuesday" or DOW == "Tuesday":
   print("What a wonderful Tuesday it is", name)
 if DOW == "wednesday" or DOW == "Wednesday":
   print("Happy Hump Day", name)
 if DOW == "thursday" or DOW == "Thursday":
   print(name,"your week is almost over!")
 if DOW == "friday" or DOW == "Friday":
   print(name, "It's FRIDAY!")

elif name == "David" or name== "david":
 DOW = input("What is the day of the week?")
 if DOW == "monday" or DOW == "Monday":
   print("It is going to be a great Monday", name)
 if DOW == "tuesday" or DOW == "Tuesday":
   print("You look great in that color", name)
 if DOW == "wednesday" or DOW == "Wednesday":
   print("You look chipper today", name)
 if DOW == "thursday" or DOW == "Thursday":
   print(name,"you are doing a great job!")
 if DOW == "friday" or DOW == "Friday":
   print(name, "it's FRIDAY!")
else:
 print("I do not know your name, but I hope you are having a great day!")
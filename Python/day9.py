#day 9 - Casting

""""Casting
If statements support more than ==. They support inequality symbols as well. Remember those <, >, and = signs you used in math way back when? Well they are back again, but this time they look a bit different."""

# equal
5 == 5

# not equal
3 != 5

# greater than
5 > 3

# greater than or equal to
5 >= 3

# less than
3 < 5

# less than or equal to
3 <= 5

"""This is because the way input works behind the scenes is it always assumes what you are typing is text (or a string) and gets stored as a variable in "".

Casting is where we explicitly tell the computer that what we are typing is a number and not a letter.

There are two types of numbers the computer will recognize:
int whole number (ex: 42)
float any number with a decimal (ex: 1.81)"""

myScore = int(input("Your score: "))
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")

  myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")

  score = int(input("What was your score on the test?"))
if score >= 80:
    print("Not too shabby")
elif score > 70:
    print("Acceptable.")
else:
    print("Dude, you need to study more!")

#👉 Day 9 Challenge

"""What generation are you a part of?

Use this list to guide you.

Generation Name         Starting Birth Year     Ending Birth Year
Lost generation         1883                    1900
Greatest generation     1901                    1927
Traditionalists         1928                    1945      //Silent generation
Baby Boomers            1946                    1964
Generation X            1965                    1980
Millenials              1981                    1996
Generation Z            1997                    2012
Generation Alpha        2012                    Present

Have a user type in the year they were born.
"""
print("What generation are you a part of?")


birthYear = int(input("What year were you born?"))
if birthYear <= 1946:
  print("You are a Traditionalist.")
elif birthYear >= 1947 and birthYear <= 1964:
  print("Hey, Baby Boomer! How you doing?")
elif birthYear >= 1965 and birthYear <= 1981:
  print("Gen X! What's up?")
elif birthYear >= 1982 and birthYear <= 1995:
  print("Millenials! The age of tech!")
elif birthYear >= 1996:
  print("Hey, Gen Z! TikTok much?")
else: 
  print("Try again!")
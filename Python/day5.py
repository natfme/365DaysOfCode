#Day Five - If this...else that?!

"""You are telling the computer: if something is true, then do this specific block of code. Double equals (==) is asking the computer to compare if these two things are exactly the same."""

myName = input("What's your name?: ")
if myName == "David":
 print("Welcome Dude!")
 print("You're just the baldest dude I've ever seen")
else:
 print("Who on earth are you?!")

catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat":
  print("Meow")
else:
  print("Woof")

#Day 5 Challenge
#*********************************
# Marvel Movie Character Creator
#*********************************

print("Which character are you from 'Avengers?'")
print()
print("Answer these questions and let's find out.")
print()
print("Please use Y or N for yes and no.")

likeGreen = input("Do you like the color green?: ")
if likeGreen == "Y":
  print("You must be the Hulk!")

IronIsCool = input("Do you think building robots is cool?: ")  
if IronIsCool == "Y":
  print("You must be Iron Man. Cool suit!")

TimeTravel = input("Do you like traveling through time?: ")  
if TimeTravel == "Y":
  print("You must be Captain America!")

Strong = input("Are you super strong?: ")
if Strong == "Y":
  print("You have got to be Thor!")
else:
  print("I guess you are not like anyone from 'Avengers.'")

optionSpider = input("Do you like 'hanging around'?: ")
if optionSpider == "N":
  print("Then you're not Spider-man")

optionKorg = input("Do you have a 'gravelly' voice?: ")
if optionKorg == "N":
    print("Aww, then you're not Korg")

optionMarvelous = input("Do you often feel 'Marvelous'?: ")
if optionMarvelous == "Y":
  print("Aha! You're Captain Marvel! Hi!")
else:
  print("You\'re a special person")
"""********************************************************************
* Day 3 - Concatenate
*
*Concatenar
*You can combine as many things as you want in any order you want, as long as they're separated by that comma!
*********************************************************************"""
number = input("Give me a number: ")
group = input("Give me a collective noun for a group of things: ")
thing = input("Give me the name of a weird or wacky thing: ")
print("No I don't think that", number, "is a", group, "of", thing,". That's just odd.")

yourName = input("Name: ")
whatYear = input("What year is it?: ")
print(yourName, "thinks it is", whatYear)

#------------------------
print("=== Your Song Generator ===")
print("""You\'ll be asked a bunch of questions
then we\'ll make you up an amazing
song, totally copyright free 😭""")
print()
person = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your person\'s name: ")
print()
print("There was a person called", person)
print("Who did something cool like", thing, "at the wonderful", place, "where you\'ll find me", rhyme)


#---Day3 Challenge
"""1. Create these as a variable:
A type of food
A type of plant
A method of cooking
A word to describe burned food
A household item
2. Output a nice looking Recipe page that *concatenates* a dish in this format:
cooking food with burned plant on a bed of item"""


#example
"""Name a food > Mac & Cheese
Name a type of plant > Cactus
Name a method of cooking > Saute        
What word describes burned food? > Ruined
Name a DIY item > Hammer

MENU
Saute Mac & Cheese with Ruined Cactus on a bed of Hammers
"""

nameFood = input("Name a food: ")
namePlant = input("Name a type of plant: ")
methodCook = input("Name a method of cooking: ")
wordFood = input("What word describe burned food: ")
nameDIY = input("Name a DIY item: ")

print("MENU")
print(methodCook,nameFood,"with",wordFood,namePlant,"on a bed of",nameDIY+"s")

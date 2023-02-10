# Day27 - Video Game Characters

#Project Day! Build some characters and create their health and strength stats through the power of return, libraries, and loops. Get them ready to battle on Day 28.

""" 👉 Day 27 Challenge
Welcome to your first video game creation. You will create a video game that creates a character's health and attack stats...along with an epic name for your character.

Do not delete today's code. You will be building upon it on Day 28.

* Write a subroutine that generates a character: first name and character type (human, imp, wizard, elf, etc.).
* Write a subroutine that multiplies a bunch of random dice rolls together to generate the character's health stats. Use this formula:

(6-sided-roll * 12-sided-roll)/2 + 10

* Write a second subroutine that multiplies a bunch of random dice rolls together to generate the character's strength stats. Use this formula:

(6-sided-roll * 12-sided-roll)/2 + 12

* Present the data in a menu with time.sleep and os.system("clear") to make it appealing.
* Wrap it in a loop so the user has the option to create another character.
Example:

Character Builder

Name Your Legend:
Sheila the Almighty

Character Type (Human, Elf, Wiard, Orc):
Human

Sheila the Almighty
HEALTH: 40
STRENGTH: 26

May your name go down in Legend...

Hints:

* Import libraries first. You will need to use all three libraries you have learned so far.
* You will need four subroutines: character name and type, to create a random sided dice, for the formula to generate health, and for the formula to generate strength. You will return each subroutine.
* Create a while loop that allows the player to choose to play again, clears the code, and pauses it when needed (think about your libraries).
"""

import os, time, random

def character_leg():
    x = random.randint(0,9)
    y = random.randint(0,9)
    list_name = ["Kassandra", "Ratchet", "Dorian", "Alduin", "Goth", "Steve","Ralph", "Chloe", "Vakarian", "Nook"]
    list_last_name = ["The Windrunner", "The Unchained", "The Predactor", "The Constructor", "The Captain", "The Spider","The Fischer", "The Big Daddy", "The Little Sister", "The Baby"]
    print("Name your legend: ")
    print(f"{list_name[x]} {list_last_name[y]}")
    list_character = ["Human", "Elf", "Wizzard", "Ord", "Wolf", "Dwarf", "Vamp"]
    n = random.randint(0, 6)
    print()
    print("Character type (Human, Elf, Wizzard, Ord, Wolf, Dwarf, Vamp): ")
    character = print(list_character[n])

    six_sided_roll = random.randint(1, 6)
    twelve_sided_roll = random.randint(1, 12)
    health = (six_sided_roll * twelve_sided_roll)/2 + 10
    strength = (six_sided_roll * twelve_sided_roll)/2 + 10
    print()
    print(f"Health: {health}")
    print(f"Strength: {strength}")
    print()
    print("May your name go downin Legend")

    print("Again?: ")
    play_again = input().lower()

    while True:
        if play_again == "yes":
            return
        elif play_again == "no":
            break
        else:
            continue

while True:
    os.system("clear")
    print("🎮 CHARACTER BUILDER 🎮")
    time.sleep(1)
    print("Press yes to Play")
    time.sleep(1)
    print("Press no to Exit")
    time.sleep(1)
    print("Press anything else to see the menu again")

    play = input()
    if play == "yes":
        character_leg()
    elif play == "no":
        break
    else:
        continue

#Solution (No peeking!)

import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat

while True:
  print("⚔️ CHARACTER BUILDER ⚔️")
  print()
  name = input("Name your Legend:\n")
  type = input("Character Type (Human, Elf, Wizard, Orc):\n")
  print()
  print(name)
  print("HEALTH:", health())
  print("STRENGTH:", strength())
  print()
  print("May your name go down in Legend…")
  print()
  again = input("Again?:\n")
  if again=="No" or again=="no":
    break
  time.sleep(1)
  os.system("clear")
# Day 28 - Epic Character Battle

# Project Day! Your characters you built on Day 27 will fight to the death. Who will win out?

""" 👉 Day 28 Challenge
Use Day 27's character generator for this project...to build an automated game battle system!

Add return functions to your character's health and strength statuses from Day 27's project.
Generate two different characters and store their data (health and strength stats, character type, name, etc.).
Use a while True loop to simulate those two characters battling.
Roll one six-sided dice for both characters. The character who rolls the higher amount wins that round.
The winner of that round (the one who rolled the higher number) will give damage to the other character by doing the following:
Find the difference between the strength of both opponents and add one.
Take that amount away from the loser's health.
At the end of each round, check the stats of each character to ensure neither of them have died yet.
When one character dies (they run out of health), declare a winner of the battle!
To keep this battle from looking hideous between rounds use time.sleep to pause between rounds os.system("clear") to ensure the screen clears between battles.
Extra points for the use of emojis, colors, or even sound code!

Example:

⚔️ BATTLE TIME ⚔️

Name your Legend:
Arthur the Magnificent
Character Type (Human, Elf, Wizard, Orc): 
Elf

Arthur the Magnificent
HEALTH: 13
STRENGTH: 18

Who are they battling?

Name your Legend:
Sheila the Almighty
Character Type (Human, Elf, Wizard, Orc): 
Human

Sheila the Almighty
HEALTH: 40
STRENGTH: 26

*clear screen here*

⚔️ BATTLE TIME ⚔️

The battle begins!

Arthur wins the first blow
Sheila takes a hit, with 8 damage

Arthur the Magnificent
HEALTH: 13

Sheila the Almighty
HEALTH: 32

And they're both standing for the next round!

*clear screen here*

⚔️ BATTLE TIME ⚔️

The battle continues!

Sheila wins round 2
Arthur takes a hit, with 8 damage

Arthur the Magnificent
HEALTH: 5

Sheila the Almighty
HEALTH: 32

And they're both standing for the next round!

*clear screen here*

⚔️ BATTLE TIME ⚔️

The battle continues!

Sheila wins round 3
Arthur takes a hit, with 8 damage

Arthur the Magnificent
HEALTH: -3

Sheila the Almighty
HEALTH: 32

Oh no Arthur the Mighty has died!

Sheila the Almighty destroyed Arthur the Magnificent in 3 rounds!

Hints:

Start with the code you created from Day 27.
Keep the same subroutines as Day 27 and add one more subroutine about character damage (how a winner is declared in each round).
Tweak the while loop from Day 27 to introduce the first character and their stats followed by the character they will battle and that character's stats. (You will want to include pausing and clearing of the code as you did on Day 27).
Create a counter (within the loop) to keep track of the winner for each round.
Create another while loop inside the current while loop with if statements, pausing, and clearing of code to show what happens if character 1 wins, the characters tie, etc.
Make sure you give a recap of the health each character has left after each round.
"""

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


print("⚔️ BATTLE TIME ⚔️")
print()
c1Name = input("Name your Legend:\n")
c1Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c1Name)
c1Health = health()
c1Strength = strength()
print("HEALTH:", c1Health)
print("STRENGTH:", c1Strength)
print()
print("Who are they battling?")
print()

c2Name = input("Name your Legend:\n")
c2Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c2Name)
c2Health = health()
c2Strength = strength()
print("HEALTH:", c2Health)
print("STRENGTH:", c2Strength)
print()

round = 1
winner = None

while True:
  time.sleep(1)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")

  c1Dice = rollDice(6)
  c2Dice = rollDice(6)

  difference = abs(c1Strength - c2Strength) + 1

  if c1Dice > c2Dice:
    c2Health -= difference
    if round==1:
      print(c1Name, "wins the first blow")
    else:
      print(c1Name, "wins round", round)
  elif c2Dice > c1Dice:
    c1Health -= difference
    if round==1:
      print(c2Name, "wins the first blow")
    else:
      print(c2Name, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)

  print()
  print(c1Name)
  print("HEALTH:", c1Health)
  print()
  print(c2Name)
  print("HEALTH:", c2Health)
  print()

  if c1Health<=0:
    print(c1Name, "has died!")
    winner = c2Name
    break
  elif c2Health<=0:
    print(c2Name, "has died!")
    winner = c1Name
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    

time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")
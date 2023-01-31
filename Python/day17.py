# Day 17 - Let's Cheat Continue

#Learn the `continue` command. An ideal component of building games AND build your first game that keeps score!

"""
Another Cheat
So far we've used break in the while True loop. break leaves the loop completely and runs the next unindented line of code. However, you may want to stop the code and start the loop from the top again. (This is ideal for building games!)

In the code below, the game runs and the user is asked if they want to go left or right. If the user chooses left, they fall to their death, and break will kick the user out of the loop. That's the game.

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
    
Well that's a bit lame and not any different than what we learned in day 16...now for the cheat.

The Continue Command
The continue command stops executing code in the loop and starts at the top of the loop again. Essentially, we want to kick the user back to the original question.

Adding continue will start the code from the start and ask the first question again: "Do you go left or right?".

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")

The else statement refers to any input besides left or right (up or esc). Since the user is a winner, we do not want to use break or it would say they have failed.

So how do we make it stop?

Proceed to the Nearest Exit
The previous code continues to loop even after the user has won. Let's fix that with the exit() command
The exit() command completely stops the program and it will not run any more lines of code.

👉 Copy all the code and try it out. Does it do what you expected?

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")
"""

# 👉 What is wrong here?
"""
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")
"""

# Fix My Code
# 👉 Try and fix this code which is full of errors.

"""
print("Let's play chutes and ladders. Pick ladder or chute.")
while True:
   print("Do you want to go up the ladder or down the chute?")
   direction = input("> ")
   if direction == "chute":
       print("Game over!")
       break
   elif direction == "ladder":
       continue
   else:
        print("Game over!")
        exit()
print("Thanks for playing!")
"""

# 👉 Day 17 Challenge

"""
Go find your Rock, Paper, Scissors game from Day 14 and add the code here before you start. We are going to build upon this game.

Use a loop to repeat the game multiple rounds.
Keep score of player 1 and player 2.
End the game when a player wins three rounds using break and exit.
Use continue to restart the round until one player wins three rounds.
Your last bit of code should be the results of which player won.

Hints

Create a counting system using a variable and += to keep track of the winner for each round.
The while loop needs to be at the start of the game.
Make sure you include print statements saying each player's final score at the end.
Create an if statement to end the loop.

You have created your first game involving scoring. Well done!
"""

from getpass import getpass as input

counter = 1 # Contador de rondas
counterP1 = 0 # Contador jugador 1
counterP2 = 0 # Contador jugador 2

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()

while True:
  print()
  print(f"Round {counter}")
  print()
  print("Select your move (R, P or S)")
  print()
  player1Move = input("Player 1 > ")
  player1Move = player1Move.upper()
  print()
  player2Move = input("Player 2 > ")
  player2Move = player2Move.upper()
  print()
  
  if player1Move=="R":
    if player2Move=="R":
        print("You both picked Rock, draw!")
    elif player2Move=="S":
        print("Player1 smashed Player2's Scissors into dust with their Rock!")
        counterP1 += 1
    elif player2Move=="P":
        print("Player1's Rock is smothered by Player2's Paper!")
        counterP2 += 1
    else:
        print("Invalid Move Player 2!")

  elif player1Move=="P":
    if player2Move=="R":
        print("Player2's Rock is smothered by Player1's Paper!")
        counterP1 += 1
    elif player2Move=="S":
        print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
        counterP2 += 1
    elif player2Move=="P":
        print("Two bits of paper flap at each other. Dissapointing. Draw.")
    else:
        print("Invalid Move Player 2!")

  elif player1Move=="S":
    if player2Move=="R":
        print("Player 2's Rock makes metal-dust out of Player1's Scissors")
        counterP2 += 1
    elif player2Move=="S":
        print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif player2Move=="P":
        print("Player1's Scissors make confetti out of Player2's paper!")
        counterP1 += 1
    else:
        print("Invalid Move Player 2!")
  else:
    print("Invalid Move Player 1!")
    
  continuar = input("Do you play again?")
  continuar = continuar.lower()
  if continuar == "yes":
    counter += 1
    continue
  elif continuar == "no":
    if counterP1 > counterP2:
       print(f"Player 1 wins with {counterP1} victories!")
    elif counterP2 > counterP1:
       print(f"Player 2 wins with {counterP2} victories!")
    else:
       print("Player 1 and Player 2 have tied!")
    print("Bye!")
    break
  else:
     print("Write yes or no. Do you play again?: ")

#------------------------------------------------------
from getpass import getpass as input


print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()
#hint: create these variables outside loop and then add += with correct player to keep score throughout
player1_score = 0
player2_score = 0
#hint: that the while loop needs to go around all code and then highlight the rest of the code and hit tab once. 
while True: 
  player1Move = input("Player 1 > ")
  print()
  player2Move = input("Player 2 > ")
  print()
  
  if(player1Move=="R"):
    if(player2Move=="R"):
      print("You both picked Rock, draw!")
    elif(player2Move=="S"):
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
      player1_score += 1
    elif(player2Move=="P"):
      print("Player1's Rock is smothered by Player2's Paper!")
      player2_score += 1
  elif(player1Move=="P"):
    if(player2Move=="R"):
      print("Player2's Rock is smothered by Player1's Paper!")
      player1_score += 1
    elif(player2Move=="S"):
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
      player2_score += 1
    elif(player2Move=="P"):
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
  elif(player1Move=="S"):
    if(player2Move=="R"):
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
      player2_score += 1
    elif(player2Move=="S"):
      print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif(player2Move=="P"):
      print("Player1's Scissors make confetti out of Player2's paper!")
      player1_score += 1
  
# hint: make sure you add player scores at the end of all the options but still inside the while loop.
  print("Player 1 has", player1_score, "wins.")
  print("Player 2 has", player2_score, "wins.")

  if player1_score==3 or player2_score==3:
    print("Thanks for playing!")
    exit()
  else:
    continue
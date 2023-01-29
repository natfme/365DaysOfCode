# Rock, Paper, Scissors

# Day 14! Now for the most epic of projects...a rock, paper, scissors game to share with the community.

""" 2 player

Are you ready for your first BIG project?!!

So far you have learned

-input and output,
-if/elif/else statements,
-basic mathematics,
-and casting as float and int.

WOW! That's a lot in just 13 days.

Today, you are going to build a rock, paper, scissors game.

Start with this code below to ensure that whenever you use input, each player cannot see what the other player typed in 😉:

    from getpass import getpass as input

1. For this version, you have two players. Player 1 and Player 2.
2. You will need to create if statements (and probably nesting) to decide who has won, lost or if the game is a tie.
3. Make it fun and add emojis or epic comments as your players battle it out.
4. Keep it simple for you. Don't expect the user to type in the words rock, paper, scissors. Instead, encourage them to use R, P, or S. (Can you ensure the user can still input an option even if it is typed in wrong?)

Happy Coding! """

from getpass import getpass as input

print("Rock, paper, scissors game")
print()
player1 = input("Player 1: Choose rock 🥌, paper 📄, scissors ✂, please use R (Rock), P (paper), or S (scissors): ")
player2 = input("Player 2: Choose rock 🥌, paper 📄, scissors ✂, please use R (Rock), P (paper), or S (scissors): ")
print()
print("Epic 🥌 📄 ✂")
player1 = player1.upper()
player2 = player2.upper()

#Combate
def combate(player1, player2):

    if player1 == 'R':
        print("Player 1: Rock 🥌")
    elif player1 == 'P':
        print("Player 1: Paper 📄")
    elif player1 == 's':
        print("Player 1: Scissors ✂")
    else:
        print("Player 1, please try again")
        

    if player2 == 'R':
        print("Player 2: Rock 🥌")
    elif player2 == 'P':
        print("Player 2: Paper 📄")
    elif player2 == 'S':
        print("Player 2: Scissors ✂")
    else:
        print("Player 2, please try again")
        
    if player1 == 'R' and player2 == 'R':
        print("Tie 😁😁")
    elif player1 == 'P' and player2 == 'P':
        print("Tie 😁😁")
    elif player1 == 'S' and player2 == 'S':
        print("Tie 😁😁")
    elif player1 == 'R' and player2 == 'P':  # usuario elegio Piedra, máquina eligió Papel
        print("Player 2 win 🥳, player 1 lost ☹️, try again!")
    elif player1 == 'P' and player2 == 'R': # usuario elegio Papel, máquina eligió Piedra
        print("Player 1 win 🥳, player 2 lost ☹️, try again!")
    elif player1 == 'S' and player2 == 'R': # usuario elegio Tijeras, máquina eligió Piedra
        print("Player 2 win 🥳, player 1 lost ☹️, try again!")
    elif player1 == 'R' and player2 == 'S': # usuario elegio Piedra, máquina eligió Tijeras
        print("Player 1 win 🥳, player 2 lost ☹️, try again!")
    elif player1 == 'P' and player2 == 'S': # usuario elegio Papel, máquina eligió Tijeras
        print("Player 2 win 🥳, player 1 lost ☹️, try again!")
    elif player1 == 'S' and player2 == 'R': # usuario elegio Tijeras, máquina eligió Papel
        print("Player 1 win 🥳, player 2 lost ☹️, try again!")
    else:
        print("Try again")

combate(player1, player2)
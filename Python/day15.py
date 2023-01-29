# All About the Loop

# Make your games much more epic by adding a loop to repeat the game over and over...

""" counter = 0
while counter <= 100:
  print(counter)
  counter +=1

exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ") """

# Fix My Code
# 👉 Try and fix this code which is full of errors.

"""
counter = 0
while counter < 25:
  print(counter)

counter = 0
while counter >= 12:
  print(counter)
  counter += 1

exit = ""
while exit = "yes":
  print("🥳")
exit = input("Exit?: ") 
"""

# 👉 Day 15 Challenge

"""
Write a program that loops. Inside the loop, ask the user what animal sound they want to hear.

Example
What animal do you want?: Cow
A cow goes moo.

Do you want to exit?: no

What animal do you want?: A Lesser Spotted lemur
Ummm...the Lesser Spotter Lemur goes awooga.

Do you want to exit?: yes
"""

print("Welcome to animal sounds")

start = input("Do you start?: please write yes or no ")
while start == "yes":
    animal = input("What animal do you want to hear 🐮🐱🐶🐎🐑🐐🐒🐴🐥🐓🦜🦉🦆🪰🦟🦗🐸🦁🐯🐝?: ")
    animal = animal.lower()
    if animal == "cow":
        print("🐮 A cow goes moo.")
    elif animal == "cat":
        print("🐱 A cat goes meow.")
    elif animal == "dog":
        print("🐶 A dog goes woof.")
    elif animal == "horse":
        print("🐎 A horse goes neigh.")
    elif animal == "goat":
        print("🐐 A goat goes baa.")
    elif animal == "sheep":
        print("🐑 A sheep goes baa.")
    elif animal == "monkey":
        print("🐒 A monkey goes Hhuo-huooo-hoooo.")
    elif animal == "donkey":
        print("🐴 A donkey goes hee haw.")
    elif animal == "chicken":
        print("🐥 A chicken goes cluck.")
    elif animal == "rooster":
        print("🐓 A rooster goes cock-a-doodle-do.")
    elif animal == "bird":
        print("🦜 A bird goes chirp.")
    elif animal == "owl":
        print("🦉 An owl goes hoot.")
    elif animal == "duck":
        print("🦆 A duck goes moo.")
    elif animal == "mosquitoes":
        print("🦟 A mosquitoes goes buzz.")
    elif animal == "cricket":
        print("🦗 A cricket goes chirp.")
    elif animal == "frog":
        print("🐸 A frog goes ribbit.")
    elif animal == "lion":
        print("🦁 A lion goes roar.")
    elif animal == "tiger":
        print("🐯 A tiger goes roar.")
    elif animal == "bee":
        print("🐝 A bee goes buzz.")
    else:
        print(f"I don't know how to hear {animal}")
    continueGame = input("Do you continue?: ")
    start = continueGame
print("Thanks, see you later")



exit = "no"


while exit == "no":
  animal_sound = input("What animal sound do you want to hear?")
  
  if animal_sound == "cow" or animal_sound == "Cow":
    print("🐮 Moo")
  elif animal_sound == "pig" or animal_sound == "Pig":
    print ("🐷 Oink")
  elif animal_sound == "sheep" or animal_sound == "Sheep":
    print ("🐑 Baaa")
  elif animal_sound == "duck" or animal_sound == "Duck":
    print("🦆 Quack")
  elif animal_sound == "dog" or animal_sound == "Dog":
    print("🐶 Woof")
  elif animal_sound == "cat" or animal_sound == "Cat":
    print("🐱 Meow")
  else: 
    print("I don't know that animal sound. Try again.")


  exit = input("Do you want to exit?: ")



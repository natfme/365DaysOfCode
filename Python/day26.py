# Day26 - The Power of Libraries in Games

"""
You are 1/4th of the way done with 100 Days of Code! Well done. Learn how to import two libraries: 'os' and 'time', which will be super helpful as you start to build some really cool automation.

os Library
What is the os library?

It allows us to "talk" to the console. One of the most powerful things we can do with this library is allow it to clear the console.

Import the os library
👉 Well, this just prints a list of numbers to 1,000...

import os
for i in range(1,1000):
  print(i)

Adding os.system
We can clear the code above by using the os.system function to 'clear' the console.

👉 Add this to the code above: (remember to indent this properly)

os.system("clear")

import os
for i in range(1, 1000):
  print(i)
  os.system("clear")

Do you notice how it clears the console? Cool, right?!

Let's try one more...
👉 For this code, I want the program to say "Welcome to Replit!", delete that, and then ask for my username on a blank screen. Remove the previous code, add the code below and see what happens when you hit run!

import os
print("Welcome")
print("to")
print("Replit")

os.system("clear")

username = input("Username: ")

Wow! The console printed and cleared 'Welcome to Replit!' before I even had a chance to read it.

Let's fix that with another library.

Time Library
We can import a second library by placing a , after the name of the first library.

👉 Let's add a second library, time.

import os, time

This library allows us to pause the execution of a program for a specific amount of time.

The time.sleep(1) function allows us to pause the program for the amount of seconds listed in the ().

👉 Add this to your code before the program is cleared to pause the program for 1 second before displaying the username.

time.sleep(1)
os.system("clear")

Try it out with other amounts of time and see what happens.

import os, time

print("Welcome")
print("to")
print("Replit")

time.sleep(1)
os.system("clear")

username = input("Username: ")
"""

# 👉 Day 26 Challenge

"""
Play a song from this repl and build a menu to go with it. Make it look like an iPod!

Use a while true loop to create a title for a music player.
Allow the user to select to play a song and use subroutine called 'play' when they select the song.
Give the user the option to exit the program.
The title should pop up and pause along with the menu options.
If the user chooses anything else, start again by clearing the screen.
Use this code to get started:

from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    input()

while True:
  # clear the screen 

  # Show the menu

  # take user's input

  # check whether you should call the play() subroutine depending on user's input

Here is an example:

🎵 MyPOD Music Player

Press 1 to Play
Press 2 to Exit

Press anything else to see the menu again.

Hints:
* Import your libraries first.
* With the sample code above, think about what code can be added to pause and play the audio.
* What command do you need to use to return (hint, hint) to the main menu (subroutine)?
* Create a while True loop that clears the code and pauses the code. What libraries would you need for these things to happen?
* You may also need if statements within your loop.

---------------------------------------------------------------

from replit import audio
import os, time


def play():
  source = audio.play_file('audio.wav')
  source.paused = False  # unpause the playback

  while True:
    # Start taking user input and doing something with it
    stop_playback = int(
      input("Press 2 anytime to stop playback and go back to the menu : ")
    )  # giving the user the option to stop playback

    if stop_playback == 2:
      source.paused = True  # Pausa la reproducción
      return # let's go back from this play() subroutine
    else:
      continue

while True:
  # clear the screen
  os.system("clear")
  print("🎵 Mi cajita de música_")

  # Show the menu
  time.sleep(1)
  print("write 1 to play")
  time.sleep(1)
  print("write 2 to exit")
  time.sleep(1)
  print("Press anything else to see the menu again")

  userInput = int(input())

  # take user's input
  if userInput == 1:
    # check whether you should call the play() subroutine depending on user's input
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else:
    continue

-------------------------------------------------------------

from replit import audio

import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : ")) # giving the user the option to stop playback
    if stop_playback == 2:
      source.paused = True # let's pause the file 
      return # let's go back from this play() subroutine
    else: 
      continue
  
while True:
  os.system("clear")
  print("🎵 MyPOD Music Player ")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else :
    continue
    
"""
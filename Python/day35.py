# Day35 - The ULTIMATE List Maker

# Beef up your to do list from Day 33 to make the ULTIMATE list maker by adding 'pretty printing' subroutines.

# 👉 Day 35 Challenge

""" Build a really cool to do list manager. (I know we did this before...hold on!)

We are going to upgrade the last to do list manager we created:

Create a menu where the user can view, add, or remove an item.
The user should be able to edit the text of an item on the list too.
Don't allow the user to add duplicates.
Double check with the user they want to remove an item from the list before it is actually removed. (Is this the item they really want to remove?)
Give the user the option to completely erase the to do list. (You should be able to do this in one line of code!)
Example:

To Do List Manager:

Do you want to view, add, edit, or remove an item from the to do list?
view

record the video for day 36

Do you want to view, add, edit, or remove an item from the to do list?
remove

What do you want to remove?
record the video for day 36

Are you sure you want to remove this?
yes

👉 Hints:

You should be able to use all the code from Day 33 to get started. The biggest additions will be related to the menu options for edit and remove.
Use a nested if statement to verify if the user wants to remove something. """

import os, time
toDoList = []

def printList():
  print()
  for items in toDoList:
    print(items)
  print()

while True:
  menu = input("To Do List Manager xD\nDo you want to view, add, edit, remove, delete the to do list or exit?\n")
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n").title()
    toDoList.append(item)
  elif menu=="remove":
    item = input("What do you want to remove?\n").title()
    check = input("Are you sure you want to remove this?\n")
    if check[0]=="y":
      if item in toDoList:
        toDoList.remove(item)
  elif menu=="edit":
    item = input("What do you want to edit?\n").title()
    new = input("What do you want to change it to?\n").title()
    for i in range(0,len(toDoList)):
      if toDoList[i]==item:
        toDoList[i]=new
  elif menu=="delete":
    toDoList = []
  elif menu == "exit":
    print("Bye!")
    break
time.sleep(2)
os.system('clear')






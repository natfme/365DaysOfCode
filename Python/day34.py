# Day34 - Pretty Printing

# Let's be honest...so far all your subroutines have been pretty boring. Now let's make them, well, pretty.

""" Pretty print Functions
Let's build a pretty print subroutine! So far all the subrouintes you have made have been pretty boring...just saying.

When we have a list of data, being able to print out that data in pretty ways is something we need to be able to do. So "pretty printing" is actually a thing.

👉 I have created a program called "Spammer Inc." to spam emails (obviously this is not something you would actually do). If the user presses 1, they can add an email, and pressing 2 allows them to remove an email. (Hint: This should all look familiar so far). """

import os, time
listOfEmail = []

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  time.sleep(1)
  os.system("clear")

#👉 What we have not done yet is print this out. Let's add a pretty print function. (Everything else in this code will stay the same).

import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") # start by clearing the screen
  print("listofEmail") # print the title of my program
  print() # print a blank line
  for email in listOfEmail: # use for loop to access list
    print(email)
  time.sleep(1)

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
    prettyPrint()  
  time.sleep(1)
  os.system("clear")

""" Play around with your creation. Do you see what we did to make it 'pretty'?

-------------------------------------------------------------------------
Creating a Numbered List

👉 I can also ensure my list prints as a numbered list. Let's make this happen by making these few changes below to our subroutine. This code snippet only shows the subroutine so we can focus on the changes there: """

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  counter = 1 # add a counter
  for email in listOfEmail: 
    print(f"{counter}: {email}") # make this an f-string
    counter += 1 # adds a number with each new email
  time.sleep(1)

#👉 We still need to call the subroutine. Let's edit our while loop a bit.

import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  counter = 1 
  for email in listOfEmail: 
    print(f"{counter}: {email}") 
    counter += 1 
  time.sleep(1)
  
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3": # we added this elif
    prettyPrint() # called our subroutine here
  time.sleep(1)
  os.system("clear")

""" Can you add some color? Write your own pretty print function. Make it a numbered list, too.

--------------------------------------------------------------------------
Using the Index
We can also use loops in a slightly different way to access elements in a list (or array). With the way we have our code written right now, our list creates a variable called email, sets it equal to the first value (with our counter we set 1 as the first value), and then counts on as we go. (2, 3, 4, etc.)

However, we can also set the for loop to use the index. What should happen is index will start at 0, go through the entire code in the loop at 0, go back to the start of the loop, add 1, and then loop again and again until the list ends.....

👉 Let's tweek the for loop in our subroutine just a bit to accomplish this: """

import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)): # len counts how many items in a list
    print(f"{index}: {listOfEmail[index]}") 
  time.sleep(1)


while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  time.sleep(1)
  os.system("clear")

""" len counts how many items are in a list. In this case, it is starting at 0 and then keeps going until it reaches the end of our data inside our list. We can now eliminate the counter variable because we are counting with index.

We do need to access email in a different way now. We are going to use the actual list name itself and then [index] to access the index. """

#------------------

import os, time
listOfEmail = []

for index in range(len(listOfEmail)): 
    print(f"{index}: {listOfEmail[index]}") 
    counter += 1 
time.sleep(1)

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in len(listOfEmail): 
    print(f"{index}: {listOfEmail[Index]}") 
    counter += 1 
  time.sleep(1)


while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  time.sleep(1)
  os.system("clear")

# ------------------------------------------------------------S
import os, time
listOfFood = []

def prettyPrint():
  os.system("clear") 
  print("listofFood") 
  print()
  counter = 1 
  for order in listOfFood: 
    print(f"{counter}: {order}") 
    counter += 1 
  time.sleep(1)
while True:
  print("Yummy Food Restaurant")
  menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
  if menu == "1":
    order = input("order > ")
    listOfFood.append(order)
  elif menu =="2":
    order = input ("delete order> ")
    if order in listOfFood:
      listOfFood.remove(order)
  elif menu == "3": 
    prettyPrint() 
  time.sleep(1)
  os.system("clear")

# 👉 Day 34 Challenge
"""Let's extend this program and build option 4: "Get SPAMMING".

Print out the first 10 email addresses with a custom email sent to each of those people.
Print one email at a time, pause, and then clear the screen before the next email is printed.
Example:

Dear john@test.com
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
Ian Spammington III

Hints:

Use the same libraries, list, and subroutine we just created.
Create a second subroutine relating to spam. In the for loop, we want to spam everyone. What would the range look like?
Write the email copy that will get sent to the email addresses.
Finish with the same while loop we created, but add option 4 (spamming). Make sure you only include 10 emails.
Don't forget to pause and clear the screen each time."""

import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear")
  print("listOfEmail")
  print()
  counter = 1
  for email in listOfEmail:
    print(f"{counter}: {email}")
    counter+=1
  time.sleep(1)

def spam(max):
  for i in range(0,max):
    print(f"""Email {i+1}

Dear {listOfEmail[i]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,

Ian Spammington III""")
    time.sleep(1)
    os.system("clear")
while True:
  print("SPAMMER Inc.")
  menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu== "2":
    email = input("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu =="4":
    spam(10)
  time.sleep(1)
  os.system("clear")
# day40 - Dictionaries

# Don't worry. No need to buy a massive paper book to look up words. Let's take lists one step further with dictionaries.

""" Dictionaries
As you might have guessed, we love lists. However, list items are accessed in order by index number. This isn't always the way we want it to work.

Dictionaries are a slightly different type of list that access data by giving each item a key. This creates what we call key:value pairs.

Now we can access each item through its key, instead of having to remember what index it is at in the list.

Creating a dictionary - brace!
Curly, curly braces...

To create a dictionary we start just like a list, except with curly braces {}. This dictionary will store data about a user.

The data is inserted in key value pairs like this. Each pair is separated by a comma:

dictName = {key name : key value, Next key name : key value }

👉 The first key:value pair below has "name" as the key and "David" as the value. Try it out: 

myUser = {"name": "David", "age": 128}

Printing the keys
To output (print) from a dictionary, we can use the key instead of the index. Note that we still use square brackets for accessing items (ex: ["name"]).

print( dictName[ key name])

👉 Let's print "name". """

myUser = {"name": "David", "age": 128}

print(myUser["name"])

print(myUser["age"])

# This code outputs 'David'.

#-----------------------------------

""" Note that we have to put the keys in single quotation marks '' inside the fString when using this technique.

This is because we've already used double quotes to start and end the fString. So, using "" for the dictionary value would get Python all confuzzled. """

""" myUser = {"name": "David", "age": 128}

print(f"Your name is {myUser['name']} and your age is {myUser['age']}")

# This code outputs 'Your name is David and your age is 128'.

myUser = {"name":"David", "age": 128}

myUser["age"] = 129

print(myUser)

myUser = {"name":"Andy", "age":128}

myUser["age"] = 129

print(myUser["name"]) """

#👉 Day 40 Challenge

""" Today's challenge is to create a contact card using a dictionary.

Ask the user to input their name, date of birth, telephone number, email and physical address.
Store it all in a dictionary.
Print it out in a nice way once its stored.
Example:

🌟Contact Card🌟

Input your name > David Morgan

Input your date of birth > 01/01/1900

Input your telephone number > 01234 567890

Input your email > david@replit.com

Input your address > The Cupboard Under The Stairs, Replit Towers, NY.

Hi David Morgan. Our dictionary says that you were born on 01/01/1900, we can call you on 01234 567890, email david@replit.com, or write to The Cupboard Under The Stairs, Replit Towers, NY. 

Hints:

You may find \""" helpful here.
Don't forget to .strip() out any unwanted spaces.
Pay close attention to when to use [] and when to use {}.
For extra fun, try investigating the .update() method for another way of working with dictionaries.
"""
name = input("Input your name and last name> ")
dateBirth = input("Input your date of birth > ")
phoneNumber = input("Input your telephone number > ")
email = input("Input your email > ")
address = input("Input your address > ")

userContact = {"name" : name, "dateBirth" : dateBirth, "phoneNumber" : phoneNumber, "email" : email, "address" : address}

print("😎 Contact Card 📱")
print()
print(f"Hi {userContact['name']}. Our dictionary says that you were born on {userContact['dateBirth']}, we call you on {userContact['phoneNumber']}, email {userContact['email']}, or write to {userContact['address']}")
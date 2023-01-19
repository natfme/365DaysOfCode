#day 6 - What the elif is this?
#Learn 'elif' statements. Can you create a login system to keep passwords safe from hackers?

""" print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "mark" and password == "password":
 print("Welcome Mark!")
elif username == "suzanne" and password == "Su74nne":
 print("Hey there Suzanne!")
else:
 print("Go away!") """

""" print("You are getting really good at this!")

season = input("what is your favorite season?")
               
if season == "spring":
    print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
    print("Catch some sun and cool off with a lemonade.")
elif season == "autumn":
    print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
    print("Stay warm by the fire and watch the snow fall.")
else:
    print("I don't know that season. Please try again.") """

#👉 Day 6 Challenge
#Make your own login program.

""" Create a program where someone logins with their username and password correctly and then gets a lovely individual greeting.
Write a specific personalized greeting for 3 different people.
Don't forget an else statement for everyone else who shouldn't be logging in. """

print("===============\nMy Login System\n===============")
print("Please, enter your user name and password")
username = input("Username > ")
password = input("Password > ")

def texto (username):
 username = username.capitalize()
 template = f"Why hello there {username}, What a lovely accent you have, you could have charmed your way in here even without a password. \n\nHave a great day. \n\nDon\'t forget to wear a hat in the sun!"
 print(template)

if username == "mark" and password == "marcapaso2":
 print("Welcome Mark!")
 texto(username)
elif username == "suzanne" and password == "Su74nne":
 print("Hey there Suzanne!")
 texto(username)
elif username == "ana" and password == "4nn3tte":
 print("Hello Ana!")
 texto(username)
else:
 print("Go away!")

#other option
print("Secure Login")
username = input("What is your username?")
password = input("What is your password?")

if username == "David" and password == "PyTh0nR*cks":
  print("Welcome, David! You are looking nice today!")
elif username == "Beth" and password == "Repl!t4evEr":
  print("Hi Beth! Love your hair today!")
elif username == "Anna" and password == "SmashTHEb*gs!":
  print("Yo! Anna! What up?!")
else:
  print("You do not have access. Go away!")
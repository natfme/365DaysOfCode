# Day30 - f...what?

# The `f` stands for format...not whatever you were thinking. Change the way you combine strings and variables with f-strings.

""" f-strings

f-strings (format strings) are the best way to combine variables and text together. Everything up until now has been...well...awkward.

👉 Let's look at how we have combined variables and text in the past...concatenating.

👉 Let's now use an f-string for this same code. What changes did I make to this code?

Change 1: Using {} as a placeholder for the variable. Change 2: Adding .format(variable names, commas)

Why is this easier? Let's find out.
"""

name = "Katie"
age = "28"
pronouns = "she/her"

print("This is", name, "using", pronouns, "pronouns and is age", age)

print("-------------------------------------------------------------------------------------------")

name = "Katie"
age = "28"
pronouns = "she/her"

print("This is {}, using {} pronouns, and is {} years old.".format(name, pronouns, age))

print("-------------------------------------------------------------------------------------------")

""" Local Variables

We can set local variables within the f-string itself. Now it doesn't matter the order of the variables.

👉 Looking at this code again, I can set my variables inside the text itself. Watch this:

Change 1: Replace {}with variable names. Change 2: Replace each variable inside {} with what has been defined in format.( = )

f-strings work with different variable types too: int, float, and string.

👉 We can assign concatenated sentences to variables. Watch this. We made a variable called response and made it equal to a concatenated sentence. Now I can use this response easily wherever I want.

Now we have a unique text string. We can't do this with commas.
"""

name = "Katie"
age = "28"
pronouns = "she/her"

print("This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age))

print("-------------------------------------------------------------------------------------------")

name = "Katie"
age = "28"
pronouns = "she/her"

response = "This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age)

print(response)

"""
The Power of f...
Instead of all that faffing about...try this instead.

Use the letter f before any string with {} for variable names (and forget that .format business).

👉 Look at this same code and see the difference using this technique:

You can even use this trick with the \""" triple quote. (Remember, when we learned that on Day 1.)
"""
print("-------------------------------------------------------------------------------------------")

name = "Katie"
age = "28"
pronouns = "she/her"

response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"

print(response)

"""
Alignment

left = <, right = >, center = ^

👉 This program shows how much of 100 Days of Code we have completed so far. I want this to look like a list. However, once we get to day 10, it starts to look a bit messy. Make sure you include f when using alignment.

👉 Let's fix it by adding a left alignment of 2 characters long.

Play around with alignment. What do you think?
"""

for i in range(1, 31):
  print(f"Day {i} of 30")

for i in range(1, 31):
  print(f"Day {i: <2} of 30")

for i in range(1, 31):
  print("Day {count} of 100".format(count=i))

food = "pizza"
location = "beach"
color = "green"
friend = "Quinn"

response = "Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame.".format(food=food, location=location, color=color, friend = friend)

print(response)

"""
👉 Day 30 Challenge
Create a program that uses a loop that asks the user what they have thought of each of the 30 days of challenges so far.

For each day, prompt the user to answer a question and restate it in a full sentence that is center aligned underneath the heading.

Example:

30 Days Down

Day 1: 
Amazing

            You thought Day 1 was amazing.
Day 2:
so good that I bought the David plushie

              You thought Day 2 was so good...

Hints:

Look at the common error for help on the loop.
Create an input statement for the user to express what they thought of that day.
print using an f-string.
Think about what symbol you need for center alignment. How many spaces should you move your statement?
Think about the length of the heading. Maybe that's how many spaces you would need to center align the text.
"""

""" print("#---------------------------------------------------------------------------------------#")

print("30 Days Down - What did you think?")
print()
for i in range(1,31):
  thought = input(f"Day {i}: \n")
  print()
  myText = f"You thought Day {i} was"
  print(f"{myText:^35}")
  print(f"{thought:^35}")
  print() """

""" print("30 Days Down - What did you think?")
print()
for i in range(1, 31):
  thought = input(f"Day {i}:\n")
  print()
  myText = f"You thought Day {i} was"
  print(f"{myText:^35}")
  print(f"{thought:^35}")
  print() """

counter = 5
while counter != 0:
  print("Dentro del bucle.", counter)
  counter -= 1
print("Fuera del bucle.", counter)

print("-----------------------------------------------------------------------")

counter = 5
while counter:
  print("Dentro del bucle.", counter)
  counter -= 1
print("Fuera del bucle.", counter)

for i in range(100):
    # do_something()
    pass

""" La palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto; es una instrucción vacía - la colocamos aquí porque la sintaxis del bucle for exige al menos una instrucción dentro del cuerpo (por cierto - if, elif, else y while expresan lo mismo). """

power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

print("Break and continue")
print()
# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

""" Estas dos instrucciones son:

break - sale del bucle inmediatamente, e incondicionalmente termina la operación del bucle; el programa comienza a ejecutar la instrucción más cercana después del cuerpo del bucle.
continue - se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; el siguiente turno se inicia y la expresión de condición se prueba de inmediato.
Ambas palabras son palabras clave reservadas. """

""" largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

print("-----------------------------------------------------------------------------")

largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
 """
""" print("---------- Escenarios ----------")
print()
print("La sentencia break - atrapado en un bucle")

while True:
    word = input("Escriba una palabra, si desea detener el ciclo escriba \"Detente\": ")
    if word == "Detente":
        break
print("Has dejado el bucle con éxito")

print()
print("La sentencia continue - el Feo Devorador de Vocales")

user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()

for i in user_word:
    if i == "A":
        continue
    elif i == "E":
        continue
    elif i == "I":
        continue
    elif i == "O":
        continue
    elif i == "U":
        continue
    else:
        print(f"{i}")

 # Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.

for letter in user_word:
    # Completa el cuerpo del bucle for.

print()
print("La sentencia continue - el Lindo Devorador de Vocales")

word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.

user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()

for i in user_word:
    if i == "A":
        continue
    elif i == "E":
        continue
    elif i == "I":
        continue
    elif i == "O":
        continue
    elif i == "U":
        continue
    else:
        word_without_vowels += i

print(f"{word_without_vowels}")

#for letter in user_word:
    # Completa el cuerpo del bucle.

# Imprimir la palabra asignada a word_without_vowels. """

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

for i in range(5):
    print(i)
else:
    print("else:", i)

i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
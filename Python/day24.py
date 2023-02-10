# Day24 - Roll in the Parameters

# Underwhelmed by subroutines? Let's switch it up and add some parameters.

""" Parameters

I get it. So far, subroutines have been a bit underwhelming...

Let's put those subroutines to better use by sending them information using parameters and making them do different things based on different inputs.

If you change the ingredients in a recipe, you get a different kind of cake. Let's do that with subroutines.

In a subroutine, the () are for the argument (FYI argument is another word for parameter). These are the pieces of information we pass to the code. These can be variable names that are made up for the first time within the argument ().



Here is a simple subroutine that uses the argument to take in the name of an ingredient and expresses its opinion (quite strongly) about the ingredient that the user typed. For example, 'chocolate' is amazing, but 'broccoli'...not so much.

👉 Try it out.

def whichCake(ingredient):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")

But how do we call it?

----------------------------------------------------------------------------

How do we call the subroutine?

We call it in the same way as before. However, instead of leaving the () blank, we send the code a message.

👉 What happens when you add this to the end of your code above?

whichCake("chocolate")
That's right. The variable 'ingredient' in the subroutine gets set to 'chocolate' and the output shows:

👉 What happens if you change "ingredient" to "broccoli"?

-------------------------------------------------------------------------------------------------------------

Adding More Arguments

We can have as many arguments as we want, separated by commas.

Now, this subroutine is expecting three arguments: ingredient, base, and coating:

def whichCake(ingredient, base, coating)
  
👉 Let's update our code to now show all three arguments:

def whichCake(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
  print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")

whichCake("carrot", "biscuit", "icing")

👉 I could even ask the user to name an ingredient, base, and coating by adding:

def whichCake(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
  print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")

userIngredient = input("Name an ingredient: ")
userBase = input("Name a type of base: ")
userCoating = input("Fave cake topping: ")
whichCake(userIngredient, userBase, userCoating)

What could you input to make a yummy cake?

--------------------------------------------------------------------------------------

def biggerNumber(number1, number2):
  if(number1 > number2):
    print(number1, "is bigger")
  else:
    print(number2, "is bigger")

biggerNumber (18,332)

def pizza_order(topping1, topping2):
  if topping1 == "pepperoni":
    print(topping1, "is a great choice")
  else:
    print(topping1, "is kinda lame on pizza")
  print(topping2, "sounds delicious, much better than", topping1)
  
topping1 =  input("Name a pizza topping. ")
topping2 = input("Name a second pizza topping. ")

pizza_order(topping1, topping2)

-------------------------------------------------------------------------------------------------------

👉 Day 24 Challenge

Let's build an infinity dice!

Create subroutines that will roll a dice with any number of sides (essentially as big of a number as you like). Write one subroutine with one parameter that allows us to call a function (such as rollDice).
Example:

Infinity Dice 🎲

How many sides?: 600
You rolled 532

Roll again? yes
You rolled 102

Roll again? no

Hints:
* Import your library first.
* Create a variable to ask the user how many sides the dice should be.
* Create a variable that allows the user to leave the game.
* Create a subroutine with rollDice that sets the sides of the dice as the argument.
* Create a while loop that allows the user to roll again or leave the game.
"""
""" import random

print("Infinity Dice 🎲")
print()


def dice(num):
    diceNum = random.randint(1, numSides)
    print("You rolled ", diceNum)
    print()

numSides = int(input("How many sides?: "))
dice(numSides)

while True:
    continuar = input("Roll again?: ").lower()

    if continuar == "yes":
        dice(numSides)
    elif continuar == "no":
        break
    else:
        continue
    
#-----------------------------------------------------------

import random
print("Infinity Dice 🎲")
  
sides = int(input("How many sides?: "))
playGame = "yes"
  
def rollDice(sides):
  print("You rolled ", random.randint(1,sides))
while playGame == "yes":
    rollDice(sides)
    playGame = input("Roll again?")

#-------------------------------------------------------------------------------------------------------- """

# 💡 Problema: Ecuaciones de física (Parte I)

""" Podemos calcular este valor a partir de algunos parámetros iniciales que describen el problema. Estos parámetros iniciales son:


La velocidad inicial v0 del objeto en dirección del recorrido.
La posición inicial x0. En este caso el recorrido solo se dará en una dirección de forma horizontal.
La aceleración a que se mantiene constante en todo el recorrido.
El tiempo t o duración del recorrido.

Se conoce que la posición de un objeto uniformemente acelerado puede ser calculada por la siguiente ecuación:

x = x0 + v0*t + (1/2)*a*t^2 

En este ejercicio usted deberá crear un programa que realice lo siguiente:

Obtener de la entrada del programa los parámetros iniciales, línea por línea y en el orden descrito en la sección ⌨️ Entrada.
Convertir cada valor de texto obtenido de la entrada en un valor numérico decimal.
Utilizar los valores numéricos en una expresión matemática y obtener el valor de la posición final.
Reportar el resultado de la operación con el formato numérico descrito en la sección 🖥️ Salida.

------------------------------------------------------------------------------------------

Su programa deberá recibir de la entrada 4 líneas con los valores de x0, v0, a y t respectivamente.

Línea 1: cadena de texto con la posición inicial x0 en m
.
Línea 2: cadena de texto con la velocidad inicial v0 en m/s
.
Línea 3: cadena de texto con la aceleración a en m/s2
.
Línea 4: cadena de texto con el tiempo t en s
.

Tenga en cuenta que cada una de estas líneas es obtenida como cadenas de texto con un formato que puede ser convertido a un valor decimal con la función float. No olvide realizar la conversión del tipo de dato en su programa.


En este ejercicio el programa deberá imprimir exactamente 1 línea con la respuesta del ejercicio. Esta respuesta deberá tener este formato exacto:


'La posición final es {x} metros.'


Donde {x} corresponde a la posición calculada en metros, que deberá ser presentada con un formato que muestre exactamente dos dígitos decimales.

Entrada Ejemplo 1
15
3.2
0
0

Salida Ejemplo 1
La posición final es 15.00 metros.

Entrada Ejemplo 2
21.1
40
0.1
60

Salida Ejemplo 2
La posición final es 2601.10 metros.

Entrada Ejemplo 3
47
6
5e-2
147

Salida Ejemplo 3
La posición final es 1469.22 metros.
"""

##################################################
### 💻  Ejemplo: Ejercicios de física (I)  💻 ###
##################################################

## 👇 Escriba su código DEBAJO de esta línea 👇 ##

# 1) Obtener de la entrada del programa los parámetros iniciales.

# 2) Convertir cada valor de texto obtenido de la entrada en un valor numérico decimal.

x0 = float(input("Ingrese la posición inicial x0 en m: "))
v0 = float(input("Ingrese la velocidad inicial v0 en m/s: "))
a = float(input("Ingrese la aceleración a en m/s2: "))
t = float(input("Ingrese el tiempo t en s: "))

x0 = float(input())
v0 = float(input())
a = float(input())
t = float(input())

# 3) Utilizar los valores numéricos en una expresión matemática y obtener el valor de la posición final.

x = x0 + v0 * t + (1/2) * a * t ** 2

# 4) Reportar el resultado de la operación con dos dígitos decimales.

print(f"La posición final es {x :.2f} metros.")

## ☝️ Escriba su código ENCIMA de esta línea ☝️ ##
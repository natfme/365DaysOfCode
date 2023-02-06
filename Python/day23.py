# Day 23 - 💡 Problema: Dividir en grupos

"""
¿Cuántos grupos completos de x estudiantes pueden armarse en una clase de n estudiantes?
¿Cuántos reportes en total debería recibir del grupo de calificadores?

Su programa deberá recibir de la entrada los parámetros iniciales n y x e imprimir el número con el resultado de ambas preguntas en la salida.

En este ejercicio el programa deberá imprimir exactamente 2 líneas con la respuesta a cada pregunta:


En la primera línea: número total de grupos completos que se deben crear.
En la segunda línea: número total de reportes que se escribirán por parte de los calificadores.

Entrada 1       Salida 1
16              2
6               8

Entrada 2       Salida 2
25              3
7               12

Entrada 3       Salida 3
10              1
8               2
"""

##################################################
####   💻  Práctica: Dividir en grupos  💻  #####
##################################################

## 👇 Escriba su código DEBAJO de esta línea 👇 ##


# Reciba n y x de la entrada con la función 'input'. 
# No olvide convertir las cadenas en números con 'int'.

n = int(input()) # Número de estudiantes
x = int(input()) # Números de grupos

# Calcula el número de grupos de tamaño x que se pueden formar.

num_grupos = n // x

# Calcula el número de estudiantes sobrantes asignados a la calificación.
# (Este número debe ser menor que x)

resto = n % x

# Calcula el número de reportes entregados por los estudiantes.

total_reportes = resto * num_grupos

# Imprime en la salida el número correspondiente para las preguntas del enunciado.
print(num_grupos)
print(total_reportes)

## ☝️ Escriba su código ENCIMA de esta línea ☝️ ##

raiz1 = 4 ** 0.5
raiz2 = 2 ** 0.5

print(f"Raíz de 2: {raiz1:.6f}")  # imprime 6 dígitos decimales
print(f"Raíz de 2: {raiz2:.6f}")

num = 6.5734 * 10 ** 20

print(f"Valor en notación científica: {num: .2e}")

porcentaje = 0.5274645641

print(f"Número en formato de porcentaje: {porcentaje: .6%}")
print(f"Número en formato de porcentaje con 2 dígitos: {porcentaje: .2%}")

# Separador de miles
valor = 7785964164146454
valor1 = 2.456 ** 17

print(f"Número con separador de miles: {valor:,}")
print(f"Número con separador de miles: {valor:_}")
print(f"Número con separador de miles y dígitos decimales (2 dígitos decimales): {valor1:,.2f}")
print(f"Número con separador de miles y notación científica (2 dígitos decimales): {valor1:,.2e}")
print(f"Número con separador de miles y procentaje (2 dígitos decimales): {valor1:,.2%}")

# -------------------------------------------------------------------------------------------------------------------------------------#

# Replit Day 23 - Subroutines: The Recipe for Coding

# Write code in a way where you can use it, call it, or repeat it anywhere and at anytime with the power of subroutines.

"""
Subroutine

So far, when we wanted to repeat code, we have had to use loops or copy and paste code.

What if I told you there was a way to use code or call it and use it anytime anywhere??

That is a subroutine!!

A subroutine tells the computer that a piece of code exists and to go run that code again and again...

Just like a recipe

Subroutines work like a recipe in a cookbook. If you want to know how to make a cake, you don't have to start from scratch every time. You can use a recipe to get the same quality each time.

How do we define a subroutine?
A subroutine is defined by:

def (which stands for definition)
You need to give the subroutine a name (and just like with a variable, you can't have spaces).

You need to add () even if there are no arguments followed by a colon :. The code needs to be indented.

Let's try it ------------------------------------------

👉 Let's roll a random number on a six-sided dice. Copy the code below and click run.

def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)

Why is nothing happening??

In this code, I have defined how to roll a dice (this is my recipe for rolling a dice), but I have not actually 'called' the program to run.


Call the Subroutine
Calling the subroutine means telling it to run.

👉 We need to 'call' the code by adding one more line to our code with the name of the subroutine and the empty ():

def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)

rollDice()

Copied!
Note that when you call the subroutine, you need to ensure you do NOT indent.

I can even add a range and roll the dice 100 times by adding this code:

for i in range(100):
  rollDice()

👉 Try it out for yourself!
"""

# 👉 Day 23 Challenge

"""
1. Create a subroutine with both a username and password.
2. Create a loop to prompt the user again and again until they put in the correct login information.

Replit Login System

What is your username?: david
What is your password? whatAmazingHairYouHave

Whoops! I don't recognize that username or password. Try again!

What is your username? david
What is your password? baldies4life

Welcome to Replit!

Hints:
*Create one login subroutine. Maybe you should call it login.
*Use input and if statements inside a loop.
*Where does the loop need to break? Where does it need to continue?
"""
print("Login system")
print()
nameSave = "Juan"
passwordSave = "Juan1234"

def login_system():
    while True:
        name = input("What is your username?: ")
        password = input("What is your password?: ")

        if name == nameSave and password == passwordSave:
            print(f"Welcome {name}!")
            break
        else:
            print("Whoops! I don't recognize that username or password. Try again!")
            continue

login_system()

# Solution (No Peeking!)

def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password? ")
    if username == "David" and password == "Replit4ev#r":
      print("Welcome David!")
      break
    else:
      print("That is not the correct username or password. Try again!")
      continue
    
print("REPLIT LOGIN SYSTEM")
login()
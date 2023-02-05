# Day20 - Cadenas de texto

a = 'Esta es una cadena con comillas simples'
print(a)

b = "Esta es una cadena con comillas dobles"
print(b)

type("Una cadena de texto")

help('keywords')

ord('a')

chr(64)

cadena = "Python"
cadena = cadena.upper()
cadena = cadena.replace('O', 'OOOOO')

print(cadena)

nombre = input('Ingrese su nombre: ')
print(f'¡Bienvenido {nombre}!')

"""
Esta sintaxis nos ofrece gran flexibilidad en el manejo de cadenas de texto, heredada de lo construido en otros lenguajes de programación. En muchos casos, podemos querer hacer cosas con un texto dado, como alinearlo o darle un formato distinto al que tiene por defecto.

En este tipo de cadenas podemos personalizar el formato de la entrada con **modificadores de formato**, que se indican usando el separador punto y coma **`:`** acompañando un valor. 

<center>
<img src = "https://drive.google.com/uc?export=view&id=1xltZJMXrdAQGObfxmdNR7uE74NgJrRgR" alt = "Cadenas con formato" width = "60%">  </img>
 </center>

Veamos algunos de los modificadores más utilizados:
- **Modificador de relleno:** podemos rellenar con espacios en blanco un fragmento hasta obtener una cadena con **por lo menos** una longitud determinada. Para hacer esto, usamos el separador **`:`** e indicamos como **modificador** el número de caracteres que tendrá el fragmento indicado. 

  ```
  {VALOR:N}
  ```

  Por ejemplo, si queremos que el espacio para el nombre del usuario tenga **por lo menos** 16 caracteres haríamos lo siguiente:
f'Nombre de usuario: {nombre:16}<----'
"""

cadena_larga = "Nombre de más de 16 caracteres"
print(f'Nombre de usuario: {cadena_larga:16}<----')

"""
Modificadores de relleno y alineación:** podemos alinear el contenido con el uso de caracteres adicionales. Por ejemplo, si usamos `^` antes de indicar el número de caracteres, la cadena original quedará centrada, con **`<`** alineada hacia la izquierda y con `>` alineada hacia la derecha.

"""
print(f'Nombre de usuario: {nombre:^24}<----')
print(f'Nombre de usuario: {nombre:.^24}<----')

help(ord)
help(chr)

##################################################
##########   💻  Práctica: Gritar  💻  ##########
##################################################

## 👇 Escriba su código DEBAJO de esta línea 👇 ##


# Recibe la cadena de la entrada con la función 'input'.

cadena = input()

# 1) Convierte las minúsculas en mayúsculas.

cadena = cadena.upper()

# 2) Reemplaza la letra 'O' por 'OOO'.
cadena = cadena.replace('O', 'OOO')

# 3) Añade los signos de exclamación "!!!!!" al final.

cadena = f"{cadena}!!!!!"

# Envía el resultado a la salida con la función 'print'.

print(cadena)

## ☝️ Escriba su código ENCIMA de esta !!!!!línea ☝️ ##

#--------------------------------------------------------------------------------------------------------
# Day20 - What Can Range really do?

# Bring on the start of list making by learning all the capabilities of range.

"""
What can range really do?
Give range one number, and it will count up to that number. However, you can actually give the range function a few options...

starting value: what number do you want to start with?
ending value: the number after the number you want to end with (example: if you type 10 as the ending value, the computer will count until 9)
increment: How much should it increase by every time it loops? (example: Do you want to count by 1s, 5s, 10s?)

The ending value has an unsaid 'less than'. Meaning the computer will stop one number before the ending number that is written in the range.

Let's try it out
The first number in this range, 100, is the starting value. The second number in this range, 110, is the ending value (Remember to always put the ending number as one more than where you want to end up).

👉 What number will the code run first? What number will be last? Run the code and find out.

for i in range(100, 110):
  print(i)
👉 What do you expect to print with the range below? Run and find out.

for i in range(1, 7):
  print("Day", i)
Did you notice that the counter stopped at 'Day 6'? Change the ending value to be one more than the last number you want shown---in this case, 8 because we want to display 7 days of the week.

for i in range(1, 8):
  print("Day", i)
👉 What happens when you run this code?

print("Thirteen Times Table")
for i in range(1, 13):
  print(i, "x 13 =", i * 13)
Let's add increments to our range.

Increments
We know that this range will start at 0 and continue to 999,999 (which is the number right before the ending value written). The number will increase in increments of 25 each time.

👉 What numbers do you expect to see? Hit run and find out.

for i in range (0, 1000000, 25):
  print(i)
Counting Backward
In this example, we are starting at 10 and counting backward to 0 (because 0 is what comes right before the ending value listed), and counting backward 1 each time.

👉 What do you expect to see when you hit run?

for i in range(10, -1, -1):
  print(i)

Fix My Code
👉 Try and fix this code which is full of errors.


"""

for i in range (20, 40, 1):
  print(i)

# 👉 Day 20 Challenge

""" List Generator
Ask the user to list a starting number, ending number, and increment to use. Display an answer based on the users' answers (use the input command.)

Example:
Start at: 200
End before: 300
Increment between values: 20

200
220
240
260
280 """

num_inicial = int(input())
num_final = int(input())
num_incremento = int(input())

for i in range(num_inicial, num_final, num_incremento):
  print(i)


print("Welcome to my number list generator.")
print()
print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")
print()

x = int(input("What number do you want to start with? "))
y = int(input("What number do you want to end with? "))
z = int(input("How many should I add each time? "))

for i in range(x, y, z):
  print(i)

# números imaginarios ejemplo > 1+5j -> 1 parte real y 5j parte imaginaria

print(type(1+5j))
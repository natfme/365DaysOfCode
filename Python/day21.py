# Day21 - Throwback to Math Facts

# Create a game to test your friends’ knowledge on their math facts.

"""
👉 Day 21 Challenge
Test your family and friends on their multiplication knowledge (or just be really mean to people you know and ask them to work out their multiplication tables for 5,474,000,000....)

Prompt the user by asking for a multiplication table for the number of their choice.
Generate the multiplication table for 1 to 10 times that number and ask each math fact as a question (psst...that's a hint).
If the user gets the math correct, award them a point. If they get it wrong, do not give them any points.
At the end of the 10 rounds, show the user their score out of 10 for how many math facts they got correct.
Why not give users an emoji if they get all 10 math facts correct?

Math Game!

Name your multiples: 7

1 X 7 = 7
Great work! 

2 X 7 = 14
Awesome!

3 X 7 = 54
Nope. The answer was 21. 

---

You scored 3 out of 10.


Hints:
*Use a variable when asking the user what multiplication facts they want to solve.
*Within the for loop, set up a variable, input statement, and if statements.
*Don't forget to include your counter and an if statement to say when to give a perfect score emoji.
"""
#from getpass import getpass as input

""" print("Math Game!")
print()
num = int(input("Name your multiples: "))
print()
score = 0
for i in range(1,11):
    result = i * num
    resultUser = int(input(f"{i} X {num} = "))
    phrases = ["Great work!", "Awesome!", "You got it right!", "Yaaay!", "Well done!", "Great job", "You\'re a genius", "Wow, that\'s impressive work", "This is insanely good", "Excellent!"]

    if resultUser == result:
        print(phrases[i-1])
        print()
        score += 1
    else:
        print(f"Nope! the answer is {result}")
print(f"Your score {score} out of 10") """

# ------------------------------------------------------------------------
"""
print("Welcome to Math Facts Game")
print()
print("How well do you know your math facts? Pick a number and I will give you 10 math facts to solve.")
print()

fact_family = int(input("Name your multiples: "))
print()

counter = 0
for i in range(1, 11):
  correct_answer = i*fact_family
  print(i, "x", fact_family)
  answer = int(input("> "))
  if answer == correct_answer:
    print("You got it right!")
    counter += 1
  else:
    print("That's not correct. It should have been", correct_answer)

if counter == 10:
  print("Wow! A perfect score! 🥳")
else:
  print("You got", counter, "out of 10 correct.")
  """

#La planta que quiere es

""" name = input("Introduce el nombre de la flor: ")

if name == "ESPATIFILIO":
    print("Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!")
elif name == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!")
else:
    print("¡ESPATIFILIO!, ¡No", name + "!")
 """
# ----- Soy o no bisiesto ------

""" year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if year % 4 != 0:
		print("Año Común")
	elif year % 100 != 0:
		print("Año Bisiesto")
	elif year % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")
		 """
# x, y, z = 5, 10, 8

# x, y, z = 5, 10, 8
# x, y, z = z, y, x

""" x = 10
 
if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")

# ¿Cuál es el resultado del siguiente fragmento de código?

x = 1
y = 1.0
z = "1"
 
if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")

while True:
    print("Estoy atrapado dentro de un bucle.")
    print("Para finalizar tu programa, simplemente presiona Ctrl-C (o Ctrl-Break en algunas computadoras)") """


""" # Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:

# ¿Es el número más grande que el valor de largest_number?

    if number > largest_number:

# Sí si, se actualiza largest_number.
      largest_number = number

# Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number) """

#---------------------------------------------------------------------------------------

# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.
 
odd_numbers = 0
even_numbers = 0
 
# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))
 
# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))
 
# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

counter = 5
while counter:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

# Adivina el número secreto

""" Escenario

Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada secret_number. Quiere que todos los que ejecutan su programa jueguen el juego Adivina el número secreto, y adivina qué número ha elegido para ellos. ¡Quiénes no adivinen el número quedarán atrapados en un bucle sin fin para siempre! Desafortunadamente, él no sabe cómo completar el código.

Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

pedirá al usuario que ingrese un número entero;
utilizará un bucle while;
comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente. Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."
¡El mago está contando contigo! No lo decepciones.

  INFO EXTRA  
Por cierto, observa la función print(). La forma en que lo hemos utilizado aquí se llama impresión multilínea. Puedes utilizar comillas triples para imprimir cadenas en varias líneas para facilitar la lectura del texto o crear un diseño especial basado en texto. Experimenta con ello. """

secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

user_number = int(input("Ingresa el número: "))

while user_number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    user_number = int(input("Ingresa el número nuevamente: "))
print(secret_number, "¡Bien hecho, muggle! Eres libre ahora.")

"""
nota la palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto; es una instrucción vacía - la colocamos aquí porque la sintaxis del bucle for exige al menos una instrucción dentro del cuerpo (por cierto - if, elif, else y while expresan lo mismo).
"""
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

"""
Fundamentos del bucle for – contando lentamente (mississippily)

Escenario
¿Sabes lo que es Mississippi? Bueno, es el nombre de uno de los estados y ríos en los Estados Unidos. El río Mississippi tiene aproximadamente 2,340 millas de largo, lo que lo convierte en el segundo río más largo de los Estados Unidos (el más largo es el río Missouri). ¡Es tan largo que una sola gota de agua necesita 90 días para recorrer toda su longitud!

La palabra Mississippi también se usa para un propósito ligeramente diferente: para contar mississippily (mississippimente).

Si no estás familiarizado con la frase, estamos aquí para explicarte lo que significa: se utiliza para contar segundos.

La idea detrás de esto es que agregar la palabra Mississippi a un número al contar los segundos en voz alta hace que suene más cercano al reloj, y por lo tanto "un Mississippi, dos Mississippi, tres Mississippi" tomará aproximadamente unos tres segundos reales de tiempo. A menudo lo usan los niños que juegan al escondite para asegurarse de que el buscador haga un conteo honesto.

Tu tarea es muy simple aquí: escribe un programa que use un bucle for para "contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco, el programa debería imprimir en la pantalla el mensaje final "¡Listos o no, ahí voy!"

Utiliza el esqueleto que hemos proporcionado en el editor.

  INFO EXTRA  
Ten en cuenta que el código en el editor contiene dos elementos que pueden no ser del todo claros en este momento: la sentencia import time y el método sleep(). Vamos a hablar de ellos pronto.

Por el momento, nos gustaría que supieras que hemos importado el módulo time y hemos utilizado el método sleep() para suspender la ejecución de cada función posterior de print() dentro del bucle for durante un segundo, de modo que el mensaje enviado a la consola se parezca a un conteo real. No te preocupes - pronto aprenderás más sobre módulos y métodos.

Salida esperada:

1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
"""

import time

# Escribe un bucle for que cuente hasta cinco.
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle, emplea : time.sleep(1)

# Escribe una función print con el mensaje final.

for i in range(1,6):
    time.sleep(1) #el método sleep() para suspender la ejecución de cada función posterior de print() dentro del bucle for durante un segundo
    print(f"{i} Mississippi")

print("¡Listos o no, ahí voy!")

"""
Las sentencias break y continue

break - sale del bucle inmediatamente, e incondicionalmente termina la operación del bucle; el programa comienza a ejecutar la instrucción más cercana después del cuerpo del bucle.
continue - se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; el siguiente turno se inicia y la expresión de condición se prueba de inmediato.
"""

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

# ------------------------------------------

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

# -----------------------------------------------

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
La sentencia break - atrapado en un bucle

Escenario
La instrucción break se implementa para salir/terminar un bucle.

Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" como la palabra de output secreta, en cuyo caso el mensaje "Has dejado el bucle con éxito." debe imprimirse en la pantalla y el bucle debe terminar.

No imprimas ninguna de las palabras ingresadas por el usuario. Utiliza el concepto de ejecución condicional y la sentencia break.
"""


"""
💡 Problema: Dividir en grupos

Un docente quiere realizar una actividad en grupo para una clase de n estudiantes, con exactamente x estudiantes por grupo. Sabe que es posible que la división implique la existencia de un grupo con menos estudiantes, por lo que plantea una estrategia.


En primer lugar, cuando vaya a realizar la actividad, asignará aleatoriamente los grupos para prevenir que sean los mismos estudiantes en cada actividad. En caso de que uno de los grupos quede con menos de x estudiantes, estos no realizarán la actividad y en su lugar apoyarán el proceso de calificación del resto de grupos.


Este grupo de calificadores deberá preparar y entregar un reporte corto de observaciones del trabajo realizado por cada uno de los grupos completos que fueron asignados.


Por ejemplo, para una clase con 16 estudiantes y una actividad que requiera crear grupos de 6 personas, podríamos obtener 2 grupos completos y un grupo de 4 calificadores. Cada uno de ellos calificaría individualmente a los 2 grupos creados, para un total de 8 reportes creados y entregados al docente.
"""
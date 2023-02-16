"""
Escenario

Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.

Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide - es plana. La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.

La figura ilustra la regla utilizada por los constructores:

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

Prueba tu código con los datos que hemos proporcionado.

Ejemplo:
  X
 X X
X X X

Altura = 3 y Número de bloques = 6

Datos de Prueba
Entrada de muestra:             Salida esperada:
6                               La altura de la pirámide es: 3
20                              La altura de la pirámide: 3
1000                            La altura de la pirámide: 44
2                               La altura de la pirámide: 1

"""
""" numeroBloques = int(input("Ingresa el número de bloques: "))

altura = 0
capa = 1
while capa <= numeroBloques:
    altura += 1
    numeroBloques -= capa
    capa += 1

print("La altura de la pirámide es:", altura)

name = input("Escribe tu nombre: ")
rolName = input("Escribe tu nombre de rol: ")
firstAdjective = input("Escribe el primer adjetivo: ")
secondAdjective = input("Escribe el segundo adjetivo: ")
firstFood = input("Escribe la primera comida: ")
secondFood = input("Escribe la segunda comida: ")
feelings = input("Escribe un sentimiento: ")

print()
print(f"{name} comenzó su primer bootcamp de Generation hoy. Se está capacitando como {rolName}. Descubrieron que su cohorte era muy {firstAdjective} pero su maestro era, al menos, {secondAdjective}. Para el almuerzo comieron {firstFood} y {secondFood} mientras revisaban sus notas. Sienten {feelings} pero están decididos a completar el bootcamp.")
 """
""" def dispense_fibonnaci(sequence_number):
    x = 0
    y = 1
    lista = [x, y]

    if sequence_number in range(0, 100):
        for i in range(sequence_number-1):
            z = x + y
            lista.append(z)
            x = y
            y = z
            i += 1
        print(lista)

        if sequence_number == 0:
            return 0
        else:
            return lista[sequence_number]


numero = int(input("Escriba el número: "))
print(dispense_fibonnaci(numero))


for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

----------------------------------------------------------------------------------------------------

Los fundamentos de las listas

Escenario
Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4, y 5.

Tu tarea es:

escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1)
escribir una línea de código que elimine el último elemento de la lista (Paso 2)
escribir una línea de código que imprima la longitud de la lista existente (Paso 3). """

""" hat_list = [1, 2, 3, 4, 5, 6, 7]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.

num = int(input("Escriba un número: "))
x = int(len(hat_list) / 2)

hat_list[x] = num

print(hat_list)

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.

del hat_list[-1]
print(hat_list)

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.

print(len(hat_list))

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#

my_list = [1, 2, 3, 4, 5, 6, 7]

length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

----------------------------------------------------------------------------------------------------------------------------------------

Los fundamentos de las listas: los Beatles

Escenario
Los Beatles fueron uno de los grupos de música más populares de la década de 1960 y la banda más vendida en la historia. Algunas personas los consideran el acto más influyente de la era del rock. De hecho, se incluyeron en la compilación de la revista Time de las 100 personas más influyentes del siglo XX.

La banda sufrió muchos cambios de formación, que culminaron en 1962 con la formación de John Lennon, Paul McCartney, George Harrison y Richard Starkey (mejor conocido como Ringo Starr).


Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

paso 1: crea una lista vacía llamada beatles;
paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
paso 3: emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.
Por cierto, ¿eres fan de los Beatles? (Los Beatles son una de las bandas favoritas de Greg. Pero espera...¿Quién es Greg?) """

# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
for i in range(2):
    beatles.append(input("Ingrese los otros miembros: "))
print("Paso 3:", beatles)

# paso 4
del beatles[-1]
print("Paso 4.1:", beatles)
del beatles[-1]
print("Paso 4.2:", beatles)

# paso 5
beatles.insert(0,"Ringo Starr")
print("Paso 5:", beatles)

# probando la longitud de la lista
print("Los Fav", len(beatles))

# Las listas pueden ser anidadas
my_list = [1, 'a', ["lista", 64, [0, 1], False]]

my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
 
for color in my_list:
    print(color)

lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0
 
for number in lst:
    add += number
    lst_2.append(add)
 
print(lst_2)
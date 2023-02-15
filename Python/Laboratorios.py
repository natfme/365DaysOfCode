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
numeroBloques = int(input("Ingresa el número de bloques: "))

altura = 0
capa = 1
while capa <= numeroBloques:
    altura += 1
    numeroBloques -= capa
    capa += 1

print("La altura de la pirámide es:", altura)


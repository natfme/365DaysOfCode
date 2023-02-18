# Ordenando una lista

my_list = [8, 10, 6, 2, 4]  # lista a ordenar
 
for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.
print(my_list)
print("------------------------------------")
my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1): # i comienza en 0
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)

print("------------------------------------")
""" my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list) """

print("------------------------------------")
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

print("------------------------------------")
lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort()
print(lst) # output: [1, 2, 3, 4, 5]

print("------------------------------------")
lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst) # output: [4, 2, 1, 3, 5]

print("------------------------------------")

lst = ["D", "F", "A", "Z"]
lst.sort()
 
print(lst)

print("------------------------------------")

a = 3
b = 1
c = 2
 
lst = [a, c, b]
lst.sort()
 
print(lst)

print("------------------------------------")
a = "A"
b = "B"
c = "C"
d = " "
 
lst = [a, b, c, d]
lst.reverse()
 
print(lst)
print("------------------------------------")

# my_list[inicio:fin]
# Una rebanada de este tipo crea una nueva lista (de destino), tomando elementos de la lista de origen - los elementos de los índices desde el inicio hasta el fin - 1.

# Copiando la lista completa.
list_1 = [10, 8, 6, 4, 2]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)
print("------------------------------------")
# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
print("------------------------------------")
# Indices negativos
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
print("------------------------------------")
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)
print("------------------------------------")
# my_list[:end]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
print("------------------------------------")
# my_list[start:]
# my_list[start:len(my_list)] más compacto

my_list = [10, 8, 6, 4, 2]
new_list = my_list[2:]
print(new_list)
print("------------------------------------")
# omitir el inicio y fin crea una copia de toda la lista:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

print("------------------------------------")
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

print("------------------------------------")
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

print("------------------------------------")
""" my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list) #La instrucción del eliminará la lista, no su contenido, la instrucción print provoca un error de ejecución """

# in, on y not en listas

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

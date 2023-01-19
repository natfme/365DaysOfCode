"""********************************************************************
* Day 3 - Concatenate and methods for strings
*
*Concatenar
*You can combine as many things as you want in any order you want, as long as they're separated by that comma!
*********************************************************************"""

"""number = input("Give me a number: ")
group = input("Give me a collective noun for a group of things: ")
thing = input("Give me the name of a weird or wacky thing: ")
print("No I don't think that", number, "is a", group, "of", thing,". That's just odd.")

yourName = input("Name: ")
whatYear = input("What year is it?: ")
print(yourName, "thinks it is", whatYear)"""

#------------------------
#print("=== Your Song Generator ===")
#print("""You\'ll be asked a bunch of 
#questions then we\'ll make you up an 
#amazing song, totally copyright free 😭""")
#print()
#person = input("Name a person famous for something good: ")
#thing = input("Name a thing they did: ")
#place = input("Name a place you like: ")
#rhyme = input("Give me a verb that rhymes with your person\'s name: ")
#print()
#print("There was a person called", person)
#print("Who did something cool like", thing, "at the wonderful", place, "where you\'ll find me", rhyme)


#---Day3 Challenge
""" 1. Create these as a variable:
A type of food
A type of plant
A method of cooking
A word to describe burned food
A household item
2. Output a nice looking Recipe page that *concatenates* a dish in this format:
cooking food with burned plant on a bed of item """


#Example
"""Name a food > Mac & Cheese
Name a type of plant > Cactus
Name a method of cooking > Saute        
What word describes burned food? > Ruined
Name a DIY item > Hammer

#------MENU
Saute Mac & Cheese with Ruined Cactus on a bed of Hammers


nameFood = input("Name a food: ")
namePlant = input("Name a type of plant: ")
methodCook = input("Name a method of cooking: ")
wordFood = input("What word describe burned food: ")
nameDIY = input("Name a DIY item: ")

print("MENU")
print(methodCook,nameFood,"with",wordFood,namePlant,"on a bed of",nameDIY+"s") """


#String in Python

""" String Methods
Python has a set of built-in methods that you can use on strings.
Note: All string methods return new values. They do not change the original string. """


#Cheking a string
a = "Python is a very large"
print("very" in a)

text = "Ella sabe programar en Python"
print("Javascript" in text)
print("Python" in text)

if "Python" in text:
    print("Elegiste bien con Python puedes hacer análisis de datos")
else:
    print("Elegiste bien Javascript también es un buen lenguaje")

#Tamaño de mi cadena de carácteres
size = len(text)
print(len("J"))
print(size)

print(text)
print(text.upper()) #Pasa toda la cadena a Mayúsculas
print(text.lower())  #Pasa toda la cadena a minúsculas
print(text.count("a"))  #Cuenta cuantos veces se repite el carácter

print(text.swapcase()) #Pasa los carácteres que están en mayúsculas a minúsculas y los que están en minúsculas a mayúsculas
print(text.startswith('Ella')) #Nos pregunta por si el texto empieza por algo en especifico y nos responde True or Falso
print(text.endswith('Rust')) #Nos pregunta por si el texto finaliza en algo en especifico y nos responde True or Falso
print(text.replace('Python','Go')) #Reempaza el texto por el texto que se coloca como argumento

text_2 = 'este es un título'
print(text_2)
print(text_2.capitalize()) #Pone el primer caracter en mayúscula
print(text_2.title()) #Coloca la primera letra de cada palabra en mayúscula
print(text_2.isdigit())
print("374".isdigit())

#indexing and slicing

""" 
0    1   2   3   4   5  6  7  8  9  10  11  12
¡    H   o   l   a   ,     M  u  n  d   o   !
-13 -11 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
"""

text = "Ella sabe Python"
print(text[0])
print(text[1])
print(text[15])
#print(text[20]) #Marca error porque la última posición es la 15

print(len(text)) #Recordar que la posición empieza a contar en 0 entonces la última posición sería la 15, o sea, tamaño o longitude del texto -1

print(text[len(text)-1])

#Si le doy el texto y le pongo -1 me da el último caracter de la cadena

print(text[-1])

#Slicing -> basado en la posición de los carácteres podemos sacar subtextos


a = "Hello!"
b = """Python is a great language but you to follow some rules"""

print(a, b)

c= "Hello, World!"
d= "Hello World!"
print(c[0])
print(c[2:7])
print(d[2:7])
print(len(c))

print(text[0:4]) #no inlcuye el extremo derecho
print(text[10:16])
print(text[5:9])
print(text[0:10])
print(text[:10]) #Hace una consulta desde el inicio hasta el punto que se indica

print(text[5:-1])
print(text[5:])
print(text[::-1]) #palabra al revés

gretting = "Hello all Subscribers!"
x = len(gretting)
print(x)
print(gretting[0:11])
print(gretting[0:x-1])
print(gretting[-1])
print(gretting[-12:-1])

#Modify Strings
print(gretting.upper())
print(gretting.lower())
print(gretting.swapcase())
print(gretting.capitalize())
print(gretting.title())

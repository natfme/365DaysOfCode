# Day 2 - 100 Days of Code: Input & Variables
"""Naming variables
 You can give a variable any name you want, but you can't use spaces. You can use:
-underscores_between_words
-camelCaseToMakeItEasierToRead """

""" myName = input("What's you name?: ")
myAge = input("How old are you? :")
print("Gee, that's REALLY OLD")
replit = input("Do you like Replit?")
print("OF COURSE YOU DO!")

#Printing a Variable
print()
print("So, you are")
print(myName)
print("and are the ripe old age of")
print(myAge)
print("and clearly think that Replit is")
print(replit)


#Examples
myGrandma = input ("How's your Grandma going: ")
print(myGrandma)

myLunch = input("What are you having for lunch? ")
print("Hmm, it sounds like you really should just order")
print(myLunch)
print("as soon as possible!")

print("Definitely not a Phishing Scam")
print()
myName = input("What is your name?")
print("Thanks for logging in")
print(myName)
cardNumber = input("What is your credit card number?")
print("Thanks, I definitely won't put")
print(cardNumber)
print("into Amazon and order anything weird")
print()
print("Promise")
maidenName = input("What is your Mother's maiden name? ")
print()
print("That's cool, I just wanted to know that")
print(maidenName)
print("was your Mum's maiden name. Not because the bank requested it or anything, honest.") 

#Challenge
myName = input("What's you name?: ")
myFood = input("What's your favourite food?: ")
myFavmusic = input("What's your favourite music?: ")  #Synthwave
myFavsinger = input("What's your favourite singer?: ")  #Rick Astley
myPlace = input("Where do you live?: ")
print()
print("Getting to know you!")
print("You are " + myName)
print("You're probably hungry for " + myFood)
print("and you're definitely getting your groove on to " + myFavmusic)
print("and Anything by our man " + myFavsinger)
print("living in the amazing  "+ myPlace) #Edge of reality


print("Getting to know you!")

YourName = input("What is your name?")
Hungry = input ("What is your favorite food?")
Music = input("What is your favorite music?")
WhereAreYou = input("Where are you?")

print("You are")
print(YourName)
print() 

print("You're probably hungry for")
print(Hungry)
print()
print("You're probably listening to")
print (Music)
print()
print ("You're probably living in the amazing")
print (WhereAreYou)
print() 
print ("Have a great day!") """

#Variable en Python - Una variable es un espacio de memoria donde se almacena un valor
a = 5 #Esto es una variable
b = 15 #Esto es otra variable
c= 'Python'
d = a + b #Esto es una variable que se obtiene sumando dos varibles
print(c)
print(d)

#Tipos de datos en Python
a = 10 #Integer
b = 10.3 #Float
c = 2j  #Complex
d = "a" #Character -> String
e = "Python" #String
f = True #Boolean
g = False #Boolean

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print("Tipos\nde\ndatos")  #\n salto de línea
print("Primero\tSegundo\tTercero")  #\t tabulación
print("1\t2\t3")
print('Ana\'s dolls') #Si se quiere imprimir comillas dentro de la cadena de carácteres se puede de tres formas:
print("Estas comillas son simples (')") #Si se quiere comillas simples se delimita con comillas dobles
print('Estas comillas son dobles (")') #Si se quiere comillas dobles, se delimita con comillas simples
print("Estas son comillas simples (\') y estas son dobles (\")") #Si se requiere las dos, tanto comillas simples como dobles, se usa backslash \
print("""Cuando se desea imprimir textos que se extienden por más de una línea de código: 
1. Hola
2. Mundo
3. ¡Hola, Mundo!""") #Cuando se desea imprimir textos que se extienden por más de una línea de código se usan tres comillas dobles como delimintador

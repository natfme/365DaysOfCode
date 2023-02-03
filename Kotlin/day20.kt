// Day20 - Objects

/*
Everything is an object
In our life, we are always surrounded by objects: you drive a car, watch TV, read books, pay for bananas with your smartphone. In Kotlin, every time when you work with variables, you work with objects. For example, an integer 5 and a string "love" are objects. It is convenient because programmers are people, and people are used to dealing with objects. In this topic, we will learn about the inner structure of objects, their state and behavior, and their distinctive features.

------------------------------------------------------------------------------------------------------

State and behavior
Objects are complex structures that can store some data and do something. How to get an object? Well, an object is a part of memory that stores some sort of information. Variables and values just point to objects. So, you can work with objects with the help of variables. A simple example of an object is a String that stores a message. Let's take a closer look at it.

First of all, a message has a state: it contains not only a sequence of symbols but also the size of the sequence, that is, the length of the message. In Kotlin, something that allows you to access the state of an object is called a property. Just put a dot and write the name of the property after the object, and you will get what you want! Suppose you have a simple String variable msg: val msg = "Hi". The length property gives us the length of the string:

val msg = "Hi"
println(msg.length) // 2

In Kotlin, some functions are bound to a specific type. This makes using the objects more logical because functions represent the behavior of those objects. These functions are also called member functions or methods. The syntax is similar: just put a dot. For example, we can repeat our message using the member function repeat():

val msg = "Hi"
println(msg.repeat(3)) // "HiHiHi"
Will print:

HiHiHi

As you can see, even the standard String type has a really complex inner structure.

------------------------------------------------------------------------------------------------------------------------

Copying by reference
In programming, copying something is a very common operation. We use = in almost all the cases. Let's take a look at how it works in Kotlin using a simple analogy with a bank account.

You may have several cards connected to one account. If you buy something with one of these cards, you still spend money from that one bank account, even though the cards are different.

In Kotlin, similar rules apply. If you create a variable and assign an object to it, another variable can point to the same object as well. Say you wrote text messages like this:

val msg1 = "Hi"
val msg2 = msg1
There will be two values pointing to a single object "Hi":


val msg1  <---->
                  "Hi"
val msg2  <---->

In other words, the = sign does not copy the object itself, it only copies a reference to it.

---------------------------------------------------------------------------------------------

Mutability

What happens if you change an object assigned to multiple variables by changing the value of one of these variables? It depends on the type of object. An object can be either mutable or immutable.

You already know that Int, String, Float, and Double in Kotlin are objects. But there is a nuance. For example, the Int or String variables behave just like the primitive types of data in other programming languages, but at the same time, they are objects – in other words, unchangeable objects. Let's look how it works:

var a: Int = 100
val anotherA: Int = a
println(a == anotherA)  // true
println(a === anotherA) // true
a = 200
println(a == anotherA)  // false
println(a === anotherA) // false

As you can see, when we change the value of the variable a = 200, we do not change its object – the variable a is assigned a new reference to the object with the value 200.

Let's look at one example, but now with the Double type of data:

var d1: Double = 1.5
val d2 = d1
println(d1 === d2) // true
d1 += 1            // d1 is 2.5 now
println(d1 === d2) // false

If the object is immutable, you cannot change it, but you can use another object and assign this new object to the same variable. When you reassign the variable, it will point to a new object and other variables will still point to the old object. Standard types such as strings or numbers are immutable, so it's safe to copy them by reference.

------------------------------------------------------------------------

Conclusion

Let's recap the main points of the topic:

*Objects are complicated structures with states, properties, and member functions.

*An object is a part of memory that stores something.

*Variables only point to objects.

*Objects can be mutable or immutable.

*The only way to change something in a variable bound to an immutable object is by reassigning it.

*You can freely copy immutable objects such as standard types.

------------------------------------------

Wise choice

Choose all the variants that can be considered objects:

val dollar = '$'

val b: Int = 0

var a: String = "a"

-----------------------------------------------------------------

Function type

A drum can make noise. How can you write code that makes a drum make some noise?

drum.makeNoize()

---------------------------------------------------------------------------

Accessing properties

There is a variable spaceship that references an object with a color property. How can you use this variable to get the value of this property?

spaceship.color

-----------------------------------------------------------------------------

What's going on?

This code prints the same object two times in a row:

println(obj)
println(obj)

To your surprise, the two lines in the console are different. Why?

The object is modified elsewhere because there is another reference to it

---------------------------------------------------------------------------------------------

Object count

How many objects are created here?

val lineOne = "Happy New Year,"
val lineTwo = lineOne
val lineThree = lineOne

answer : 1

-------------------------------------------------------------------------------

Property

In Kotlin, something that allows you to access the state of an object is referred to as property.

How can you access the property of a variable?

variable.property
*/

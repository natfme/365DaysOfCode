// Day21 - Equality

/*
Comparison
Imagine a situation: you receive two identical messages from your friend. The messages are "Hi" and "Hi". You see them and understand: the messages are the same. If you want to compare these messages in Kotlin, you can store them as string values:

val msg1 = "Hi"
val msg2 = "Hi"
Then you can use the comparison operator ==. For example, print(msg1 == msg2) gives true, and print(msg1 == "Hello") gives false. Variables msg1 and msg2 have the same state, which is called structural equality. Also, you may check for inequality using the operator != . For example, print(msg1 != "Hello") gives true.

Note that some complex data types may not have the operator==. We will discuss this later. Box in the following examples has this operator.

Let's look at an example of copying a mutable object. Suppose you have a box that stores balls, and you can add one ball to it. Try to copy this box and change the original:

val blueBox = Box(3)          // box with 3 balls
val azureBox = blueBox 
println(blueBox == azureBox ) // true, it's a copy
blueBox.addBall()             // add a ball to the first box
println(blueBox == azureBox ) // true, the second box also contains 4 balls
When you change the first box, its copy changes, too. This is because blueBoxand azureBoxpoint to the same object. How do you check this? Let's see how to check the referential equality.

-------------------------------------------------------------------

Referential equality
You know that variables can have the same state and can be the same (point to the same object). In both cases, == returns true. However, Kotlin provides a special operator === to check if the variables point to the same object. For example:

val blueBox = Box(3)
val azureBox = blueBox 
val cyanBox = Box(3)
println(blueBox == azureBox)  // true
println(blueBox === azureBox) // true, azureBox points to the same object
println(blueBox == cyanBox)   // true
println(blueBox === cyanBox)  // false, cyanBox points to another object
So, blueBox and cyanBox have the same state, but they point to different objects. In this case, if you change the state of blueBox, cyanBox remains the same:

blueBox.addBall()
println(blueBox == cyanBox) // false
Also, you may check for referential inequality with the operator !== . For example, print(blueBox !== cyanBox) gives true.

Another interesting thing about the === operator is the equality of immutable objects. Let's look at the following example:

var two = 2
var anotherTwo = 2
println(two === anotherTwo) // true
These variables point to the same object! Don't worry about this: as you remember, you cannot change an immutable object, so if you try to do something with the variable, it will point to a new object and other variables will still point to the old object. Try to change two:

two++
println(two)        // 3
println(anotherTwo) // 2
So, immutable objects are really useful and help you avoid a lot of possible problems with copying.

------------------------------------------------------------------------------

Base types and equality
You are already quite familiar with objects in Kotlin: you have worked with text and number data a lot. In many programming languages, primitive data types – or primitives – store the most often used simple data types. Their internal structure is organized in its own way. This is not the case in Kotlin. As you might have guessed, the familiar Int, String, Float, and Double in Kotlin are also objects! But there is a nuance. For example, the Int or String variables behave just like the primitive types of data in other programming languages, but at the same time, they are objects – in other words, immutable objects. Let's look how it works:

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
As you can see, the result is the same. Now, let's look at an example with modifiable objects:

val list1: MutableList<Int> = mutableListOf()
val list2: MutableList<Int> = list1
list1.add(1)
println("list1 $list1") // list1 [1]
println("list2 $list2") // list2 [1]
list2.add(5)
println("list1 $list1") // list1 [1, 5]
println("list2 $list2") // list2 [1, 5]
As you can see in this example, the variables list1 and list2 refer to the same object. When you change the object through the first variable, we see the updated data through the second variable.

-------------------------------------------------------------------

Conclusion
Let's go over the main points of the topic once again:

Structural equality of variables implies equality of inner states.

You can use the operators == and != to check structural equality.

Referential equality of variables means that these variables point to the same object.

You can use the operators === and !== to check referential equality.

The val keyword means that you cannot reassign the variable, not immutability.
*/

// Practice 1

/*
Referential equality

Check if the variables captainJackSparrow and pirateJackSparrow point to the same object and print the result using the println() function.

val pirateJackSparrow = Sailor("None")
val captainJackSparrow = Sailor("None") 
// put your code here
println(pirateJackSparrow === captainJackSparrow)
*/

//Practice 2

/*
The same object

What construct is used to check that two variables refer to the same object in Kotlin?

===
*/

//Practice 3

/*
How to compare?

Which construction do we use to compare two objects in Kotlin?

==
===
*/

// Practice 4

/*
Equality

Suppose you compare two variables with the === operator, and the result is true.

Does this mean that if you change the value of the first variable, the value of the second one will also change? No

These variables may point to an immutable like Int, so if you do something with one of these, the other will not change.
*/

// Think of all possible cases!

// Practice 5

/*
True captain

“The problem is not the problem. The problem is your attitude about the problem. Do you understand?” – Jack Sparrow

This code prints the name of the current captain of the ship (now, it is Hector's name).

However, the crew elected a new captain, and now it's Jack Sparrow.

Fix the declaration of the captain variable, create a new Pirate object with Jack Sparrow's name, assign a new value to the variable captain, and print the name of the current captain again.

// you do not need to understand how it works, ignore it
data class Pirate(val name: String)

// Do not touch the lines above

fun main() {
    // fix the declaration below
    val captain1 = Pirate("Hector Barbossa")
    println(captain1.name)
    // put your code here
    val captain2 = Pirate("Jack Sparrow")
    println(captain2.name)
}

// Practice 6

Kings of Sweden

Fix the code below so that the king is reassigned to another object.

val kingCharlesTheEleventh = Human()
val kingCarolusRex = Human()  

val king = kingCharlesTheEleventh
king = kingCarolusRex

fix it

    val kingCharlesTheEleventh = Human()
    val kingCarolusRex = Human()  
    
    var king = kingCharlesTheEleventh
    king = kingCarolusRex

// Practice 7

Different equality

Match equality operators with their descriptions.

Match the items from left and right columns

===     Points to the same object
!==     Points to the different objects
==      Equal inner structure
!=      Different inner structure

*/

// Sololearn kotlin

/*
class Button {
    var width = 0
    var height = 0
}

fun main(args: Array<String>) {
    val b1 = Button()
    b1.width = readLine()!!.toInt()
    b1.height = readLine()!!.toInt()
    
    println(b1.width+b1.height)
}

// --------------------------------
Onjects

val c = Car ()

println(c.color) //Create an object type Car and output the color property's value

// -------------------------------------

Constructors


Constructors allow you to initialize properties when objects are created.
The constructor is defined using parentheses after the class name and includes the properties we want:
For example:

class User(val name:String, val age:Int) {
} 

Now, when creating a User object, we need to pass it values for the name and age properties:

As you can see, the constructor takes arguments and uses them to initialize the properties of the class.
Similar to function arguments, we can provide default values for the arguments.

class User(val name:String, val age:Int) {

}
fun main(args: Array<String>) {
    val u1 = User("James", 42)
    println(u1.name)
    println(u1.age)
}

//----------------------------------------------

class Car(val color:String) {

}
fun main(args: Array<String>) {
    val c = Car("Red")
    println(c.color)
}

class User {
    var name = ""
    var age = 0
    constructor(nm: String) {
      name = nm
    }
    constructor(nm: String, a: Int) {
      name = nm
      age = a
    }
  }
  fun main(args: Array<String>) {
      val u1 = User("James", 42)
      val u2 = User("Amy")
      println(u1.name)
      println(u2.name)
      println(u1.age)
  }

  Now, our User class has two constructors
  As you can see, constructors are like functions, taking arguments.}

  // ----------------------

  Buttons Constructor


You need to modify the Button class and add a default constructor to it, which initializes the width and height properties.
Add the constructor so that the given code in main works as expected.
The given code takes the values from user input and passes them to the object's constructor.


class Button {
    var width = 0
    var height = 0
    constructor(wd: Int, hg: Int){
        width = wd
        height = hg
    }
}
fun main(args: Array<String>) {
    val b1 = Button(readLine()!!.toInt(), readLine()!!.toInt())

    println(b1.width*b1.height)
}

test:
input:
100
42

output:
4200

// ----------


class Test{
    var x = 1
    constructor(v: Int){
        x = v - 2
    }
}

fun main(args: Array<String>) {
    val t = Test(8)
    println(t.x) //6
}
*/

fun main() {
    System.out.println("1, 2, 3...")
    print("Line print here ")
    println(42)
    print("Pay attention to ")
    println("syntax")
  }
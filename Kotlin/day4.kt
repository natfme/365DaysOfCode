// Day 4 - 100 Days of Code: Input & Variables
//What language will you study now?

/*
Val variables and mutability
It is important to note that val is not a synonym of immutable. In the following example, we will use a MutableList, which is an ordered set of elements of the same type. If you want to get ahead and learn more about MutableList, you can use the corresponding topic, but it is not a necessity right now.

// list creation
val myMutableList = mutableListOf(1, 2, 3, 4, 5)
// trying to update the list
myMutableList = mutableListOf(1, 2, 3, 4, 5, 6) // error line

It is always possible to change the internal state of a val variable: while it is prohibited to reassign the variable, its content can be modified in some other ways.
Example:
*/

// list creation

fun main() {

    println("Yaaay!")
    val myMutableList = mutableListOf(1, 2, 3, 4, 5)
    //adding a new element
    myMutableList.add(6)   // it works
    //printing the list
    println(myMutableList) // [1, 2, 3, 4, 5, 6]

    val part1: String = "Kotlin "
    val part2 = "is a cross-platform"
    val part3 = ", statically typed, "
    val part4 = "general-purpose programming language with type coercion."

    print(part1)
    print(part2)
    print(part3)
    println(part4)

    val number1: Int = 100
    println(number1)

    // put your code above
    val first = "Name"
    val last = "Last name"
    val age: Int = 100
    println("My name is $first $last and I’m $age years old")
    print("Hasta mañana, muchas gracias")
}

/*
Const variables
In Kotlin, there is also a const modifier, which is used before the val keyword to declare a compile-time constant. The value of a const variable is known at compile time and won't be changed at runtime: 

const val MY_STRING = "This is a constant string"

The following code will give you an error, since the value is unknown before the program execution and it is not a constant:
const val MY_STRING = readln() // not a constant String!!!

There are some restrictions on when the const modifier can be applied. First, it can only be used with a String or a primitive type variable

const val CONST_INT = 127
const val CONST_DOUBLE = 3.14
const val CONST_CHAR = 'c'
const val CONST_STRING = "I am constant"
const val CONST_ARRAY = arrayOf(1, 2, 3) // error: only primitives and strings are allowed

Besides, const variables need to be declared on top level, outside of any functions:

const val MY_INT_1 = 1024 // correct line

fun main() {
    const val MY_INT_2 = 2048 // error: Modifier 'const' is not applicable to 'local variable'
}
*/

//Tipos de variable
/*
val text = "Hello, I am studying Kotlin now."
val n = 1

In this case, Kotlin knows that text is a string and n is a number. Kotlin determines the types of both variables automatically. This mechanism is called type inference.

Please, take a look at the following piece of code. This is how we declare a variable with type inference:

val/var identifier = initialization

You can also specify the type of a variable when declaring it:

val/var identifier: Type = initialization

Let's declare the same variables as in the previous example and specify their types

val text: String = "Hello, I am studying Kotlin now."
val n: Int = 1

val greeting: String // ok
greeting = "hello"

Type mismatch
One of the most important functions of data types is to protect you from assigning an unsuitable value to a variable. Take a look at an example of code that doesn't work:

val n: Int = "abc" // Type mismatch: inferred type is String but Int was expected

So, if you see a type mismatch error, it means you've assigned something unsuitable to a variable. The same problem occurs when you try to assign an unsuitable value to a mutable variable declared with type inference.

var age = 30 // the type is inferred as Int
age = "31 years old" // Type mismatch

Note, you cannot change the type of a variable.

val age: Int = 42  // this is correct for integer type not a String type
Int age = 42  // invalid Kotlin syntax
val age = “42”: String  // invalid syntax, colon, and type should come right after the value name
String age = “42”  // valid in Java but not in Kotlin
var age = 42  // var is used here not val, and age is of type Int, not a String
val age: String = “42”  // correct syntax, although not mandatory we can explicitly declare the type
val age: Char = ‘42’  // '42' is not Char type, in fact, it is not a valid type Kotlin knows about
*/
// Day 2 - 100 Days of Code: Input & Variables
//What language will you study now?

//Tipos de datos--------------------------------
/*
Boolean
Character
String
Array
Number -Byte
       -Short
       -Int
       -Long
       -Double
       -Float

Integer numbers - 0, 1, 100, -3
If an integer value contains a lot of digits, we can add underscores to divide the digits into blocks to make this number more readable: for example, 1_000_000 is much easier to read than 1000000.
ex: 1__000_000

Characters - 
A single character can represent a digit, a letter, or another symbol. To write a single character, we wrap a symbol in single quotes as follows: 'A', 'B', 'C', 'x', 'y', 'z', '0', '1', '2', '9'. Character literals can represent alphabet letters, digits from '0' to '9', whitespaces (' '), or some other symbols (e.g., '$').

Do not confuse characters representing numbers (e.g., '9') and numbers themselves (e.g., 9).

Strings 
Strings represent text information, such as the text of an advertisement, the address of a web page, or the login to a website. A string is a sequence of any individual characters.

To write strings, we wrap characters in double quotes instead of single ones. Here are some valid examples: "text", "I want to learn Kotlin", "123456", "e-mail@gmail.com". So, strings can include letters, digits, whitespaces, and other characters.

A string can also contain just one single character, like "A". Do not confuse it with the character 'A', which is not a string.*/


fun main() {
    println("Hello, World!")
    println("Hello, Kotlin!")
    println("We believe in you!")
    println("Great job, keep at it!")
    println("Not correct, but keep on trying and never give up!")
    println("Amazing, you've got it!")
    println("Your practice is really paying off. Well done!")
    println("Practice makes perfect. Good for you for not giving up easily!")
    println("A \n B \n C")
    println("You're doing great!")

    // val name : data tyoe = initial value

    //a = 123 // Int se usa para almacenar números enteros
    //b= 12.4 // Double y Float se utilizan para almacenar números decimales
    //c = 'Z' // Char representa un carácter
    //d = true //Boolean, tiene sólo dos valores posibles

    val language = "Kotlin"
    println(language) // prints "Kotlin" without quotes   //language es diferente Language - los nombres son case-sensitive

    var dayOfWeek = "Monday"
    println(dayOfWeek) // prints Monday

    dayOfWeek = "Tuesday"
    println(dayOfWeek) // prints Tuesday

    //It is also possible to declare and initialize a variable with the value of another variable

    val cost = 3
    val costOfCoffee = cost
    println(costOfCoffee) // prints 3

    val ten = 10
    val greeting = "Hello"
    val firstLetter = 'A'

    println(ten) // prints 10
    println(greeting) // prints Hello
    println(firstLetter) // prints A

    var number = 10
    number = 11 // ok
}

//Variables
/* What is a variable?
A variable is a storage for a value, which can be a string, a number, or something else. Every variable has a name (or an identifier) to distinguish it from other variables. You can access a value by the name of the variable.

Variables are one of the most often used elements in programs; therefore, it is important to understand how to use them 

Declaring variables
Before you can start using a variable, you must declare it. To declare a variable, Kotlin provides two keywords:

val (for value) declares an immutable variable (just a named value or a constant), which cannot be changed after it has been initialized (this is actually not entirely true, we will discuss this issue in more detail later);
var (for variable) declares a mutable variable, which can be changed (as many times as needed).

There is one restriction for mutable variables (the ones declared with the keyword var), though. When reassigning their values, you can only use new values of the same type as the initial one. So, the piece of code below is not correct

var number = 10
number = 11 // ok
number = "twelve" // an error here!
*/
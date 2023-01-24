import kotlin.text.toDouble
/* 
Standard input
Standard input is a stream of data that goes into the program. It is supported by the operating system. By default, standard input obtains data from the keyboard, but it is also possible to get it from a file.

Not all programs need to use standard input, but still, you're likely to use it quite often. A typical way of solving programming problems goes as follows:

Read data from the standard input;
Process data to obtain a result;
Output the result to the standard output.
Before you start writing programs that do something useful, you need to understand how to read data from the standard input.

Using readln
In Kotlin, to read data from the standard input you can use the function readln(). It reads the whole line as a string:

val line = readln()
The variable line has the type String because the expression readln() returns a value of this type.

If you are working with older versions of the Kotlin language you need to use readLine()!! instead of readln(). These functions do the same thing, but readln() is shorter and preferred, so if you're working with Kotlin 1.6 or higher, use readln().

val line = readLine()!! // before Kotlin 1.6
You are probably a little confused about the exclamation marks. This construction guarantees non-empty input to the compiler. We will talk about it in more detail later.
Here is a simple program that reads a line from the standard input and sends it to the standard output:

fun main() {
    val line = readln()
    println(line)
}
Here is an example of valid input data:

Hello, Kotlin
The output would be the following:

Hello, Kotlin
By default, to see the information about the entered data you need to press Enter.

Now, let's see how you can read different types of data using readln().

toInt() and toLong()
Sometimes we need to get numeric data from the user. For example, suppose we need to get information about the user's age or graduation year. To work with numeric values, use the function toInt(). To convert the input to an integer, use the toInt()function and dot syntax:

println("Print any number: ") 
val number = readln().toInt() 
print("You printed the number: ")
print(number) 
Here is an example of valid input data:

56
The output is:

Print any number: 
56 
You printed the number: 56
In case we need to process a larger number, for example, the cost of a large and luxurious yacht, use the function toLong():

println("How much is your yacht worth?")
val cost = readln().toLong()
print("You printed: ")
print(cost)
The output is:

How much is your yacht worth?
10000000000
You printed: 10000000000

toDouble() and toBoolean()
What if we need to get more accurate values? For example, suppose we need to know the exact price of a liter of gasoline. In this case, we cannot use toInt() or toLong() since likely we won't have a whole number. For this purpose, use the function toDouble():

println("Print any double type number:")
val number = readln().toDouble()
println("You printed the number: ")
print(number)
The output is:

Print any double type number:
0.5673421
You printed the number: 
0.5673421
The same logic works for Boolean: use the function toBoolean():

println("The earth is flat. Print true or false:")
val answer = readln().toBoolean()
print("The earth is flat: ")
print(answer)
The output is:

The earth is flat. Print true or false:
false
The earth is flat: false

Multiple inputs
Is it possible to receive and process multiple inputs? The answer is yes: all we need to do is declare a few different variables, all with the value of the function readln(). If you want to enter several values and their data types are different, then you need to press Enter in order to separate the different types.

Consider an example that illustrates the input and output of multiple values:

val a = readln()
val b = readln().toInt()
val c = readln()
print(a)
print(" ")
print(b)
print(" ")
print(c)
Here is an example of valid String and Int input values:

You earned
100
points!
The output is:

You earned 100 points!
As you can see, getting multiple values of different data types is not difficult. You just need to declare several variables, assign them the desired readln() function, and display them correctly in the console.

Reading multiple values in one line
If you need to read two values in one line, you can use this construction:

val (a, b) = readln().split(" ")
println(a)
println(b)
Here is an example of input data:

Hello, Kotlin
The output would be the following:

Hello,
Kotlin
This construction splits the input string at spaces and stores the words in the variables a and b. We will discuss this in more detail later.

In the same way, you can read up to five values per line:

val (a, b, c, d) = readln().split(" ")
println(a)
println(b)
println(c)
println(d)
Here is an example of input data:

Have a nice Kotlin
The output would be the following:

Have
a
nice
Kotlin

fun main() {
    //val a = readLine()!!
    //val b = readLine()!!.toBoolean()
    //val c = readLine()!!.toInt()
    val d = readLine()!!.toDouble()

    //println(a)
    //println(b)
    //println(c)
    println(d)
}

Suppose you need to read the Int value into the variable n. Correct the code below. Don't write main, just fix the input.

val n: Int = readLine()

Write a program that reads a Double value and prints it out.

val n: Int = readLine()!!.toInt()*/


fun main() {
    val n: Double = readLine()!!.toDouble()
    println(n)
}

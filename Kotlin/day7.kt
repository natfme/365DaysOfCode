//Day7 - Standard input

/*Standard input is a stream of data that is fed to a program. By default, standard input gets data from the keyboard, but it is also possible to get it from a file.

Not every program requires standard input. But we will refer to it quite often. Before we start writing programs that do something useful, you need to understand how to read data from the standard input.

Kotlin has a useful function to read data from the standard input. It is readLine. It reads the whole line as a string

val line = readLine()!!

The line variable is of the String type because the readLine()!! expression returns a value of this type.

Here is a program that reads a line from the standard input and sends it to the standard output:

fun main() {
    val line = readLine()!!
    println(line)
}

If you need to get a number from the input, you can use this construction: val number = readLine()!!.toInt() or val number = readln().toInt()

Often you need to read a few words in a line. A word is separated from other words by one or more delimiters, such as spaces or a new line character.

Java Scanner
Another way to obtain data from the standard input is to use the Java Scanner. You can access it directly from Kotlin because it is interoperable with other Java libraries. Scanner allows a program to read values of different types (strings, numbers, etc) from the standard input.

To use this type, you need to add this import statement to the top of your file with the source code:

import java.util.Scanner

import java.util.*

You can use either method to add Scanner to your program. We will discuss importing in a more detailed way later.

Let's create a variable initialized by Scanner:

val scanner = Scanner(System.`in`)

In this line, System.`in` is an object that represents the standard input stream. The scanner wraps it as an internal data source and provides a set of convenient methods to work with it.

Now we can read data from the standard input:
val line = scanner.nextLine() // read a whole line, i.e. "Hello, Kotlin"
val num = scanner.nextInt()   // read a number, i.e. 123
val string = scanner.next()   // read a string, i.e. "Hello"

Scanner.next() reads only one word, not a line. If the user enters Hello, Kotlin, it will read Hello,.

After you call scanner.nextLine() or scanner.nextInt() or something else, the program will anticipate input data. Here is an example of correct input data:

Hello, Kotlin
123 Hello

It's possible to read a number as a string using scanner.next() or scanner.nextLine() if the number is on a new line.

Also, the Scanner type provides several methods (functions) for reading values of other types. Refer to the Class Scanner documentation for more details.

The program below reads two numbers and outputs them in reverse order on two different lines
*/

/* 
fun main() {
    val line = readLine()!!
    println(line)


    val (a, b) = readLine()!!.split(' ')    // for input "Hello world!" a is "Hello" and b is "world!"
    val (c, d, e) = readLine()!!.split(' ') // can read, for example "Go for it"

    println(a)
    println(b)
    println(c)
    println(d)
    println(e)
}*/

import java.util.Scanner // a class (type) from the Java standard library

fun main() {
    val scanner = Scanner(System.`in`) // reads data

    val num1 = scanner.nextInt() // reads the first number
    val num2 = scanner.nextInt() // reads the second number

    println(num2) // prints the second number
    println(num1) // prints the first number
}
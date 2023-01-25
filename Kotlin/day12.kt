//Day 12 - String templates

/*
Sometimes you need to put values of variables in a text. Lucky for you, Kotlin can help you with that. Meet the string templates. In this topic, we will discuss their purpose.

Suppose we need to display a message about today's temperature in Celsius:

Now, the temperature in ... is ... degrees Celsius.
Instead of ... we need to display certain values.

If we have two variables city and temp, we can build the resulting string with concatenations:

val city = "Paris"
val temp = "24"

println("Now, the temperature in " + city + " is " + temp + " degrees Celsius.")
It is a simple solution. But perfect? No. It's rather awkward.

Kotlin provides a more convenient way to do the same thing using string templates. How do they work? To add a variable value to a string, write the dollar sign $ before a variable name:

val city = "Paris"
val temp = "24"

println("Now, the temperature in $city is $temp degrees Celsius.")
The code becomes more readable. Both code snippets print the same message:

Now, the temperature in Paris is 24 degrees Celsius.
If we do not want to print a string, we can create a variable:

val value = "55"
val currency = "dollars"
val price = "$value $currency" // "55 dollars"
We recommend using string templates to build strings with variable values. Try using it instead of string concatenation.

Templates for expressions------------------------------------------
You can use string templates to put the result of an arbitrary expression in a string. To do that, include the entire expression in curly braces {...} after the dollar sign $. For example:

val language = "Kotlin"
println("$language has ${language.length} letters in the name")
It prints:

Kotlin has 6 letters in the name
Here {language.length} is an expression that will be evaluated. If you skip the braces, it will output something different:

Kotlin has Kotlin.length letters in the name
So, always use curly braces for expressions in string templates to avoid these mistakes. Do not add them if you want to output only a variable value even though it does work.

Idiom---------------------------------------------
Idioms are templates for clear and readable code. These patterns clarify the code for other people, so it is a good idea to use them. All idioms are endorsed by the community, so using them will bring you closer to the genuine Kotlin-style code. You can find an exhaustive list of idioms at Kotlin docs.

The idiom we'll look at is the string interpolation:

val language = "Kotlin"
println("Have a nice $language!")        // nice code
println("Have a nice " + language + "!") // bad practice

What do you need to remember from this topic? There are two main points:

Use string templates to insert variable values into a string: "this string has $value".
If you would like to get an arbitrary expression, use curly braces: "The length is ${str.length}".
*/

//#Solve

/*
You need to write a program that prints dates and times in a special format. Hours, minutes, and seconds are split by a colon, and day, month, and year are split by a slash. Take a look at the examples below.

You can read three numbers in a line this way:

val (a, b, c) = readLine()!!.split(' ')

// or since Kotlin 1.6

val (d, e, f) = readln().split(' ')

Sample Input 1:
23 59 59
12 12 2018

Sample Output 1:
23:59:59 12/12/2018

Sample Input 2:
1 2 3
4 5 2018

Sample Output 2:
1:2:3 4/5/2018


fun main() {
    val (a, b, c) = readLine()!!.split(' ')
    val (d, e, f) = readLine()!!.split(' ')

    println("$a:$b:$c $d/$e/$f")
}
*/

/*
Write a program that reads the String representation of an arbitrary number and outputs a line with this number and its Int representation divided by 2.

Look at the example to understand the output format.

Sample Input 1:
12

Sample Output 1:
The obtained value is 12 and its Int representation after division on 2 is 6


fun main() {
    val num = readLine()!!.toInt()

    val div = num / 2

    println("The obtained value is $num and its Int representation after division on 2 is $div")
}
*/

/*
Write a program that reads two integer numbers and prints them on the same line. The numbers are separated by a space.

Please solve the problem using string templates.

Sample Input 1:
8
11

Sample Output 1:
8 11

Sample Input 2:
-5
0

Sample Output 2:
-5 0
*/

fun main() {
    val num1 = readLine()!!.toInt()
    val num2 = readLine()!!.toInt()

    println("$num1 $num2")
}
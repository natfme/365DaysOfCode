// Day 26 - Arithmetic operations

// The order is the king

// What is the result of this expression: 2 + 4 * 5 - 10 / (2 + 1)?

/* fun main(args: Array<String>) {
    print(2 + 4 * 5 - 10 / (2 + 1))
}

// For loop and ranges -----------------------------------------------------------------------------------------------------------

For loop
Kotlin provides the for loop to iterate through ranges, arrays, and other collections of elements. We will meet them later.

This is the syntax the for loop has:

for (element in source) {
    // body of loop
}

The body of this loop consists of one or more statements that are executed for each element from the specified source. The loop stops after having processed the last element.

Iterating through a range
The simplest example of using the for loop is printing each element of an integer range.

for (i in 1..4) {
    println(i)    
}
This loop prints each number from 1 to 4.

1
2
3
4
It is also possible to iterate through a range of characters:

for (ch in 'a'..'c') {
    println(ch)
}
This loop prints:

a
b
c
Note that we cannot use a string range such as "da".."dd" to get the desired result "da" "db" "dc" "dd". In the range, we can only use single characters. From now on, all the examples will be about numbers because iterating through characters is always the same.

----------------------------------------------------------------------------------------------------------------------------------------

Iterating through a String
Also, you may iterate over strings. The following code prints each symbol of a String:

val str = "Hello!"
for (ch in str) {
    println(ch)    
}
This code prints:

H
e
l
l
o
!

----------------------------------------------------------------------------------------------------------------------------------------

Iterating in the backward order
You can also iterate a range in the backward order.

for (i in 4 downTo 1) {
    println(i)
}
This loop prints numbers from 4 to 1.

4
3
2
1
Note that it is required to use in 4 downTo 1, not in 4..1, to iterate the range in reverse order.

----------------------------------------------------------------------------------------------------------------------------------------

Excluding the upper limit
If we need to exclude the upper limit from a range, we can subtract one from it or write until instead of ..:

for (i in 1 until 4) {
    println(i)
}
This loop prints numbers from 1 to 3.

----------------------------------------------------------------------------------------------------------------------------------------

Specifying a step
If we do not specify a step, it is assumed that the step is equal to one (e.g. 1, 2, 3, ...). Although if we want to change the step, we need to specify it explicitly.

In the example below, we print only odd numbers from the range 1..7.

for (i in 1..7 step 2) {
    println(i)
}
This loop prints four numbers:

1
3
5
7
You can also use it for backward iteration.

for (i in 7 downTo 1 step 2) {
    println(i)
}
This loop prints:

7
5
3
1

----------------------------------------------------------------------------------------------------------------------------------------

An example: the factorial of a number
Let's write a program that calculates the factorial of a given integer number. It's a classic. The factorial of n is a product of integer numbers from 1 to n inclusive. Assumed that factorial of 0 is 1. The factorial of 1 is 1 as well.

fun main() {
    val n = readln().toInt()
    var result = 1 // starting value of the factorial

    for (i in 2..n) { // the product from 2 to n
        result *= i
    }

    println(result)
}
The program above reads an integer number from the standard input. We suppose that the starting value of the factorial is 1 and then sequentially multiply it by numbers from 2 to n. If the input number is 1, the result is 1. If the input number is 5, the result is 120.

----------------------------------------------------------------------------------------------------------------------------------------

An example: the multiplication table of even numbers
You can nest one for loop in the body of another for loop because loops are just regular statements. Programmers often use nested loops to process multidimensional structures like tables (matrices), data cubes, and so on.

For example, the code below prints the multiplication table of even numbers from 2 to 10.

fun main() {
    for (i in 2..10 step 2) {
        for (j in 2..10 step 2) {
            print(i * j)
            print('\t')  // print the product of i and j followed by one tab
        }
        println()
    }
}
It prints:

4   8   12  16  20  
8   16  24  32  40  
12  24  36  48  60  
16  32  48  64  80  
20  40  60  80  100

----------------------------------------------------------------------------------------------------------------------------------------

Idiom
Almost everything in this topic is an idiom! Different types of ranges may be difficult to understand, but they offer a really convenient and easy-to-read way to write code. Here we give you a quick reminder of the syntax for iterating over basic ranges:

for (i in 1..6) { ... }        // closed range: 1, 2, 3, 4, 5, 6
for (i in 1 until 6) { ... }   // half-open range: 1, 2, 3, 4, 5
for (x in 1..6 step 2) { ... } // step 2: 1, 3, 5
for (x in 6 downTo 1) { ... }  // closed range, backward order: 6, 5, 4, 3, 2, 1 

----------------------------------------------------------------------------------------------------------------------------------------
 */
// Practice 1

/*The sum of integers from a to b

Read two integers a and b. Print the sum of all the integers from a tob inclusive. It is guaranteed that a <b.

Sample Input 1:
6
15

Sample Output 1:
105

fun main() {
    // put your code here
    val a = readLine()!!.toInt()
    val b = readLine()!!.toInt()
    var sum = 0

    if (a < b) {
        for (i in a..b) {
            sum += i
        }
        println(sum)
    }
}
*/

// Practice 2 

/*
The roots of equation

There are numbers a, b, c, d. Output in ascending order all the integers between 0 ans 1000 (inclusively), which are the roots of the equation ax^3+bx^2+cx+d=0. The roots of a quadratic equation are the values of the variable that satisfy the equation.

If a specified interval does not contain any roots of the equation, do not output anything.

Detalles
You can just iterate over x from 0 to 1000 and check the value of the expression.

Sample Input 1:
-1
1
-1
1

Sample Output 1:
1

Sample Input 2:
0
1
-6
5

Sample Output 2:
1
5

Sample Input 3:
1
1
1
1

Sample Output 3:


// Solution
const val END_RANGE = 1000

fun main() {
    // put your code here
    val a = readLine()!!.toInt()
    val b = readLine()!!.toInt()
    val c = readLine()!!.toInt()
    val d = readLine()!!.toInt()

    for (i in 0..END_RANGE) {
        val x = a * i * i * i + b * i * i + c * i + d

        if (x == 0) {
            println(i)
        }
    }

Otra solución para analizar

fun main() = Array(4) { readLine()!!.toInt() }.let { 
    for (i in 1..1000) { if (it[0] * i * i * i + it[1] * i * i + it[2] * i + it[3] == 0) println(i) } }
*/
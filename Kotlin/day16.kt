// Day 16 - Relational operators

/*
List of relational operators
Kotlin provides six relational operators to work with numbers:

== — equal to X
!= — not equal to X
> — greater than X
>= — greater than or equal to X
< — less than X
<= — less than or equal to X
A relational operator results in a Boolean value (true or false) regardless of the operand type.

Comparing integer numbers
Relational operators allow you to compare two integer numbers, among other things. Here are some examples:

val one = 1
val two = 2
val three = 3
val four = 4

val oneIsOne = one == one // true

val res1 = two <= three // true
val res2 = two != four  // true
val res3 = two > four   // false
val res4 = one == three // false
You can use relational operators together with arithmetic operators. In these expressions, relational operators have a lower priority than arithmetic operators.

Let's take a look at the example below. First, Kotlin calculates two sums, and after that, they are compared with the > operator:

val number = 1000
val result = number + 10 > number + 9 // 1010 > 1009 is true
The result is true.

Note that you cannot check the equality of Int and Long! You can compare Int and Long freely with >, <. >=, <=, but cannot use == and !=. You can check equality only for the same types, so you need to convert Int to Long:

val one: Long = 1
val zero: Int = 0

println(one >= zero)          // OK, prints true  
// println(one == zero)          Error
println(one == zero.toLong()) // OK, prints false

Joining relational operations
Kotlin cannot process expressions like:

a <= b <= c
You should join two Boolean expressions using logical operators like || and && instead.

For example, let's say we need to check the validity of the following expression:

100 < number < 200
To do that, we should write something like this:

number > 100 && number < 200
Also, we can put different parts of the expression in the parentheses:

(number > 100) && (number < 200)
The parentheses are not necessary, though, as relational operators have a higher priority.

Logical operators allow you to join a sequence of relational operations to a single expression. This is a widely used trick in programming.

As a more complex example, let's write a program that reads an integer number and checks whether a number belongs to the following range — [100; 200] including 100 and 200:

fun main() {
    val left = 100
    val right = 200
    val number = readln().toInt()

    val inRange = number >= left && number <= right // joining two expressions using AND

    println(inRange)
}
You can have something like this:

50 is false;
99 is false;
100 is true;
200 is true, and so on.
*/

// Practice

/*
Write a program that reads three numbers and checks if they are different (numbers are not equal to one another).

Output either true or false.

Sample Input 1:

5
5
9
Sample Output 1:

false
Sample Input 2:

1
2
3
Sample Output 2:

true


fun main() {
    val num1 = readLine()!!.toInt()
    val num2 = readLine()!!.toInt()
    val num3 = readLine()!!.toInt()

    val answer = num1 == num2 || num1 == num3 || num2 == num3

    println(!answer)
}
*/

/*
Write a program that reads a value and checks whether this value is less than 10.

Sample Input 1:

5
Sample Output 1:

true
Sample Input 2:

11
Sample Output 2:

false


fun main() {
    val num = readLine()!!.toInt()

    println(num < 10)
}

Write a program that reads a value and checks whether it is less than 10 but greater than 0.

Sample Input 1:

0
Sample Output 1:

false
*/

/*
fun main() {
    val num = readLine()!!.toInt()

    println(num < 10 && num > 0)
}
*/

fun main() {
    val num = readLine()!!.toInt()

    val intRange = num in 1..9
    println(intRange)
}
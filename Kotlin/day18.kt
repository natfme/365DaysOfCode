// Day 18 - if expresion - ciclos While y Do while

/*
If expression

The conditional expression (if expression for short) is a construction that allows a program to perform different computations depending on the value of a boolean expression. If it is true, the program performs one action. If it is false , the program performs another action. Here you can see some examples of boolean expressions: a > b, i - j == 1 and so on.

The conditional expression has a number of forms. Let's take a look at them.

The single if-case
The simplest form consists of the keyword if, a boolean expression (condition), and a body enclosed in curly braces.

if (expression) {
    // body: do something
}
If the expression is true the action with statements inside the code block is executed, otherwise, the program skips them.

For example, this code prints "Very experienced person" if the value of age is greater than 100.

val age = ... // an integer value
if (age > 100) {
    println("Very experienced person")
}

// other lines of code
In this example, if the age is greater than 100 the code prints "Very experienced person", otherwise, it does nothing. After this, other lines of code are executed.

If a condition is false, actions in the body will not be executed:

if (3 == 4) {
    println("3 is 4")
}
In the code above the boolean expression 3 == 4 is false, so the body is skipped.

Sometimes you will see a situation when the expression in a condition is a single variable of the Boolean type. Instead of writing b == true or b == false, use this variable (or its negation with !) as the boolean expression:

val b = ... // it is true or false (Boolean)
if (b) { // or !b
    // do something
}
You can use this construction in any place in a program where using of a conditional statement is expected. You can even nest it inside another conditional statement to perform multistage checks.

The if-else-cases --------------------------------------------------
The expression we've seen above can be extended with the keyword else and another body to do alternative actions when the expression is false.

if (expression) {    
    // do something
} else {
    // do something else
}
In this case, if the expression is true then the first code block is executed, otherwise, the second code block is executed. Note that the situation when they both are executed is impossible.

Let's take a look at the example below. The program outputs different text depending on the value of num (even or odd). A number is considered as even if it is divisible by 2 otherwise it's odd.

val num = ... // the num is initialized by some value (Int)

if (num % 2 == 0) {
    println("It's an even number")
} else {    
    println("It's an odd number")
}
Since a number can be either even or odd, only one message will be displayed. If num is 10, the program outputs "It's an even number". If the value is 11, it outputs "It's an odd number".

The if-else-if-cases ---------------------------------------------------------------------------------
The most usual form of the conditional statement consists of several conditions and else-branches.

if (expression0) {
    // do something
} else if (expression1) {
    // do something else 1
// ...
} else if (expressionN) {
    // do something else N
}
This code outputs recommendations on what computer you need to buy depending on your budget.

val dollars = ... // your budget (Int)

if (dollars < 1000) {
    println("Buy a laptop")
} else if (dollars < 2000) {
    println("Buy a personal computer")
} else if (dollars < 100_000) {
    println("Buy a server")
} else {
    println("Buy a data center or a quantum computer")
}
This conditional expression has four branches: dollars < 1000, dollars < 2000, dollars < 100_000 and dollars >= 100_000. If the value of dollars is 10_000, it prints "Buy a server".

Nested If's --------------------------------------------------------------
As we said before, you can nest one if expression into the body of another one. For example:

if (n % 2 == 0) {
    if (n % 3 == 0) {
        println("The number can be divided by 6")
    } else {
        println("The number can be divided by 2")
    }
} else {
    println("The number cannot be divided by 2")
}
This code tests if the value is divisible by 2 and, if it is true, tests if the value is divisible by 3. If it is also true, it means the value is divisible by 6.

Condition is an expression -----------------------------------------------------------------------
Unlike other languages (such as Java, Python, C#), in Kotlin if is an expression, not a statement. As a regular expression, it can return a value (result) of computations. The result must be the last expression in a body.

This code finds the max of two integer numbers a and b. It prints the choice and stores the result to the max variable.

val max = if (a > b) {
    println("Choose a")
    a
} else {
    println("Choose b")
    b
}
If you are going to use the if as an expression, it must have an else branch.

In an expression-style if, it's better to produce results of the same type in all the branches because in this case, the type of the variable will be strict. However, in general, it's not required. Later, you will learn how to work with variables of an unknown type.
If all the bodies contain only a single statement, you can skip braces:

val max = if (a > b) a else b
Sometimes we even do NOT need to declare a new variable for storing a result. In this example, we compare two numbers and print the text information passing it to a function.

fun main() {
    val a = readln().toInt()
    val b = readln().toInt()

    println(if (a == b) {
        "a equal b"
    } else if (a > b) {
        "a is greater than b"
    } else {
        "a is less than b"
    })
}

Idiom --------------------------------------------------------
It's time for the next idiom! Now we draw your attention to the expression-style if. You should prefer to use this form when you need to get some results. Of course, you may work with if as a statement, but using if as an expression is a better way. For example:

val max = if (a > b) a else b // one line

...

var max = a // try to avoid var if possible
if (b > a) max = b
The second snippet may cause some trouble, for example, you may accidentally alter the value of the max variable or forget to change it. So we suggest you use expression-style if in those cases.
*/

/*
val x = 11

if (x * 2 + 1 < 23 && x % 2 == 1) {
    print("1")
    print(if (x == 11) "2" else "3")
} else if (x != 0) {
    print("4")
}
print("5")

answer 45

Odd or even

Write a program that reads a number and prints EVEN if it is even. Otherwise, the program should print ODD.

Sample Input 1:

5
Sample Output 1:

ODD
Sample Input 2:

-5
Sample Output 2:

ODD

fun main() {
    // write your code here
    val num1 = readLine()!!.toInt()

    if (num1 % 2 != 0) {
        println("ODD")
    } else {
        println("EVEN")
    }
}
*/

/*
Practice 3

There is an integer as input. Output True if its value is within the interval 
(
−
15
,
12
]
∪
(
14
,
17
)
∪
[
19
,
+
∞
)
(−15,12]∪(14,17)∪[19,+∞)
, otherwise print False (case sensitive).

Please note the different brackets, which are used to specify intervals. The problem uses semi-open and open intervals. You can read more about them in the Wikipedia.

The union sign means a union of intervals. A shortlist of intervals:

Sample Input 1:

20
Sample Output 1:

True
Sample Input 2:

-20
Sample Output 2:

False

fun main() {
    // write your code here
    val num = readLine()!!.toInt()

    if (num in -14..12 || num in 15..16 || num >= 19) {
        println("True")
    } else {
        println("False")
    }
}
*/

/*
Practice 4

Write a program that uses if to find the max of two integer numbers. These numbers can be positive, negative or zero.

Be creative, solve the problem without else branch :)

Use the provided code template, print the max.

Sample Input 1:

8
11
Sample Output 1:

11

fun main() {

    val a = readLine()!!.toInt()
    val b = readLine()!!.toInt()

    // put your code here
    if (a > b) {
        println(a)
    }
    if (a < b) {
        println(b)
    }
    if (a == b) {
        println(a)
    }
}
*/

/*
Healthy sleep

Ann watched a TV program about health and learned that she should sleep at least 
�
A
 hours per day, but oversleeping is also not healthy and you should not sleep more than 
�
B
 hours. Now Ann sleeps 
�
H
 hours per day. If Ann's sleep schedule complies with the requirements of that TV program – print "Normal". If Ann sleeps less than 
�
A
 hours, output “Deficiency”, if she sleeps more than 
�
B
 hours, output “Excess”.

Input to this program are the three strings with variables in the following order: 
�
A
, 
�
B
, 
�
H
. 
�
A
 is always less than or equal to 
�
B
.

Please note letters case: the output should exactly correspond to what required in the problem, i.e. if the program has to output "Excess", such output as "excess", "EXCESS", "ExCeSs" and others will not be considered correct.

You should think carefully about all the conditions, which you need to use. A special attention should be paid to the strictness of the conditional operators used: distinguish between 
<
<
 and 
≤
≤
; 
>
>
 and 
≥
≥
. In order to understand which ones to use, read carefully the problem statement.


Sample Input 1:

6
10
8
Sample Output 1:

Normal
Sample Input 2:

7
9
10
Sample Output 2:

Excess
Sample Input 3:

7
9
2
Sample Output 3:

Deficiency

*/

fun main() {    
    // write your code here
    val hoursA = readLine()!!.toInt() // She should sleep at least A hours per day
    val hoursB = readLine()!!.toInt() // Oversleeping is also not healthy and you should not sleep more than B hours
    val hoursH = readLine()!!.toInt() // Anna sleeps H hours

    if (hoursH < hoursA) {
        println("Deficiency")
    } else if (hoursH > hoursB) {
        println("Excess")
    } else {
        println("Normal")
    }
}
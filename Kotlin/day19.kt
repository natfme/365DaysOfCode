// Day 19 - Repeating blocks

/*
Repeat loop
To use the simplest loop, write repeat(n) and a sequence of statements in curly braces {...}. n is an integer that determines how many times these statements are going to be repeated.

repeat(n) {
    // statements
}
For example, the program below prints Hello three times:

fun main() {
    repeat(3) {
        println("Hello")
    }
}
Output:

Hello
Hello
Hello

Hint: If n is zero or a negative number, Kotlin will ignore the loop. If n is one, the statements will be executed only once.

Kotlin has the opportunity to control the current iteration with the it name:

fun main() {
    repeat(3) {
        println(it)
    }
}
Output:

0
1
2
The code in parentheses is commonly called a "lambda expression". It's a function that doesn't have name and is passed immediately as an expression. You can find more information about lambdas here.

Reading and processing data in a loop ------------------------------------------------------------------
You can read data from the standard input, declare variables and even perform calculations inside the repeat statement.

Take a look at this example. The program below reads numbers from the standard input and calculates their sum. The first number is not a part of the sum, it determines the length of the input sequence.

fun main() {
    val n = readln().toInt()
    var sum = 0

    repeat(n) {
        val next = readln().toInt()
        sum += next
    }

    println(sum)
}
This code reads a length of a number sequence and assigns it to the n variable. After that, it creates a variable to store the total sum. The code reads the next number and adds it to the sum exactly n times. Then, the loop stops, and the program prints the total sum.

Here is an example of input numbers:

5
40
15
30
25
50
Output:

160
*/

/*
fun main() {
    repeat(3) {
        println("Hello")
    }
}


fun main() {
    repeat(4) {
        println(it)
    }
}

fun main() {
    val n = readLine()!!.toInt()
    var sum = 0

    repeat(n) {
        val next = readLine()!!.toInt()
        sum += next
    }

    println(sum)
}
*/

// Decrement in loops

/*
What does this code print?

fun main() {
    var number = 5

    repeat(2) {
        number--
    }
    println(number)

    repeat(0) {
        number--
    }
    println(number)

    repeat(1) {
        number--
    }

    println(number)
}
*/

/*
How many times it repeats

Take a look at the code:

repeat(5) {
    println("Kotlin")
}

Practice 3
Repeat by value

Write a program that reads a number and prints it the number of times corresponding to the value of the input number.

Sample Input 1:
5

Sample Output 1:
55555

Sample Input 2:
10

Sample Output 2:
10101010101010101010

fun main() {
    // write your code here

    val num = readLine()!!.toInt()

    repeat(num) {
        print(num)
    }

}
*/

// Grades

/*
Find how many "D", "C", "B" and "A" grades the students have got after the last Computer Science test. There are n students in the class. The program gets the n number as input and then gets the grades one by one. The program should output four numbers in a single line, representing the grades from "D" to "A".

Numbers represent the following grades: 2 is "D", 3 is "C", 4 is "B", and 5 is "A".


ample Input 1:

12
5
2
5
3
5
4
2
2
3
4
2
3
Sample Output 1:

4 3 2 3
*/

/*
Failed test #1 of 10. Wrong answer

This is a sample test from the problem statement!

Test input:
12
5
2
5
3
5
4
2
2
3
4
2
3

Correct output:
4 3 2 3

Your code output:
7 2 3 0
*/

/*

fun main() {
    // put your code here
    val numStudent = readLine()!!.toInt()
    var counterA = 1
    var counterB = 1
    var counterC = -1
    var counterD = -1

    repeat(numStudent) {
        val grade = readLine()!!.toInt()

        if (grade == 5) {
            //A
            counterA++
        } else if (grade == 4) {
            //B
            counterB++
        } else if (grade == 3) {
            //C
            counterC++
        } else if (grade == 2) {
            //D
            counterD++
        } else {
            //F
        }
    }
    println("$counterA $counterB $counterC $counterD")
}

fun main() {
    // put your code here
    val numStudent = readLine()!!.toInt()
    var counterA = 0
        var counterB = 0
        var counterC = 0
        var counterD = 0

    repeat(numStudent) {
        val grade = readLine()!!.toInt()
        

        when (grade) {
            5 -> counterA += 1
            4 -> counterB += 1
            3 -> counterC += 1
            2 -> counterD += 1
            // 'else' is not required because all cases are covered
        }
    }
    // Representing the grades from "D" to "A"
    println("$counterD $counterC $counterB $counterA")
}

fun main() {
    // put your code here
    val numStudent = readLine()!!.toInt()
    var counterA = 0
    var counterB = 0
    var counterC = 0
    var counterD = 0

    repeat(numStudent) {

        when (readLine()!!.toInt()) {
            5 -> counterA += 1
            4 -> counterB += 1
            3 -> counterC += 1
            2 -> counterD += 1
            // 'else' is not required because all cases are covered
        }
    }
    // Representing the grades from "D" to "A"
    println("$counterD $counterC $counterB $counterA")
}
*/

// Maximum element divisible by 4

/*
You have a sequence of natural numbers that do not exceed 30000. Find the maximum element in the sequence divisible by 4. As input, the program first gets the number of elements in the sequence, and then the elements themselves. A sequence always has an element divisible by 4. The number of elements does not exceed 1000. The program should print a single number — the maximum sequence element (number) divisible by 4.

Sample Input 1:
6
24
12
47
36
16
46

Sample Output 1:
36

Hint: 1) Initialize two scanner.nextInt() variable, one outside the loop for getting the number of iterations and one inside the loop for scanning each element.
2) Initialize a temporary variable using "var".
3) You can use (input % 4 == 0 && input > max) with if statement for getting the the max value and assigning it to the temporary variable.

import java.util.*

fun main(args: Array<String>) {
    val scanner = Scanner(System.`in`)
    val loop = scanner.nextInt()
    var maximum = 0
    repeat(loop) {
        val value = scanner.nextInt()
        if (value % 4 == 0 && value > maximum) {
            maximum = value
        }
    }
    println(maximum)  
}
*/

/*
fun main() {
    var maximum = 0
    repeat(readLine()!!.toInt()) {
        val input = readLine()!!.toInt()
        if (input % 4 == 0 && input > maximum) maximum = input
    }
    print(maximum)
}
*/

//Counting positive numbers

/*
Write a program that reads a sequence and prints how many positive numbers it contains.

The first number is the length of the sequence. Other numbers are the elements of this sequence.

Sample Input 1:
8
2
3
0
7
4
-2
-3
0

Sample Output 1:
4

fun main() {
    // put your code here
    var counter = 0
    val n = readLine()!!.toInt()

    repeat(n) {
        val num = readLine()!!.toInt()
        if (num > 0) {
            counter += 1
        }
    }
    println(counter)
}
*/

// Kotlin x5

/*
Write a program that prints the word Kotlin five times. Print each word on a new line.

Use the provided template for your solutions:

Sample Output

Kotlin
Kotlin
Kotlin
Kotlin
Kotlin

fun main() {
    repeat(5) {
        println("Kotlin")
    }
}
*/

// Print a string exactly ten times

/*
Write a program that reads a line and then prints it 10 times, each on a new line. A line may include multiple words separated by spaces.

Sample Input 1:

I will not use copy-paste!
Sample Output 1:

I will not use copy-paste!
I will not use copy-paste!
I will not use copy-paste!
I will not use copy-paste!
I will not use copy-paste!
I will not use copy-paste!
I will not use copy-paste!
I will not use copy-paste!
I will not use copy-paste!
I will not use copy-paste!


fun main() {
    // put your code here
    val frase = readLine()!!.toString()

    repeat(10) {
        println(frase)
    }
}
*/

// Size of parts

/*
A detecting device compares the size of components produced by a machine against the reference component.

If the size of the component is larger, it can be fixed; the detector prints 1.
If the size of the component is smaller, it is deemed as a rejection; the detector prints -1.
If the component is perfect, it is sent to the box; the detector prints 0.

Write a program which takes n (the number of parts) as input and then the detector sequence. The program should output three numbers in a single line — the number of perfect components, the number of larger components, and the number of rejections.

Sample Input 1:
10
-1
-1
0
1
-1
-1
1
0
1
0

Sample Output 1:
3 3 4

fun main() {
    // put your code here
    val n = readLine()!!.toInt()
    var counterLarger = 0
    var counterSmaller = 0
    var counterPerfect = 0

    repeat(n) {
        when (readLine()!!.toInt()) {
            -1 -> counterSmaller += 1
            0 -> counterPerfect += 1
            1 -> counterLarger += 1
            // 'else' is not required because all cases are covered
        }
    }
    println("$counterPerfect $counterLarger $counterSmaller")
}
*/

// Time difference

/*
We are going to consider two moments in time that happened on the same day — hours, minutes, and seconds. It is known that the second moment happened not earlier than the first one. Find how many seconds passed between the two moments.

Input data format

The program receives three integers: hours, minutes, seconds of the first moment, and three integers of the second moment.

Output data format

Output the number of seconds between these two moments.

Sample Input 1:
1
1
1
2
2
2

Sample Output 1:
3661

Sample Input 2:
1
2
30
1
3
20

Sample Output 2:
50
*/

const val HOURS_SECONDS = 3600
const val MINUTES_SECONDS = 60

fun main() {
    // put your code here
    val hours1 = readLine()!!.toInt()
    val minutes1 = readLine()!!.toInt()
    val seconds1 = readLine()!!.toInt()
    val hours2 = readLine()!!.toInt()
    val minutes2 = readLine()!!.toInt()
    val seconds2 = readLine()!!.toInt()

    /*val total = (hours2 - hours1) * 3600 + (minutes2 - minutes1) * 60 + seconds2 - seconds1 // MagicNumber: This expression contains a magic number. Consider defining it to a well named constant.
    fix it */
    val total = (hours2 - hours1) * HOURS_SECONDS + (minutes2 - minutes1) * MINUTES_SECONDS + seconds2 - seconds1
    println(total)
}
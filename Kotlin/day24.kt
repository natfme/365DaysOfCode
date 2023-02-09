// day 24 - Ranges

// val within = a <= c && c <= b

// This code works well. However, Kotlin provides a more convenient way to do the same thing using ranges:

// val within = c in a..b

/*
Here, a..b is a range of numbers from a to b (including both border values), in is a special keyword that is used to check whether a value is within a range. Later you will see that this keyword can be used with other types as well.

The value of within is true if c belongs to the range inclusively, otherwise, it is false.

Here are some examples:

println(5 in 5..15)  // true
println(12 in 5..15) // true
println(15 in 5..15) // true
println(20 in 5..15) // false

If you need to exclude the right border, you may subtract 1 from it:

val withinExclRight = c in a..b - 1 // a <= c && c < b
If you need to check that a value is not within a range, just add ! (not) before in.

val notWithin = 100 !in 10..99 // true
You may combine ranges using standard logical operators. The code below checks if c is within one of three ranges.

val within = c in 5..10 || c in 20..30 || c in 40..50 // true if c is within at least one range
You can assign a range to a variable and use it later.

val range = 100..200
println(300 in range) // false
In addition to integer ranges, you can also use ranges of characters and even strings (according to dictionary order).

println('b' in 'a'..'c') // true
println('k' in 'a'..'e') // false

println("hello" in "he".."hi") // true
println("abc" in "aab".."aac") // false
This is enough to understand ranges for integer numbers and characters. We won't cover other type ranges here.
*/

// Practice 1 -Not in range

/*  Read an Int number. Write a program that prints false if this number is between 1 and 10 (inclusive), and true otherwise.

fun main(args: Array<String>) {
    val num = readLine()!!.toInt()

    if (num in 1..10) {
        println(false)
    } else {
        println(true)
    }
}

*/

// Practice 2 - Working hours

/*
The car wash works from 9 to 18 (we use a 24-hour clock format), and from 13 to 14, its employees take lunch to refuel and recharge for further work.
As input, our program reads an integer, a positive number from the console, which is the desired time to make a reservation at the car wash, and checks whether the entered time is within the working hours.

If the time is within the range of working hours, return true, but if the time is during lunch or outside the working hours, return false.

Sample Input 1:
10

Sample Output 1:
true

Sample Input 2:
23

Sample Output 2:
false

val time = readln().toInt()
    val workTime = 9..18
    val lunchTime = 13..14
    // do not change the code above
    // put your code here

const val WORK_START = 9  //Solución para los warning -> This expression contains a magic number. Consider defining it to a well named constant
const val WORK_END = 18
const val LUNCH_START = 13
const val LUNCH_END = 14

fun main() {
    val time = readLine()!!.toInt()
    val workTime = WORK_START..WORK_END
    val lunchTime = LUNCH_START..LUNCH_END
    // do not change the code above
    // put your code here
    println(time in workTime && time !in lunchTime)
}
*/

// Practice 3 - Job

/*
Julia wants to get a job. By the laws of the country she lives in, she can have a job only if her age is within 18 to 59 years inclusive.

Depending on the input age, output true if she can get a job, otherwise output false.

Sample Input 1:
25

Sample Output 1:
true

Sample Input 2:
16

Sample Output 2:
false

const val AGE_START_JOB = 18
const val AGE_END_JOB = 59

fun main() {
    // write your code here
    val age = readLine()!!.toInt()
    println(age in AGE_START_JOB..AGE_END_JOB)
}
*/

// Practice 4 - At least one

/*
Write a program that reads five integer numbers. The first and the second numbers create one range, and the third and the fourth ones create another range. Output true if the fifth number is in at least one of these ranges, otherwise output false.

Sample Input 1:
1
2
5
6
2

Sample Output 1:
true

Sample Input 2:
0
5
6
8
10

Sample Output 2:
false

fun main() {
    // write your code here
    val numStartRange1 = readLine()!!.toInt()
    val numEndRange1 = readLine()!!.toInt()
    val numStartRange2 = readLine()!!.toInt()
    val numEndRange2 = readLine()!!.toInt()
    val num = readLine()!!.toInt()

    println(num in numStartRange1..numEndRange1 || num in numStartRange2..numEndRange2)
}
*/
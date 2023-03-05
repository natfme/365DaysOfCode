// Day 31

/*Let's make a simple converter that converts values to the following three types – Int, Double, and Boolean.

Your program should read a value and print the result of its conversion to Int, Double, and Boolean types sequentially.

Input: value: String.

Output: Int, Double, and Boolean values (each on a new line).*/

fun main() {
    // write your code here
    val num = readLine()!!

    println(num.toInt())
    println(num.toDouble())
    println(num.toBoolean())

}
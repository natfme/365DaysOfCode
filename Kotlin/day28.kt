// Day 28 - Relational operators

/*
Inbetween

Write a program that reads three integer numbers and prints true if the first number lies between the second and third one (inclusive). Otherwise, it is to print false.

The sorting order of the two last arguments can be any.

Sample Input 1:
3
3
3

Sample Output 1:
true

Sample Input 2:
40
30
50

Sample Output 2:
true

Sample Input 3:
40
100
20

Sample Output 3:
true
*/

fun main() {
    val numx = readLine()!!.toInt()
    val num1 = readLine()!!.toInt()
    val num2 = readLine()!!.toInt()

    if (numx in num1..num2 || numx in num2..num1) {
        println(true)
    } else {
        println(false)
    }
}
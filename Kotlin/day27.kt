

import kotlin.collections.mutableListOf// Day27 - For loop and ranges

/* The product of numbers from a to b
Write a program that prints the product of all the integer numbers from a to b (a < b).

Include a and exclude b from your calculation.

The result can be large, so you should use the Long type.

Sample Input 1:
1
2

Sample Output 1:
1

Sample Input 2:
100
105

Sample Output 2:
11035502400

fun main() {
    val a = readLine()!!.toLong()
    val b = readLine()!!.toLong()
    var resultado: Long = 1

    if (a < b) {
        for (i in a until b) {
            resultado *= i
        }
        println(resultado)
    }
}
*/

// Practice 2

/*
The longest sequence
Write a program that reads N numbers and outputs the length of the longest sequence in non-descending order. By non-descending, we mean that the next element is either equal or greater than the previous one (A<=B). Elements of the sequence are to follow one another.

Input format

The first line contains the positive integer number N (N>0).
The other lines contain N numbers.

Example

The input array is 1 2 4 1 2 2 5 7 4 3. In this case, the length of the longest sequence in non-descending order is 5. It includes these elements: 1 2 2 5 7.

Sample Input 1:
10
1
2
4
1
2
2
5
7
4
3

Sample Output 1:
5

fun sum(a: Int, b: Int): Int = a + b
*/

fun main() {
    // write your code here
    val n = readLine()!!.toInt()
    var sum = 0
    var numbers = MutableList(n) { readLine()!!.toInt() }
    
    var num1 = numbers[0]
    for (i in 1..numbers.size-1){
         var num2 =numbers[i]

        if (num1 <= num2) {
            sum += 1
        } else {
            var sumaAct =sum
        }

        if ()

        num1 = num2
        
        }
}



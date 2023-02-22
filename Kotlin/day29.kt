

import kotlin.math.min// Day29 - The classification of basic types

// Size, min and max

// Create a program that prints the size (in bits) and the min and max values of the Int type. Output each value on a new line.

/* Here is an example of output with the Byte type:
8
-128
127
*/

fun main() {
    println(Byte.SIZE_BITS)
    println(Byte.MIN_VALUE)
    println(Byte.MAX_VALUE)

    println(Integer.SIZE)
    println(Integer.MIN_VALUE)
    println(Integer.MAX_VALUE)

    listOf(Int.SIZE_BITS, Int.MIN_VALUE, Int.MAX_VALUE).forEach { println(it) }
}

//val (a, b) = Array(2) { readLine()!!.toInt() }
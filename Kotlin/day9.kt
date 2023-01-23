//Day 9 - type covertion

/*Conversion between numeric types
There are three most common numeric types: Int, Long, and Double. Sometimes, you may need to assign a value of one numeric type to a variable of another numeric type. In this case, you need to carry out type conversion by invoking a special function, for example, toInt(), toLong(), toDouble(), and so on.

Imagine, you have a variable called num, which is of the Int type. You want to pass this variable to a function called sqrt (you can read more about this function and how to use it here) that finds the square root of a number. This function requires a Double value rather than Int, so you need to convert it using toDouble() to prevent a type mismatch error.

val num: Int = 100

val res: Double = sqrt(num.toDouble())
println(res) // 10.0

println(num) // 100, it is not modified

n the example above, the variable types are specified to simplify the explanation.


toDouble() does not modify the type of the variable. This function produces a new value of the Double type.
It's possible to perform these operations even when the target type is larger than the source type. So it means that we can convert Int to Long. It distinguishes Kotlin from other programming languages like Java and C#. They allow assigning numbers of a smaller type to variables of a larger type without extra actions.

val num: Int = 100
val bigNum: Long = num.toLong() // 100
Char is not a numeric type, but you can convert a number to a character and vice versa according to the character code. You can take a look at the code in the Unicode table. This code is basically an integer number.

val n1: Int = 125
val ch: Char = n1.toChar() // '}'
val n2: Int = ch.code      // 125
If you have a value of a floating type, a Double value, for example, you may convert it to a value of an integer type, such as Int or Long.

val d: Double = 12.5
val n: Long = d.toLong() // 12
As you can see, the fractional part is simply dropped.

Also, you can convert a number from a larger type to a smaller type ( Long or Double to Int) using the functions mentioned above.

val d: Double = 10.2
val n: Long = 15

val res1: Int = d.toInt() // 10
val res2: Int = n.toInt() // 15
However, this conversion may truncate the value, as Long and Double can store numbers larger than the truncated Int number.

val bigNum: Long = 100_000_000_000_000

val n: Int = bigNum.toInt() // 276447232; oops
As a result, we receive a truncated value. This problem is known as type overflow. The same problem may occur if you try to convert Int to Short or Byte. So, if you want to convert a larger type value into a smaller one, make sure that the truncation is not going to mess up your program.

Conversion to Short and Byte types
As you know, the Short and Byte types are really small. These types are rarely used, and if you need to store an integer number, you should use Int. Here is an example of why you need to do it.

Normally, you can use functions toShort() and toByte() to convert something to these types. Since Kotlin 1.4, you should avoid these functions when you try to convert Double or Float type. This feature will be removed in future releases. The main problem here is that the conversion can lead to unexpected results due to the variable's smaller size. Now, you need to convert Double or Float to Int and then convert the result to Short or Byte:

val floatNumber = 10f
val doubleNumber = 1.0

val shortNumber = floatNumber.toShort() // avoid this
val byteNumber = doubleNumber.toByte()  // avoid this

val shortNumber = floatNumber.toInt().toShort() // correct way
val byteNumber = doubleNumber.toInt().toByte()  // correct way

String conversion
Sometimes you need to get a string representation of a value of another type. Kotlin provides the toString() function for that. It can convert a value of any type to a string.

val n = 8     // Int
val d = 10.09 // Double
val c = '@'   // Char
val b = true  // Boolean

val s1 = n.toString() // "8"
val s2 = d.toString() // "10.09"
val s3 = c.toString() // "@"
val s4 = b.toString() // "true"
A string can be converted to a number or even to a boolean value but not to a single character.

val n = "8".toInt() // Int
val d = "10.09".toDouble() // Double
val b = "true".toBoolean() // Boolean
If a string representation has an invalid format, it will produce an error. After that, the program will stop unless you take special actions. We will discuss them later.

However, if you convert a string to a boolean value, no errors will occur. If the string is "true" (case insensitive), it will produce a true boolean value, otherwise a false one.

val b1 = "false".toBoolean() // false
val b2 = "tru".toBoolean()   // false
val b3 = "true".toBoolean()  // true
val b4 = "TRUE".toBoolean()  // true

Demonstration
The program below demonstrates the functions discussed above. It reads a string representation of a number, converts it to several other types, and then prints the results of all conversions.

fun main() {
    val something = readln()

    val d = something.toDouble()
    val f = d.toFloat()
    val i = f.toInt()
    val b = i.toByte()

    println(d)
    println(f)
    println(i)
    println(b)
    println(something.toBoolean())
}
Imagine, we have the following input:

1000.0123456789
The program will output the following:

1000.0123456789
1000.0123
1000
-24
false

Let's take a closer look at the output. The number represented by a string is successfully converted to Double, as it has a suitable format. This number can be saved as a Double type safely. Then the number is converted to Float. We see a loss here, as this type can store fewer decimal numbers. The Int conversion cuts the fractional part. The number 1000 is larger than the Byte type can store (from -128 to 127), so we have a type overflow (-24). The result of converting the input string to Boolean is false, because the value is not "true".
*/

/*fun main() {
    val n: Int = 10_000 * 10_000 * 10_000
    println("n is $n")
}*/

/*
It is known that the Galactic Empire has more ships than the Rebel Alliance and the number of the Empire's ships is a multiple of the number of the rebels' ships.

Write a program that calculates how many times larger the Empire fleet is.

Input: two integers as strings (each starting on a new line).

Output: Int value. */
/*
import java.util.Scanner

fun main() {

    val scanner = Scanner(System.`in`)

    val n1: Double = scanner.nextDouble()
    val n2: Double = scanner.nextDouble()
    val mult = n1 / n2

    println(mult.toInt())

}*/

import java.util.Scanner

fun main() {

    val scanner = Scanner(System.`in`)

    val n1 = scanner.nextLong()
    val n2 = scanner.nextLong()
    val mult = n1 + n2

    println(mult.toLong())

}

/*n.toint().toByte() */
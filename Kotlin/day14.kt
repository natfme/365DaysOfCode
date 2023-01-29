// Day 14 - Arithmetic operations

/*
Kotlin has five arithmetic operators:

addition +
subtraction -
multiplication *
integer division /
modulus %

These operators are binary, which means they take two values as operands. The operand is the value or variable the operator is being applied to. For example, in expression 1 + 3, 1 and 3 are the operands, and + is the operator.

The piece of code below prints the results of addition, subtraction, and multiplication:

println(13 + 25) // prints 38
println(20 + 70) // prints 90

println(70 - 30) // prints 40
println(30 - 70) // prints -40

println(21 * 3)  // prints 63
println(20 * 10) // prints 200
The / operator divides the integer parts of two numbers; the fractional part is discarded. You may read about modulo division in our topic.

println(8 / 3)  // prints 2
println(41 / 5) // prints 8
The % operator finds the remainder of a division:

println(10 % 3) // prints 1 because 10 divided by 3 leaves a remainder of 1
println(12 % 4) // prints 0 because 12 divided by 4 leaves no remainder
As you may know, division with negative numbers is different.

Complex expressions -----------------------------------
You can combine arithmetic operations to write complex expressions:

println(1 + 3 * 4 - 2) // prints 11
The calculation order coincides with the rules of arithmetic operations. Multiplication has a higher priority than addition or subtraction, so 3 * 4 is calculated first.

Consider an expression as a part of code that produces a value (for example, 14 + 5 or 15 - 3 * 4). Further, we will take a closer look at expressions.

Use parentheses to specify the order of execution. Let's take a look at the example below:

println((1 + 3) * (4 - 2)) // prints 8
Parentheses can be nested. You can also use them to simplify the notation.

For example, here is a program that prints all digits of the number 54 in reverse order. We will use arithmetic operations to extract the digits.

fun main() {
    println(54 % 10) // it prints 4
    println((54 / 10) % 10) // it prints 5
}
The program outputs:

4
5

Unary operators ------------------------------------------
A unary operator takes a single value as the operand.

A unary plus just gives you a value. It is an optional operator, so you omit it in practice:
println(+5) // prints 5
println(+(-5)) // prints -5
A unary minus negates a value or expression:
println(-8)  // prints -8
println(-(100 + 4)) // prints -104

Precedence order ----------------------------------------
Take a look at the precedence order of arithmetic operators, including parentheses. The list is sorted from the highest to the lowest priority.

Parentheses;
Unary plus/minus;
Multiplication, division, and modulus;
Addition and subtraction.
Mind this order: it's important for correct calculations. Also, you can use the acronym BODMAS (Brackets, Order, Division, Multiplication, Addition, Subtraction) to remember priority.
*/

// -------------------------------------------------------------------------------------------------------------------------------------
// Type of the numeric expression

/*
Type coercion
In such cases, the compiler automatically sets all components (it's called type coercion) and the result type to the widest type in the expression. The picture below illustrates the direction of this casting:

Byte  ->
        Int -> Long -> Float -> Double
Short ->

Since the type of the result is wider than the previous type, there is no loss of information.

Type coercion is rare in Kotlin. It works only with numbers and strings.

Examples ---------------------------------------------------------------------------------------------------
The theory looks pretty clear, so let's take a look at some examples of type coercion.

from Int to Long:
val num: Int = 100
val longNum: Long = 1000
val result = num + longNum // 1100, Long
Although result is just 1100, it is the sum of Long and Int variables, so the type is automatically cast to Long. If you try to declare a result as Int, you get an error because you cannot assign the value of Long type to an Int variable. You can assign only an Int value or an integer number to a variable of Int type.

from Long to Double:
val bigNum: Long = 100000
val doubleNum: Double = 0.0
val bigFraction = bigNum - doubleNum // 100000.0, Double

Short and Byte types -------------------------------------------------------------------------------------------

You can see how the result of an expression with variables of different types is automatically cast to the widest type. However, the Byte and Short types are unusual in this respect. If you need to do some calculations with these types, the result of the calculation is Int:

Byte and Byte
val one: Byte = 1
val two: Byte = 2
val three = one + two // 3, Int

Short and Short
val fourteen: Short = 14
val ten: Short = 10
val four = fourteen - ten // 4, Int

Short and Byte
val hundred: Short = 100
val five: Byte = 5
val zero = hundred % five // 0, Int

So what should we do if we want to sum two Byte variables and get a Byte result? Well, in this case, you must manually perform type conversion:

val one: Byte = 1
val five: Byte = 5
val six = (one + five).toByte() // 6, Byte
Remember that Byte can store data in the range -128.. 127.

Summary -------------------------------------------------------------------------------------------

To sum up, if you have an expression with different numeric types, use these rules to know the type of the result:

If either operand is of type Double, the result is Double.
Otherwise, if either operand is of type Float, the result is Float.
Otherwise, if either operand is of type Long, the result is Long.
Otherwise, the result is Int.
Type coercion does not occur when a value is put into the variable. For example, val longValue: Long = 10.toInt() is incorrect, because 10 is Int and longValue requires Long type.


Look at the piece of code below. Select the lines that are written incorrectly:

fun main() {
    val seven = 7.0
    val five = 5

    val toShort = seven.toShort()            // line 4  esta
    val sum = seven + five                   // line 5
    val difference = seven - five.toDouble() // line 6
    val toByte = seven.toByte()              // line 7 esta
    val mul = seven * five                   // line 8
}
*/

/*
Select all invalid lines in the following snippet.

val b0: Byte = 2
val s0: Short = 10
val n0: Int = 5    
val l0: Long = 14
val f0: Float = 11.4f

val b: Byte = 5                 
val s: Short = 2 + b0           
val n: Int = s0.toByte() + 2    
val l: Long = n0 + 4            
val f: Float = l0.toFloat() + 1 
val d: Double = f0 / 1          
Keep in mind that you cannot assign a value of type Float to a variable of type Double and so on. And remember the rules:

If either operand is of type Double, the result is Double.
Otherwise, if either operand is of type Float, the result is Float.
Otherwise, if either operand is of type Long, the result is Long.
Otherwise, the result is Int.

fix it ------

fun main(args: Array<String>) {
    val b0: Byte = 2
    val s0: Short = 10
    val n0: Int = 5    
    val l0: Long = 14
    val f0: Float = 11.4f

    val b: Byte = 5
    val s: Short = 2 + b0                   Esta
    val n: Int = s0.toByte() + 2
    val l: Long = n0 + 4                    Esta
    val f: Float = l0.toFloat() + 1 
    val d: Double = f0 / 1                  Esta
}
*/
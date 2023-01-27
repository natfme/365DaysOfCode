//Day 13 - Boolean and logical operations
/*fun main(args: Array<String>) {
    val t = true  // t is true
    val f = false // f is false

    println(t) // true
    println(f) // false
}

Boolean variables ----------------------------------------------------------------------
Boolean is a special data type that has only two possible values — true and false:

val t = true  // t is true
val f = false // f is false

println(t) // true
println(f) // false
You cannot assign an integer value to a Boolean variable. In Kotlin, 0 is not the same as false.

Reading Boolean values -------------------------------------------------------
Since Kotlin 1.4, you can read a Boolean value like this:

val b: Boolean = readLine().toBoolean()
and since Kotlin 1.6, you can read a Boolean value like this:

val b: Boolean = readln().toBoolean()
toBoolean() returns true if the input is "true", case insensitive. If otherwise, it will return false.

So, suppose you have the following input:

true
True
TRuE
T
false
The output will be as follows:

println(readln().toBoolean()) // true
println(readln().toBoolean()) // true
println(readln().toBoolean()) // true
println(readln().toBoolean()) // false
println(readln().toBoolean()) // false
You can use readLine()!!.toBoolean() with any compiler version Kotlin is 1.3 or older:

val b: Boolean = readLine()!!.toBoolean()
Since Kotlin 1.5, you can use other functions to convert String to Boolean. The function toBooleanStrict() returns true if the string is equal to the word "true", case sensitive, and false if the string is equal to "false"; otherwise, your program will crash with the java.lang.IllegalArgumentException error. The function toBooleanStrictOrNull() returns true if the string is equal to the word "true", case sensitive, and false if the string is equal to "false"; otherwise, it returns a special value null. We will discuss it later.

println("true".toBooleanStrict())     // true
// println("True".toBooleanStrict())  // program crashes
println("false".toBooleanStrict())    // false
// println("faLse".toBooleanStrict()) // program crashes

println("true".toBooleanStrictOrNull())  // true
println("false".toBooleanStrictOrNull()) // false
println("faLse".toBooleanStrictOrNull()) // null

Logical operators ---------------------------------------------------------------------------
Boolean type variables construct logical statements with the help of logical operators. Kotlin has four logical operators: NOT, AND, OR, and XOR:

NOT is a unary operator that reverses the Boolean value. It can be denoted with !.

val f = false // f is false
val t = !f    // t is true

AND is a binary operator that returns true if both operands are true. Otherwise, it returns false. It can be denoted with &&.

val b1 = false && false // false
val b2 = false && true // false
val b3 = true && false // false
val b4 = true && true  // true 

OR is a binary operator that returns true if at least one operand is true. Otherwise, it returns false. It can be denoted with ||.

val b1 = false || false // false
val b2 = false || true  // true
val b3 = true || false  // true
val b4 = true || true   // true

XOR (exclusive OR) is a binary operator that returns true if the Boolean operands have different values. Otherwise, it is false.

val b1 = false xor false // false
val b2 = false xor true  // true
val b3 = true xor false  // true
val b4 = true xor true   // false
The XOR operator is not as popular as other logical operators. But you can still use it, just in case.

Logical operator precedence -------------------------------------------------------------
Take a look at the precedence of logical operations in Kotlin below. Precedence determines how other variables are grouped in the absence of parentheses:

! for NOT

xor for XOR

&& for AND

|| for OR

So, the variable below is true:

val bool = true && !false // true because !false is evaluated first
You can use parentheses (...) to change the order of execution.

For example, let's write a Boolean expression that determines the possibility of going on a hike during the summer and in other seasons:

val cold = false
val dry = true
val summer = false // suppose it is autumn now

val hiking = dry && (!cold || summer) // true, let's go hiking!
Do not get carried away by the expression above. A good programmer should understand not only arithmetic rules but also logical operations. Otherwise, you can end up hiking in bad weather.

---------------------
fun main(args: Array<String>) {
    //val b: Boolean = readLine()!!.toBoolean()
    //print(b)
    val f = false // f is false
    val t = !f    // t is true

    val b1 = false && false // false
    val b2 = false && true // false
    val b3 = true && false // false
    val b4 = true && true  // true 

    val b5 = false || false // false
    val b6 = false || true  // true
    val b7 = true || false  // true
    val b8 = true || true   // true

    val b9 = false xor false // false
    val b10 = false xor true  // true
    val b11 = true xor false  // true
    val b12 = true xor true   // false

    println(f)
    println("NOT")
    println(t)
    println("AND")
    println(b1)
    println(b2)
    println(b3)
    println(b4)
    println("OR")
    println(b5)
    println(b6)
    println(b7)
    println(b8)
    println("XOR")
    println(b9)
    println(b10)
    println(b11)
    println(b12)

}

Mr. Groundhog is throwing a party. He’s known for his pragmatism, so only those who bring a gift will be allowed to attend the party. And, of course, a guest must have an invitation.

Write a program that checks if a guest should be allowed at the party. The program should read two booleans, each on a separate line:

One showing whether the guest has an invitation;
Another indicating if the guest brought a gift.
Print true if both conditions are met and false if not.



fun main() {
    val invitation = readLine()!!.toBoolean()
    val gift: Boolean = readLine()!!.toBoolean()

    val result = invitation && gift
    println(result)
}

Write a program that reads three boolean variables x, y, and z (each on a separate line) and then prints the result of the following logical expression: NOT(x AND y) OR (z).

Sample Input 1:
true
true
false

Sample Output 1:
false

Sample Input 2:
true
false
true

Sample Output 2:
true
*/

fun main() {
    val x = readLine().toBoolean() // read other values in the same way
    // write your code here
    val y = readLine().toBoolean() // read other values in the same way
    val z = readLine().toBoolean() // read other values in the same way

    val result = !(x && y) || z
    println(result)
}

/*
Imagine you need to determine whether you should go to a store. There are two variables to help you make a choice:

isClosingSoon determines that this store is closing soon (in a few minutes)
isNear determines that this store is near you
Write a boolean expression that is true if at least one condition is true:

the store is not closing soon
the store is near you
Otherwise, the expression is false.
*/
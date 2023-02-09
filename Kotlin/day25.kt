// Day 25 - Introduction to MutableList

/*
Introduction to MutableList
The Kotlin Standard Library provides many ways to organize data and to group multiple values. Now we will consider one of them – the MutableList.

MutableList is an ordered list of variables of the same type. You can access the list items by their indexes.

val numbers = mutableListOf(10.8, 14.3, 13.5, 12.1, 9.7) 

println(numbers) // [10.8, 14.3, 13.5, 12.1, 9.7]

The picture below illustrates a mutable list of five floating-point numbers. Each element has an integer index (0-4), so you can access an element by referring to its index. The first element always has the index 0, and the last element has the index that equals the list size minus one.

----------------------------------------------------------------------------------------------------------------------------------------

Creating a MutableList with specified elements
In Kotlin, the mutableListOf() function is used to create an object of the MutableList class.

Kotlin can handle any types of MutableList you want: for example, Int, Long, Double, Float, Char, String, Byte, or Boolean.

Here is an example of creating a mutable list in cases when we know the content type. In angle brackets <>, you may specify the type of data that will be stored in the list. You will learn more about <> in the following topics.

//declaring a mutable list of integers
val mutableListA = mutableListOf<Int>(1, 2, 3, 4, 3)
println(mutableListA)
  
//declaring a mutable list of strings
val mutableListB = mutableListOf<String>("Kotlin", "JetBrains")
println(mutableListB)
  
//declaring an empty mutable list of booleans
val mutableListC = mutableListOf<Boolean>()
println("Empty list $mutableListC")

The above code snippet prints three lists:

[1, 2, 3, 4, 3]
[Kotlin, JetBrains]
Empty list []
Also, Kotlin allows you to not explicitly specify what type of data the list stores:

//declaring a mutable list of integers
val mutableListA = mutableListOf(1, 2, 3, 4, 5)

println(mutableListA) // [1, 2, 3, 4, 5]

----------------------------------------------------------------------------------------------------------------------------------------

MutableList size
To create a mutable list of a specified size n, we use the MutableList(n) function:

val list = MutableList(5) { 0 }

println(list) // [0, 0, 0, 0, 0]
In curly braces, we write the object that will make up our list. For example, if you specify "a", the list will contain 5 elements equal to "a":

val list = MutableList(5) { "a" }

println(list) // [a, a, a, a, a]
A mutable list always has a specified size, that is, the number of elements. To obtain it, we need to take the value of the size property. It is a number of the Int type.

val numbers = mutableListOf<Int>(1, 2, 3, 4, 5)

println(numbers.size) // 5

----------------------------------------------------------------------------------------------------------------------------------------

Reading list from input
You don't need to figure out all the snippets right now, just use them as a template in your projects!

To read a list of a certain size from the console, we first need to create a MutableList of some type with a known size. Inside the parentheses, we should place readln(), with the help of which we can read input from the console. The readln() function returns a string, so don’t forget to convert the input string into the type of the created list.

val numbers = MutableList(5) { readln().toInt() } // on each line single numbers from 1 to 5
println(numbers) // [1, 2, 3, 4, 5]

This code allows you to read 5 numbers, each number on a separate line.

If you want to read a list in a single line, use the following approach. You can read the list with the readln() function. You’ll get a string, which you should split.

// here we have an input string "1 2 3 4 5"

val numbers = readln().split(" ").map { it.toInt() }.toMutableList()
println(numbers) // [1, 2, 3, 4, 5]

Let’s have a look at this code snippet. We read a string from input and then use split(). We divide our string into smaller ones by space, then we use the map function to convert every element to Int, and then we convert the result to MutableList. Here you can read more about mapping transformation.

There is also a way that allows you to ignore line breaks and extra spaces in the input string. You can do this with the help of regular expressions, which are often used in text searching and editing.

val regex = "\\s+".toRegex()  // 1 or more whitespace character (space, tabs etc.)
val str = "1 2\t\t3  4\t5  6"
val nums = str.split(regex).map { it.toInt() }.toMutableList()
println(nums.joinToString()) // 1, 2, 3, 4, 5, 6

With this regular expression, you can ignore spaces and tabs in the input string. You can learn more about regular expressions in our topics.

----------------------------------------------------------------------------------------------------------------------------------------

Accessing elements
You can change the values of mutable list elements. Use index to set a value in the list.

Setting the value of an element using the element's index:

list[index] = elem
Getting the value of an element using the element's index:

val elem = list[index]
List indexes are numbers from 0 (the first element) to list.size-1 (the last element).

Here is an example of a three-element list of integers:

val numbers = mutableListOf(0, 0, 0) // numbers: 0, 0, 0

numbers[0] = 1 // numbers: 1, 0, 0
numbers[1] = 2 // numbers: 1, 2, 0
numbers[2] = numbers[0] + numbers[1] // numbers: 1, 2, 3

println(numbers[0]) // 1, the first element
println(numbers[2]) // 3, the last element

Let's take a closer look at the code above. First, we have a list with three elements. All elements are equal to 0. Then, the value of 1 is assigned to the first element of the list at the index 0. Then, the value of 2 is assigned to the second element of the list at the index 1. After that, the value of 3 (the sum of 1 and 2) is assigned to the last element of the list at the index 2. Then, we print the first and the last elements of the three-element list.

If we try to access a nonexistent element by index, there will be an error in the program. Let's try to get the fourth element with the index 3 in the above numbers list:

val elem = numbers[3]

IDEA will issue a warning: "Index is always out of bounds," if you miss this warning, you will receive the exception "IndexOutOfBoundsException". You can learn more about the Exception topic.

As you already know, the last list element has an index equal to list.size - 1. Let's access the last element and the one before last:

val alphabet = mutableListOf('a', 'b', 'c', 'd')

val last = alphabet[alphabet.size - 1]    // 'd'
val prelast = alphabet[alphabet.size - 2] // 'c'

Kotlin provides several convenient ways to get the first and the last list elements as well as the last index in the list:

println(alphabet.first())   // 'a'
println(alphabet.last())    // 'd'
println(alphabet.lastIndex) // 3

Use this approach to make your code more readable and to avoid accessing nonexistent indexes.

----------------------------------------------------------------------------------------------------------------------------------------

In this topic, we have discussed the concept of a mutable list and the basic operations with it. Please, remember that:

A mutable list is a data structure of elements that can be accessed by index;

The first element of a list has the index 0;

A mutable list always has a specified size;

It is possible to modify an element of a list using the element's index;

Kotlin can handle lists of different types: Int, Char, Double, and so on.

-----------------------------------------------------------------------------------------------------------------------------------

map

val numbers = setOf(1, 2, 3)
println(numbers.map { it * 3 })
println(numbers.mapIndexed { idx, value -> value * idx })

val numbers = setOf(1, 2, 3)
println(numbers.mapNotNull { if ( it == 2) null else it * 3 })
println(numbers.mapIndexedNotNull { idx, value -> if (idx == 0) null else value * idx })

val numbersMap = mapOf("key1" to 1, "key2" to 2, "key3" to 3, "key11" to 11)
println(numbersMap.mapKeys { it.key.uppercase() })
println(numbersMap.mapValues { it.value + it.key.length })
*/

// Practice 1 - Initializing a mutable list of longs

/*
Create a mutable list of longs named longs with three elements: 100_000_000_001, 100_000_000_002, and 100_000_000_003. Output the list.

fun main() {
    val longs = mutableListOf(100_000_000_001, 100_000_000_002, 100_000_000_003)

    // do not touch the lines below 
    println(longs.joinToString())
}
*/

// Practice 2 - Initializing a mutable list of integers

/*
Create an Int mutable list named numbers with five elements: 12, 17, 8, 101, and 33. After that, the code will output it.

Use the provided code template.

fun main() {
    val numbers = mutableListOf(12, 17, 8, 101, 33)

    // do not touch the lines below 
    println(numbers.joinToString())
}
*/

// Practice 3 - Getting an element

/*
fun main(args: Array<String>) {
    val list = mutableListOf(1, 2, 3, 4, 5, 6, 7, 8, 9)
    val n = 6
    val elem = list[list[n]]

    println(elem) //8
}
*/

// Practice 4 - Basic operations

/*
fun main(args: Array<String>) {
    val numbers = mutableListOf<Int>(1, 2, 3, 5, 4, 6, 4)
    println(numbers[0])
    println(numbers[6])
    //println(numbers[7]) // The program fails
    println(numbers.size)
}
*/

// Practice 5 - Right ways to create mutable lists

// val list = mutableListOf(1, 2, 3)

// val list = MutableList(3) { 0 }

// Practice 6 - Equal lists

/*
val numbers1 = mutableListOf<Int>(1, 2, 3, 4)
val numbers2 = mutableListOf<Int>(1, 2, 3, 4)
val numbers3 = mutableListOf<Int>(4, 3, 2, 1)
val numbers4 = mutableListOf<Int>(1, 2, 3)

println(numbers1 == numbers2)
*/
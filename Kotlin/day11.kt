//day 11

//Cmd - he echo command is used to print strings. Echo will print the string you type next to it.
//The pushd command saves the current working directory in memory and moves to the specified directory (the root in this example). The popd command returns to the latest directory saved in memory.

//String basics

/*
The length of a string
You will often need to get the length of a String. The length of the string is determined by the number of characters that are enclosed between the double quotes. To do this, simply use .length which gives a value of the Int type:

val language = "Kotlin"
println(language.length) // 6

val empty = ""
println(empty.length) // 0

Concatenating strings ---------------------------------------------
Another common operation with String is concatenation. It is used to construct one string out of other strings.

Two strings can be concatenated with the +:

val str1 = "ab"
val str2 = "cde"
val result = str1 + str2 // "abcde"
When we concatenate two strings, a new string is created.

val one = "1"
val two = "2"
val twelve = one + two 
println(one)      // 1, no changes
println(two)      // 2, no changes
println(twelve)   // 12
You can concatenate multiple strings in the same expression:

val firstName = "John"
val lastName = "Smith"
val fullName = firstName + " " + lastName

Pay attention, str1 + str2 is not the same as str2 + str1 because the concatenation is not a commutative operation, unlike addition.

Appending values to strings----------------------------------------------------------
The + also works for appending values of different types to a String. The value is automatically converted to a String and then concatenated to the target String:

val stringPlusBoolean = "abc" + 10 + true
println(stringPlusBoolean) // abc10true

val code = "123" + 456 + "789"
println(code) // 123456789

An expression must start with a String.
Take a look at the example below. It wouldn't work because the first operand is a number:

val errorString = 10 + "abc" // an error here!
Let's consider a different situation:

val stringAndNumbers = "abc" + 11 + 22
println(stringAndNumbers) // abc1122
Why did that work? First, it appends 11 to the string "abc", and then it appends 22 to the string "abc11".

You may concatenate a character with a String to get a new String:

val charPlusString = 'a' + "bc"
println(charPlusString) // abc
val stringPlusChar = "de" + 'f'
println(stringPlusChar) // def
Also, you may append any value to the result, because characters plus a string gives you a String:

val charPlusStringPlusInt = 'a' + "bc" + 123
println(charPlusStringPlusInt) // abc123
We will discuss how to work with characters later, but for now, just remember that you can concatenate characters and strings to get a String value. If you are interested in how characters operate with integers, look at this topic.

Repeating the string-----------------------------
If you need to repeat one string two or more times, then hold your loops: Kotlin provides the repeat function:

print("Hello".repeat(4)) // HelloHelloHelloHello
Now, imagine your friend senior developer gave you a secret on how to become the best programmer:

To do:
-Eat
-Sleep
-Code
-Repeat

Let's try to transform this piece of paper to a code snippet that prints your schedule for every day of the week:

println("Eat. Sleep. Code.\n".repeat(7)) // \n gives you a line feed (new line)
And here goes your week schedule:

Eat. Sleep. Code.
Eat. Sleep. Code.
Eat. Sleep. Code.
Eat. Sleep. Code.
Eat. Sleep. Code.
Eat. Sleep. Code.
Eat. Sleep. Code.
No time for procrastination!

Raw string------------------------------------------------
Sometimes you need some special symbols like tabs or quote marks in your string. You can do it with the help of escape sequences. For example:

// prints 'H' is the first letter of "Hello world!" string.
println("\'H\' is the first letter of \"Hello world!\" string.")
This looks a little heavy. If you need to write a fairly large text with newlines and special characters, it can be difficult to read.

For these cases, you can use a raw string. A raw string can contain newlines and any other characters. You just need to wrap the text in triple quotes ("""):

val largeString = """
    This is the house that Jack built.
      
    This is the malt that lay in the house that Jack built.
       
    This is the rat that ate the malt
    That lay in the house that Jack built.
       
    This is the cat
    That killed the rat that ate the malt
    That lay in the house that Jack built.
""".trimIndent() // removes the first and the last lines and trim indents
print(largeString)
This text prints:

This is the house that Jack built.

This is the malt that lay in the house that Jack built.

This is the rat that ate the malt
That lay in the house that Jack built.

This is the cat
That killed the rat that ate the malt
That lay in the house that Jack built.
As you see, we also used the function .trimIndent(). It cut off all the lines of the common minimal indent and removed the first and last lines if they are empty. For example:

val unevenString = """
        123
         456
          789""".trimIndent()
print(unevenString)
println()

val rawString = """123
         456
          789
""".trimIndent()
print(rawString )
This code prints:

123
 456
  789

123
         456
          789
*/

// JSON is a format for storing data. Below is an example of a simple JSON representation for a person. Let's practice a bit! Write a program that prints this representation.

/*
{
    "firstName": "John",
    "lastName": "Smith",
    "age": 35,
    "phoneNumbers": [
        {
            "type": "mobile",
            "number": "123 567-7890"
        }
    ]
}
*/

/*
fun main() {
    println(
        """{
    "firstName": "John",
    "lastName": "Smith",
    "age": 35,
    "phoneNumbers": [
        {
            "type": "mobile",
            "number": "123 567-7890"
        }
    ]
}"""
    )
}
*/

fun main() {
    val spell = "abra"
    println((spell + "cad").repeat(spell.length) + spell)
    val name = "10 " + "years " + "ago we were " + "in London"
    print(name)
    println("I\'m learning Kotlin!\n".repeat(6))
}

//An inexperienced programmer created name incorrectly. You need to fix it so that the program outputs 10 years ago we were in London.

//Write a program that prints I'm learning Kotlin! six times, each from a new line.



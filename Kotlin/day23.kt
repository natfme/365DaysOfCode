// Practice day 21 https://hyperskill.org/tracks/18

// Boolean and logical operations

// Buy a car

// You're a programmer and you want to buy a car. There are several restrictions on the path of buying a car:

/*
fun main(args: Array<String>) {
    val mercedes = true
    val red = true
    val enoughMoney = true

    val buyCar = enoughMoney && (!mercedes || red)
    print(buyCar)
}
*/

// So, select the desired combinations of restrictions when buyCar is true.
/*
* enoughMoney is true, mercedes is false, red is false.
* enoughMoney is true, mercedes is false, red is true.
* enoughMoney is true, mercedes is true, red is true.
*/

// Characters

/*
What is a character

Each character is just a symbol enclosed in single quotes. The Char type represents letters (both uppercase and lowercase), digits, and other symbols:

val lowerCaseLetter: Char = 'a'
val upperCaseLetter: Char = 'Q'
val number: Char = '1'
val space: Char = ' '
val dollar: Char = '$'
This type can represent any symbol including hieroglyphs, as well as some special symbols.

A character can also be represented by its hexadecimal code in the Unicode table. The code starts with \u:

val ch = '\u0040' // it represents '@'
println(ch) // @

Although we use a sequence of characters to represent such code, the code itself represents exactly one character.

For example, Latin capital letters have hexadecimal codes from '\u0041' to '\u005A', and Latin lowercase letters have codes ranging from '\u0061' to '\u007A'.

You can also convert numbers to characters and vice versa. Let's take a look at how it works:

val ch = 'a'
println(ch.code)   // 97
val num = 97
println(num.toChar()) // a

// ---------------------------------------------------------------------------------------------------------------------------------- //

How to read characters

Kotlin does not provide a convenient function to read a Char. However, you can do it another way: if you need to read one Char in a whole line, use this construction:

val ch: Char = readln().first()
You just read a String and get its first element, which will be a Char. Strings are composed of characters, but we will discuss this in more detail a little later.

// ---------------------------------------------------------------------------------------------------------------------------------- //

Retrieving subsequent characters

There are two operators for adding (+) and subtracting (-) integer numbers in order to get the next and previous characters according to the Unicode order:

val ch1 = 'b'
val ch2 = ch1 + 1 // 'c'
val ch3 = ch2 - 2 // 'a'

Remember that you cannot add a symbol to a number as it will cause an error.

val ch = 'a'
val ch1 = 1 + ch // Error

You also cannot sum up two characters:

val charsSum = 'a' + 'b' // Error
It is possible to use the increment (++) and decrement (--) operators in their prefix and postfix forms. The assignment operator combined with + or - also works for characters, as well as += and -=.

var ch = 'A'

ch += 10
println(ch)   // 'K'
println(++ch) // 'L'
println(++ch) // 'M'
println(--ch) // 'L'

You cannot multiply or divide characters by numbers.

// ---------------------------------------------------------------------------------------------------------------------------------- //

Escape sequences

There are some special characters starting with a backslash \, which are known as escape or control sequences. Most of them do not have corresponding symbols, and you cannot find them on your keyboard. To represent such characters, we use a pair of regular symbols. In a program, this pair is considered as exactly one character with the appropriate code.

'\n' is the newline character;

'\t' is the tab character;

'\r' is the carriage return character;

'\\' is the backslash character itself;

'\'' is the single quote mark;

'\"' is the double quote mark.

Here are a few examples:

print('\t') // makes a tab
print('a')  // prints 'a'
print('\n') // goes to a new line
print('c')  // prints 'c'
The above code will print:

  a
c
Note: there is also a character to represent a single space ' '. It is just a regular character, not an escape sequence.

// ---------------------------------------------------------------------------------------------------------------------------------- //

Relational operations with characters

You can compare characters using relational operations (==, <, >, <=, >=, and !=) according to their position in the Unicode table.

println('a' < 'c')  // true
println('x' >= 'z') // false

println('D' == 'D') // true
println('Q' != 'q') // true because capital and small letters are not the same

println('A' < 'a')  // true because capital Latin letters are placed before small ones

Using relational operations and codes, we can check whether a Char is a digit: all ten digits have codes from '\u0030' to '\u0039'.

Here is a program that does it:

fun main() {
    val ch = readln().first()
    val isDigit = ch >= '\u0030' && ch <= '\u0039'

    println(isDigit)
}

If the input is a digit '0', '1', '2', ..., '9' (without quotes), the program prints true. Otherwise, it prints false.

// ---------------------------------------------------------------------------------------------------------------------------------- //

Processing characters

There's a variety of useful functions to work with characters. You can use these functions instead of dealing with character codes.

* isDigit() returns true if the given character represents a digit ('1', '2', etc); otherwise, false;

* isLetter() returns true if the given character represents a letter ('a', 'B', 'm', etc); otherwise, false;

* isLetterOrDigit() returns true if the given character represents a letter or a digit; otherwise, false;

* isWhitespace() returns true if the given character represents a whitespace (' ', or '\t', or '\n'); otherwise, false;

* isUpperCase() returns true if the given character is an uppercase character; otherwise, false;

* isLowerCase() returns true if the given character is a lowercase character; otherwise, false;

* toUpperCase() returns the uppercase form of the given character (before Kotlin 1.5; you shouldn't use it nowadays);

* uppercaseChar() returns the uppercase form of the given character (since Kotlin 1.5);

* uppercase() returns a String with the uppercase form of the given character (since Kotlin 1.5);

* toLowerCase() returns the lowercase form of the given character (before Kotlin 1.5; you shouldn't use it nowadays);

* lowercaseChar() returns the lowercase form of the given character (since Kotlin 1.5);

* lowercase() returns a String with the lowercase form of the given character (since Kotlin 1.5).

Let's take a look at some examples of the functions listed above:

val one = '1'

val isDigit = one.isDigit()   // true
val isLetter = one.isLetter() // false

val capital = 'A'
val small = 'e'

val isLetterOrDigit = capital.isLetterOrDigit() // true

val isUpperCase = capital.isUpperCase() // true
val isLowerCase = capital.isLowerCase() // false

val capitalEString = small.uppercase() // "E"
val capitalE = small.uppercaseChar()   // 'E'

There are a lot more useful functions: we will discuss them in the upcoming topics.
*/

/*
Compare Latin letters

Write a program that reads two Latin letters as characters and compares them ignoring cases. If these characters represent the same letter print true , otherwise false.

Sample Input 1:
a
b

Sample Output 1:
false

Sample Input 2:
d
D

Sample Output 2:
true

fun main() {
    // write your code here
    val char1 = readLine()!!.lowercase()
    val char2 = readLine()!!.lowercase()

    if (char1 == char2) {
        println(message = true)
    } else {
        println(message = false)
    }
}

*/

// Practice 2

/*
Comparing numbers and characters

Write a program that reads one number and one character on separate lines and checks whether the entered number corresponds to the decimal representation of the character in the Unicode table.

If the input character is represented by the input number, print true; otherwise, print false.

Sample Input 1:
97
a

Sample Output 1:
true

Sample Input 2:
97
C

Sample Output 2:
false


fun main() {
    // write your code here
    val num = readLine()!!.toInt()
    val character = readLine()!!.first().code

    println(num)
    println(character)

    if (num == character) {
        println(message = true)
    } else {
        println(message = false)
    }
}

//Practice 3 - Previous character

// Write a program that reads four characters and prints the previous character in the Unicode table for each of them.

fun main(args: Array<String>) {
    val character1 = readLine()!!.first().code
    val character2 = readLine()!!.first().code
    val character3 = readLine()!!.first().code
    val character4 = readLine()!!.first().code

    val previousCharacter1 = (character1 - 1).toChar()
    val previousCharacter2 = (character2 - 1).toChar()
    val previousCharacter3 = (character3 - 1).toChar()
    val previousCharacter4 = (character4 - 1).toChar()

    println(previousCharacter1)
    println(previousCharacter2)
    println(previousCharacter3)
    println(previousCharacter4)

    println("---------------------------------------------------------------------")

    repeat(4) {
        println(readLine()!!.first() - 1)
    }
}
*/

// Practice 4 - Digits or not

/*
Write a program that reads four characters and checks for each character whether it is a digit.

The program must print either true or false for each character in a new line.

Sample Input 1:
3
@
8
d

Sample Output 1:
true
false
true
false
*/

fun main() {
    // write your code here
    val character1 = readLine()!!.first()
    val character2 = readLine()!!.first()
    val character3 = readLine()!!.first()
    val character4 = readLine()!!.first()

    println(character1.isDigit())
    println(character2.isDigit())
    println(character3.isDigit())
    println(character4.isDigit())
}
//Day 6 - invoke function

/*Functions arguments
When we want to use a function, we can invoke (or call) it using its name followed by parentheses. If a function takes one or more arguments (input data), they should be passed in the parentheses.

val text = "Hello"
println(text)

This function can also take no arguments at all to print a new line:

println()

So, in its general form, a function can be invoked like this:

function1() // invokes function1 without an argument
function2(arg1) // invokes function2 while passing an argument
function3(arg1, arg2) // invokes function3 while passing two arguments
// ... and so on

Where function is the name of a function.

----------------------------------------------------------
Producing a result
Some functions not only take arguments but also produce (return) some results. You can also assign it to a variable:

val result = function(arg)
Functions that take arguments and produce a result look like regular math functions.

For example, let's take a look at a math function that returns the absolute value of a number:

val number = -10
val nonNegNumber = Math.abs(number) // it takes -10 and returns 10

A benefit of using functions is that you don't need to implement anything, just invoke a function and it will work.

The name of the abs function is written after the dot symbol. The reason is that Math groups multiple functions, and we should write the name of the group to invoke one of them. We won't go into detail right now, just keep in mind that you will see something like that in our examples and practice problems.

All functions return a result, even the println function.

val result = println("text")
println(result) // kotlin.Unit

The result is a special value called Unit, which practically means no result. When your function returns nothing, it means it returns Unit, that's all you need to understand for now. If you're coming from another language like C or Java, you can think of it as Void.
*/


//A function is a subprogram that we can call in the program through the function name

// This is the totalLembas() function. It just counts the total number of lembas. 
// Do not change this code
// This is the totalLembas() function. It just counts the total number of lembas. 
// Do not change this code

fun totalLembas(first : String, second : String) = print(first.toInt() + second.toInt() )

fun main() {
    val breadFromFrodo = readLine()!!
    val breadFromSam = readLine()!!

    

    // write your code here
    totalLembas(breadFromFrodo, breadFromSam)
     
}

//Practice makes perfect. Good for you for not giving up easily!


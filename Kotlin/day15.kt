// Day15 - Increment and decrement

/*
Assignment operations
You already know that Kotlin supports basic arithmetic operations such as addition and subtraction:

var a = 3
a = a + 1 // 4
a = a - 1 // 3
Besides this, there are compound assignment operations that combine arithmetic operations and assignments. The assignment operator = has several forms that combine it with an operation to avoid repeating the variable twice:

+= assignment after addition: A += B equals A = A + B
-= assignment after subtraction: A -= B equals A = A - B
*= assignment after multiplication: A *= B equals A = A * B
/= assignment after division: A /= B equals A = A / B
%= assignment of the remainder after division: A %= B equals A = A % B
Let's take a look at assignment operations performed on a single variable. Here is something very basic:

var a = 3
a += 2 // 5
a -= 2 // 3
a *= 2 // 6
a /= 2 // 3
a %= 2 // 1
Here, we performed calculations with number 2 and our variable a and then assigned the values to it. As you can see, these operations made the code shorter and clearer.

Compound assignment operators can be applied only to a variable that is already defined and cannot be used to declare a new variable:

var a: Int
a += 5 // compile-time error, Variable 'a' must be initialized

Using increment and decrement----------------------------------------------
Another common operation is increasing or decreasing a number by one. Of course, you can use += 1 or -= 1, but Kotlin provides an even better way to do this: increment and decrement operations. Let's look at an example:

var num = 3
num++  // 4, increment
num--  // 3, decrement
The code above is actually the same as below:

var num = 3
num += 1  // 4
num -= 1  // 3
As you can see, increment ++ does the same as +=1 but in a simpler way. The same is true for decrement --.

Note that this works only when you are increasing or decreasing a number by one.
This looks easy, but increment and decrement operations are more complicated than you might think. Both increment and decrement operators have two forms that are very important to distinguish: prefix and postfix.

Prefix form ---------------------------------------------------------------------------------------------------------------------
Prefix form changes the value of a variable before it is used. Let's look at some examples.

Prefix increment returns the incremented value:

var a = 10
val b = ++a
println(a)  // a = 11
println(b)  // b = 11
First, the value of the variable a is increased by one, and then its value is assigned to the variable b. So, a and b are both 11.

Prefix decrement returns the following:

var a = 10
val b = --a
println(a)  // a = 9
println(b)  // b = 9
Here, you see the same thing happening: the value of the variable a is decreased by one, and then its value is assigned to the variable b.

Postfix form ---------------------------------------------------------------------------------------------------------------
By contrast, postfix form changes the value of a variable after it is used. Let's look at the examples.

Postfix increment returns the value before incrementing by one:

var a = 10
val b = a++
println(a)  // a = 11
println(b)  // b = 10
First, the value of the variable a is assigned to the variable b, and then the value of the variable a is increased by one. This way, a is 11 and b is 10.

Similarly, postfix decrement returns the following:

var a = 10
val b = a--
println(a)  // a = 9
println(b)  // b = 10

Order of precedence ----------------------------------------------------------------------------------------------------
Some operations take precedence over others, that is, they are performed first. Take a look at the list of operations in decreasing order of priority:

Parentheses ( (expr) );
Postfix increment/decrement ( expr++, expr--);
Unary plus/minus, prefix increment/decrement ( -expr, ++expr, --expr );
Multiplication, division, and modulus ( *, /, % );
Addition and subtraction ( +, - );
Assignment operations ( =, +=, -=, *=, /=, %= ).
The priority of operations should be taken into account when executing a set of arithmetic expressions:

val a = 2
var b = 3
val c = a + 4 * --b  
println(c)   // this is 10
Decrement has a higher priority than multiplication and addition, so --b is calculated first. Like in arithmetic, parentheses can be used to increase the priority of operation. You can also use them for clarity:

var a = 5
val b = 9
val c = 3
val d = a++ + (b / 2) - c - 4
println(d)   // this is 2
*/

/*
Practice

Consider the code snippet below. What will it print?
var num = 0
println(num++ + ++num)

(num = 0) num++ + ++num
(num = 1) 0 + ++num 
(num = 2) 0 + 2
*/
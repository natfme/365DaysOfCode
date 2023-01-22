//Day 8 - The classification of basic types

/*Numbers
Kotlin provides several types for integers and fractional numbers.

Integer numbers (0, 1, 2, ...) are represented by the following four types: Long, Int, Short, Byte (from the largest to the smallest). These types have different sizes and may represent different ranges of values. The integer type range can be calculated as −(2n−1) to (2n−1)−1, where n is the number of bits. The range includes 0, that's why we subtract 1 from the upper bound.

Byte: 8 bits (1 byte), range varies from -128 to 127;
Short: 16 bits (2 bytes), range varies from -32768 to 32767;
Int: 32 bits (4 bytes), range varies from −(231) to (231)−1;
Long: 64 bits (8 bytes), range varies from −(263) to (263)−1.
The size cannot be changed. It does not depend on the operating system or hardware.

The most common integer types are Int and Long. Try to stick to Int in practice. If you need more freedom for your numbers, use Long:

val zero = 0 // Int
val one = 1  // Int
val oneMillion = 1_000_000  // Int

val twoMillion = 2_000_000L           // Long because it is tagged with L
val bigNumber = 1_000_000_000_000_000 // Long, Kotlin automatically chooses it (Int is too small)
val ten: Long = 10                    // Long because the type is specified

val shortNumber: Short = 15 // Short because the type is specified
val byteNumber: Byte = 15   // Byte because the type is specified
Floating-point types represent numbers with fractional parts. Kotlin has two such types: Double (64 bits) and Float (32 bits). These types can store only a limited number of decimal digits (~6-7 for Float and ~14-16 for Double). The Double type is more common in practice:

val pi = 3.1415              // Double
val e = 2.71828f             // Float because it is tagged with f
val fraction: Float = 1.51f  // Float because the type is specified
To display the maximum and minimum value of a numeric type (including Double and Float), you need to write the type name followed by a dot . and then either MIN_VALUE or MAX_VALUE:

println(Int.MIN_VALUE)  // -2147483648
println(Int.MAX_VALUE)  // 2147483647
println(Long.MIN_VALUE) // -9223372036854775808
println(Long.MAX_VALUE) // 9223372036854775807
It is also possible to get the size of an integer type in bytes or bits (1 byte = 8 bits):

println(Int.SIZE_BYTES) // 4
println(Int.SIZE_BITS)  // 32

Characters
Kotlin has a Char type to represent various letter characters (uppercase and lowercase), digits, and other symbols. Each character is a letter character in single quotes. The size is similar to the Short type (2 bytes = 16 bits):

val lowerCaseLetter = 'a'
val upperCaseLetter = 'Q'
val number = '1'
val space = ' '
val dollar = '$'

Characters can represent symbols of many alphabets, including hieroglyphs and some special symbols, which we will consider later.

Booleans
Kotlin provides a type called Boolean. It can store only two values: true and false. It represents only one bit of information, but its size is not precisely defined.

val enabled = true
val bugFound = false

We will often use this type in conditionals.

Strings
The String type represents a sequence of characters in double quotes. It is one of the most popular types.

val creditCardNumber = "1234 5678 9012 3456"
val message = "Learn Kotlin instead of Java."
*/

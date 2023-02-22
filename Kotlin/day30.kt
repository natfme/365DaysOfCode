fun main() {
    // write your code here
    val n = readLine()!!.toInt()
    val numbers = Array(n) {readLine()!!.toInt()}
    numbers.forEach { println(it) }
}
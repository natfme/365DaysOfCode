fun main() {
    // write your code here
    val n = readLine()!!.toInt()
    var sum = 1
    val numbers = MutableList(n) { readLine()!!.toInt() }

    //val (a, b) = Array(2) { readLine()!!.toInt() }
    var password = true
    while (password == "true") {
            for (i in 1..n) {
            val x1 = numbers[(i-1)]
            val x2 = numbers[(i+1)]
            println(numbers[i])
    
            while (x1 <= x2) {
                sum += 1
            }
        }
        println(sum)
        }
    
}
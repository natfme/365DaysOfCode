// Day 3 - 100 Days of Code: Input & Variables
//What language will you study now?

fun main() {
    // Don't be afraid of the code below! 
    // In the future, you will definitely cope with it, but for now just ignore it.
    var (a, b) = readLine()!!.split(" ").map { it.toInt() }

    // Write only exchange actions here. Do not touch the lines above
    val c = a
    a = b
    b = c

    // Do not touch the lines below
    print("$a $b")

    val pi = 3.1415
    val helloMsg = "Hello" //immutable

    println(pi) //3.1415
    println(helloMsg) //Hello

    //pi = 3.1415 // Como pi fue declarado con val, su valor no cambia y dará un error
    /*
    val boolFalse: Boolean
    println(boolFalse) //Debe producir un error ya que la variable no ha sido inicializada, no se le ha asignado un valor
    */

    //Correcciones
    val boolFalse: Boolean //no inicializada
    boolFalse = false //inicializada con un valor false
    println(boolFalse) //debería imprimir false, sin ningún error

    val count :Int = 10
    var cnt = count
    
    //cnt = 20 // No se presentan errores aquí, porque cnt no es una constante, el valor val a sido reasignado a var
    println(cnt)
    cnt = 20
    println(cnt)
}


import getListOfNumbers// Day22 - listas mutables
import getListofNumbersDoubles

/*
add(element) para añadir un nuevo ítem en la parte superior de la lista
add(index, element) para insertar a ítem en un índice
removeAt(index) para eliminar ítem en un índice
[index]=element, para reemplazar un ítem en el índice. Esta construcción es equivalente al operador set(index, element)

ejemplo

val colorsList = mutableListOf("Amarillo", "Azul", "Rojo")

    colorsList.add("Verde") // [Amarillo, Azul, Rojo, Verde]
    colorsList.add(0, "Blanco") // [Blanco, Amarillo, Azul, Rojo, Verde]
    colorsList.removeAt(2) // [Blanco, Amarillo, Rojo, Verde]
    colorsList[1] = "Negro" // [Blanco, Negro, Rojo, Verde]
    colorsList.sortDescending() 

    println(colorsList) // [Verde, Rojo, Negro, Blanco]
*/

fun getListOfNumbers(): List<Int> {
    return listOf(1, 2, 3, 4, 5)
}

fun getListOfStrings(): List<String> {
    return listOf("apple", "banana", "cherry")
}

fun getListofNumbersDoubles(): List<Double> {
    val listOfDoubles = mutableListOf<Double>()
    listOfDoubles.add(1.1)
    listOfDoubles.add(2.2)
    listOfDoubles.add(3.3)
    return listOfDoubles
}

fun cuadratica (a : Double, b : Double, c: Double) : List<Double> {
    val disc = Math.pow(b, 2.0) - 4 * a * c
    val listOfXs = mutableListOf<Double>()
    if ( disc > 0) {
        listOfXs.add((-b + Math.sqrt(disc)).div(2 * a))
        listOfXs.add((-b - Math.sqrt(disc)).div(2 * a))
    } else if ( disc == 0.0) {
        listOfXs.add(-b.div(2 * a))
        listOfXs.add(listOfXs[0])
    } else {
    }
    return listOfXs

}

fun main() {
    // put your code here
    val number = 16.0
    val squareRoot = Math.sqrt(number)
    println("The square root of $number is $squareRoot")

    println(getListOfNumbers())
    println(getListOfStrings())
    println(getListofNumbersDoubles())
    print(cuadratica(1.0, -6.0, 5.0))
}

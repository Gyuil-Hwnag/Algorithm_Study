import java.util.*

fun main(args: Array<String>){
    val list1 = mutableListOf(1,2,7,6,5,6,8)
    list1.sort()
    println(list1)

    val list2 = mutableListOf(1, 2, 7, 6, 5, 6)
    val sorted = list2.sorted()
    println(sorted)
    println(list2)

    list2.sortByDescending { it }
    println(list2)

    val list3 = mutableListOf(1, 2, 7, 6, 5, 6)
    val sorted2 = list2.sortedByDescending { it }
    println(sorted2)
    println(list3)
    println(list3.sort())
    println(list3.reversed())

    val list4 = mutableListOf(1 to "a", 2 to "b", 7 to "c", 6 to "d", 5 to "c", 6 to "e")
    list4.sortBy { it.second }
    println(list4)

    val list5 = mutableListOf(1 to "a", 2 to "b", 7 to "c", 6 to "d", 5 to "c", 6 to "e")
    list5.sortWith(compareBy({it.second}, {it.first}))
    println(list5)

}
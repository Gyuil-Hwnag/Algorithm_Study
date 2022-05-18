import java.util.PriorityQueue
import java.util.*


fun main(args: Array<String>){
    val pq1 = PriorityQueue<Int>()
    val pq2 = PriorityQueue<Int>(reverseOrder())

    pq1.add(4)
    pq2.addAll(listOf(1,3,4,5,6,6))
    pq1.offer(2)
    print(pq1)

}
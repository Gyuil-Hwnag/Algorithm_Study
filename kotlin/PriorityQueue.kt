import java.util.*

fun main(args: Array<String>){
    val pq1 = PriorityQueue<Int>()
    val pq2 = PriorityQueue<Int>(reverseOrder())

    // add : 뒤에 삽입, offer : 앞에 삽입
    pq1.add(4)
    pq2.addAll(listOf(1,3,4,5,6,6))
    pq1.offer(2)

    // peek : 첫번째 꺼 보기, poll : 꺼내기
    println(pq2)
    println(pq2.peek())
    println(pq2)
    println(pq2.poll())
    println(pq2)
    println(pq2.reversed())
}
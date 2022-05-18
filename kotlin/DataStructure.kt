import java.util.Stack
import java.util.Queue
import java.util.LinkedList
import java.util.HashMap
import java.util.*

fun main(){
    class array{
        // 1,2,3 으로 된 배열 생성
        val array1: Array<Int> = arrayOf(1,2,3)
        // 크기가 5인 0으로 초기화 된 배열 생성
        val array2: Array<Int> = Array(5) { 0 }
        // 1,2,3 으로 된 배열에 3 이 추가된 1,2,3,3 인 배열 생성
        val array3 = array1.plus(3)
    }
    
    class stack{
        // stack은 LIFO 방식 <- 즉, 후입 선출
        val stack = Stack<Int>()

        // stack 의 최상단에 쌓기
        stack.push(3)
        stack.push(4)
        
        // stack 의 최상단 뽑기
        stack.pop()
    }
    
    class queue{
        // Queue 는 FIFO 방식 <- 즉, 선입 선출
        val queue: Queue<Int> = LinkedList()
        
        // Queue 의 마지막에 추가
        queue.add(3)
        queue.add(4)
    
        // Queue 의 제일 앞에서 빼기
        queue.remove()
        queue.poll()
    }
    
    class linkedList{
        val linkedList = LinkedList<Int>()
        // 리스트에 제일 앞부분에 추가
        linkedList.addFirst(3)
        // 리스트의 1번째 인덱스에 추가
        linkedList.add(1, 4)
        // 리스트의 제일 마지막 부분에 추가
        linkedList.addLast(5)
    
        // 리스트의 0번쨰 인덱스 삭제
        linkedList.removeAt(0)
        // 리스트의 제일 앞에꺼 삭제
        linkedList.remove()
        // 리스트의 제일 마지막부분 삭제
        linkedList.removeLast()
    }
    
    class hashMap{
        // hashmap 은 key, value 방식으로 저장
        val hashmap = HashMap<String, Any>()
        
        // name, age 라는 key 와 hwang, 27이라는 value를 가진값 저장
        hashmap.put("name", "hwang")
        hashmap.put("age", 27)
    
        // name이라는 key를 가진 value 추출
        hashmap.containsKey("name")
        // age라는 값 추출
        hashmap.get("age")

        // name 이라는 key 를 가진값 삭제
        hashmap.remove("name")
        // age 라는 key를 가진 value 를 변경
        hashmap.replace("age", 26)

        // hashmap 초기화
        hashmap.clear()
    }
    
    data class Node(
        val data: Int, 
        var left: Node? = null, 
        var right: Node? = null
    )
    class tree(val root: Node)
    
    fun main(){
        val tree = tree(Node(5))
        tree.root.left = Node(3, null, Node(4))
        tree.root.right = Node(7)

        // preorder (부모 -> 왼쪽 -> 오른쪽 탐색) 
        fun preorder(){
            fun preorderInternal(node: Node){
                print("${node.data}")
                if(node.right != null) preorderInternal(node.right!!)
                if(node.left != null) preorderInternal(node.left!!)
            }
            preorderInternal(tree.root)
        }
        // inorder (왼쪽 -> 부모 -> 오른쪽)
        fun inorder(){
            fun inorderInternal(node: Node){
                if(node.left != null) inorderInternal(node.left!!)
                print("${node.data}")
                if(node.right != null) inorderInternal(node.right!!)
            }
            inorderInternal(tree.root)
        }
        // postorder (왼쪽 -> 오른쪽 -> 부모)
        fun postorder(){
            fun postorderInternal(node: Node){
                if(node.left != null) postorderInternal(node.left!!)
                if(node.right != null) postorderInternal(node.right!!)
                print("${node.data}")
            }
            postorderInternal(tree.root)
        }
    }
}



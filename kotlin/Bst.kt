// Kotlin BST
data class Node(
    val value : Int,
    var left: Node? = null,
    var right: Node? = null
)

class TreeManager{
    var root: Node? = null

    fun put(value: Int){
        if(root == null){
            root = Node(value = value)
            return
        }

        var parent = root
        while(true){
            if(parent!!.value < value){
                if(parent.right != null){ 
                    parent = parent.right 
                }
                else{
                    parent.right = Node(value = value)
                    break
                }
            }
            else{
                if(parent.left != null){
                    parent = parent.left
                }
                else{
                    parent.left = Node(value = value)
                    break
                }
            }
        }
    }

    fun get(value: Int): Node?{
        if(root == null){ 
            return null 
        }
        
        var node = root
        while(node != null){
            if(node.value == value){
                return node
            }
            node = if(node.value < value){
                node.right
            }
            else{
                node.left
            }
        }
        return null
    }

    fun delete(value: Int): Boolean{
        if(root == null){
            return false
        }

        if(root!!.value == value && root!!.left == null && root!!.right == null){
            root = null
            return true
        }

        var parent = root!!
        var cur = root
        while(cur != null){
            if(cur.value == value) break
            else if(cur.value < value){
                parent = cur
                cur = cur.right
            }
            else{
                parent = cur
                cur = cur.left
            }

            if(cur == null) return false

            if(cur.left == null && cur.right == null){
                if(parent.value > cur.value){
                    parent.left = null
                }
                else{
                    parent.right = null
                }
            }

            if(cur.left != null && cur.right == null){
                if(parent.value > cur.value){
                    parent.left = null
                }
                else{
                    parent.right = null
                }
            }
            else{
                if(parent.value > cur.value){
                    parent.left = null
                }
                else{
                    parent.right = null
                }
            }

            var changeParent = cur.right!!
            var change = cur.right!!

            while(change.left != null){
                changeParent = change
                change = change.left!!
            }

            if(parent.value > cur.value){
                if(change.right == null){
                    parent.left = change
                    changeParent.left = null
                    change.left = cur.left
                    change.right = cur.right
                }
                else{
                    parent.left = change
                    changeParent.left = change.right
                    change.left = cur.left
                    change.right = cur.right
                }
            }
            else{
                if(change.right == null){
                    parent.right = change
                    changeParent.left = null
                    change.left = cur.left
                    change.right = cur.right
                }
                else{
                    parent.right = change
                    changeParent.left = change.right
                    change.left = cur.left
                    change.right = cur.right
                }
            }
        }
        return true
    }
}
# bst로 특정값보다 큰값들, 작은값들의 갯수를 계산한다. insert할때 지나는 node의 size값을 1씩증가
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.size = 0

class BST(object):
    def __init__(self):
        self.root = None
    
    #insert
    def insert(self,data):
        self.root = self._insert_value(self.root,data)

    def _insert_value(self,node,data):
        if node is None:
            node = Node(data)    
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left,data)
            else:
                node.right = self._insert_value(node.right,data)
        node.size+=1
        return node

    #find(T/F)
    def find(self,key):
        return self._find_value(self.root,key)

    def _find_value(self,node,key):
        if node is None:
            return False
        if node.data == key:
            return node.size
        elif key < node.data:
            return self._find_value(node.left,key)
        else:
            return self._find_value(node.right,key)
    #delete(T/F)
    def delete(self,data):
        self.root,deleted = self._delete_value(self.root,data)
        return deleted
    
    def _delete_value(self,node,key):
        if node is None:
            return node,False

        deleted = False
        if node.data == key:
            deleted=True
            if node.left and node.right:
                parent,child = node,node.right
                while child.left is not None:
                    parent,child = child, child.left
                child.left = node.left
                if parent!= node:
                    parent.right = child.right
                    child.left = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left = self._delete_value(node.left,key)
        else:
            node.right = self._delete_value(node.right,key)
        return node,deleted
    
    #작거나 같은 값을 찾는 메소드
    def find_not_bigger(self,key):
        return self._find_not_bigger_value(self.root,key)

    def _find_not_bigger_value(self,node,key):
        if node is None:
            return 0
        if node.data == key:
            if node.left is None:
                return 1
            else:
                return node.left.size+1
        elif key < node.data:
            return self._find_not_bigger_value(node.left,key)
        else:
            if node.left is None:
                return self._find_not_bigger_value(node.right,key)+1
            else:
                return self._find_not_bigger_value(node.right,key)+node.left.size+1

    #크거나 같은 값을 찾는 메소드
    def find_not_smaller(self,key):
        return self._find_not_smaller_value(self.root,key)
    
    def _find_not_smaller_value(self,node,key):
        if node is None:
            return 0
        
        if key == node.data:
            if node.right is None:
                return 1
            else:
                return node.right.size+1     
        elif key < node.data:
            if node.right is None:
                return self._find_not_smaller_value(node.left,key)+1
            else:
                return self._find_not_smaller_value(node.left,key)+node.right.size+1
        else:
            return self._find_not_smaller_value(node.right,key)

array = [1,10,30,20,2,8,7,9,12]
bst = BST()

for x in array:
    bst.insert(x)

for x in array:
    print(bst.find(x))

print(bst.find_not_bigger(30))
print(bst.find_not_smaller(1))


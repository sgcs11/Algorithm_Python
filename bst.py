#Binary Serach Tree Node 선언 parent, left_child, right_child, subtree_size, key로 구성
#주의할 것은 파라미터 변수에 값을 할당하면 새로운 주소로 바뀌므로 C/JAVA와 다르게 return Node를 해서 값을 할당해야됨
class Node(object):
    def __init__(self, parent, data):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
    
class BinarySearchTree(object):
    def __init__(self):
        self.root=None
    
    #insert하는 메소드
    def insert(self,data):
        self.root = self._insert_value(self.root,None,data)
    
    def _insert_value(self,node,psroot,data):
        if node is None:
            node = Node(psroot,data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left,node,data)
            else:
                node.right = self._insert_value(node.right,node,data)
        return node

    #find하는 메소드
    def find(self,data):
        return self._find_value(self.root,data)

    def _find_value(self,node,key):
        if node is None:
            return False
        if node.data == key:
            return True
        elif key < node.data:
            return self._find_value(node.left,key)
        else:
            return self._find_value(node.right,key)

    #delete하는 메소드(삭제한 노드의 subtree 중 오른쪽의 가장 왼쪽아래 or 왼쪽의 가장 오른쪽 아래 node를 가져오면 삭제 구현됨)
    def delete(self,key):
        self.root,deleted = self._delete_value(self.root,key)
        return deleted
    
    def _delete_value(self,node,key):
        if node is None:
            return node,False
        
        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent,child = node,node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node.left.parent = child
                node.right.parent = child
                child.parent = node.parent
                node = child
            elif node.left or node.right:
                if node.left:
                    node.left.parent = node.parent
                else:
                    node.right.parent = node.parent
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left,key)
        else:
            node.right, deleted = self._delete_value(node.right,key)
        return node, deleted

    #부모 출력
    def find_parent(self,key):
        return self._find_parent_value(self.root,key)
    
    def _find_parent_value(self,node,key):
        if node is None:
            return "no such key"
        if node.data == key:
            if node.parent is None:
                return "no parent"
            else:
                return node.parent.data
        elif key < node.data:
            return self._find_parent_value(node.left,key)
        else:
            return self._find_parent_value(node.right,key)
        


array = [10,4,14,15,16,13]

bst = BinarySearchTree()

print("insert : ")
for x in array:
    bst.insert(x)

bst.delete(16)

print("find :")
for x in array:
    print(bst.find_parent(x))

# print("delete : ")
# for x in array:
#     print(bst.delete(x))

# print("find : ")
# for x in array:
#     print(bst.find(x))

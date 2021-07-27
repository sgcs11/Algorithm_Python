class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    node.height = max(height(node.left),height(node.right))+1

class AVL(object):
    def __init__(self):
        self.root = None

    def left_rotate(self,x):
        y = x.right
        x.right = y.left
        y.left = x
        update_height(x)
        update_height(y)
        return y
    
    def right_rotate(self,x):
        y = x.left
        x.left = y.right
        y.right = x
        update_height(x)
        update_height(y)
        return y

    def rebalance(self,node):
        #삽입 노드부터 부모까지 올라가며 avl형태를 만듬
        if node is not None:
            update_height(node)
            if height(node.left) >= 2+height(node.right):
                if height(node.left.left)>=height(node.left.right):
                    node = self.right_rotate(node)
                else:
                    node.left = self.left_rotate(node.left)
                    node = self.right_rotate(node)
            elif height(node.right) >= 2+height(node.left):
                if height(node.right.right)>=height(node.right.left):
                    node = self.left_rotate(node)
                else:
                    node.right = self.right_rotate(node.right)
                    node = self.left_rotate(node)
        return node

    #insert하는 메소드
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
        return self.rebalance(node)

    #해당 원소 있는지 T/F로 리턴
    def find(self,key):
        return self._find_value(self.root,key)
    
    def _find_value(self,node,key):
        if node is None:
            return False
        else:
            if node.data == key:
                return True
            elif key < node.data:
                return self._find_value(node.left,key)
            else:
                return self._find_value(node.right,key)

    #해당 원소 높이 리턴
    def find_height(self,key):
        return self._find_height_value(self.root,key)
    
    def _find_height_value(self,node,key):
        if node is None:
            return -1
        else:
            if node.data == key:
                return node.height
            elif key < node.data:
                return self._find_height_value(node.left,key)
            else:
                return self._find_height_value(node.right,key)

    #delete에서 삭제하는 node를 대체할 node의 부모와의 연결 끊고 대신 node.right을 전달
    def delete_min(self,node):
        if node.left is None:
            return node.right
        node.left = self.delete_min(node.left)
        update_height(node)
        return self.rebalance(node)

    #delete할 node를 대체하는 최솟값 node 반환하는 메소드
    def minimum(self,node):
        if node.left is None:
            return node
        return self.minimum(node.left)

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
                target = node #임시저장
                node = self.minimum(target.right)
                node.right = self.delete_min(target.right)
                node.left = target.left
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left,key)
        else:
            node.right, deleted = self._delete_value(node.right,key)
        return self.rebalance(node), deleted

    #결과 출력
    def print_all(self):
        print(f"root : {self.root.data}")
        self._print_all_value(self.root)
    
    def _print_all_value(self,node):
        if node is None:
            return
        self._print_all_value(node.left)
        print(node.data,",",node.height,end="   ")
        self._print_all_value(node.right)


array = [1,2,3,4,5,6,7,8]
# ,14,13]
avl=AVL()
for x in array:
    avl.insert(x)
    avl.print_all()
    print()

avl.delete(4)
avl.print_all()
print()
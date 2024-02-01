class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MyBinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)

    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, current_node):
        if current_node is None:
            return False
        if data == current_node.data:
            return True
        elif data < current_node.data:
            return self._search(data, current_node.left)
        else:
            return self._search(data, current_node.right)

    def peek(self):
        if self.root is not None:
            return self.root.data
        else:
            return None

    def size(self):
        return self._size(self.root)

    def _size(self, current_node):
        if current_node is None:
            return 0
        return 1 + self._size(current_node.left) + self._size(current_node.right)

    def is_empty(self):
        return self.root is None


tree = MyBinaryTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(7)
tree.insert(12)

print("Search for tree with data 5 : ",tree.search(5))   
print("searching for tree with dara 8 : ",tree.search(8))   
print("tree peek value : ",tree.peek())      
print("Tree size output : ",tree.size())      
print("Is tree empty : ",tree.is_empty())

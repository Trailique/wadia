class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MyBinaryTree:
    def __init__(self, data=None):
        if data is not None:
            self.root = TreeNode(data)
        else:
            self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self._insert_recursive(current_node.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current_node, data):
        if current_node is None:
            return False
        if current_node.data == data:
            return True
        elif data < current_node.data:
            return self._search_recursive(current_node.left, data)
        else:
            return self._search_recursive(current_node.right, data)

    def peek(self):
        if not self.root:
            raise Exception("Cannot peek into an empty tree")
        return self.root.data

    def size(self):
        return self._size_recursive(self.root)

    def _size_recursive(self, current_node):
        if current_node is None:
            return 0
        return 1 + self._size_recursive(current_node.left) + self._size_recursive(current_node.right)

    def is_empty(self):
        return self.root is None


binary_tree = MyBinaryTree(5)
binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.insert(2)

print("Binary tree size:", binary_tree.size())  
print("Data of the root node:", binary_tree.peek())  

search_result = binary_tree.search(7)
print("Is 7 present in the tree?", search_result)  

empty_tree = MyBinaryTree()
print("Is the empty tree empty?", empty_tree.is_empty())  

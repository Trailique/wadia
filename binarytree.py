class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MyBinaryTree:
    def __init__(self, data):
        self.root = TreeNode(data)

    def insert(self, data):
        self._insert(self.root, data)

    def _insert(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self._insert(current_node.left, data)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self._insert(current_node.right, data)
        else:
            # Duplicates are not allowed in this example
            raise ValueError("Duplicate data is not allowed in the tree")

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, current_node, data):
        if current_node is None:
            return False
        if data == current_node.data:
            return True
        elif data < current_node.data:
            return self._search(current_node.left, data)
        else:
            return self._search(current_node.right, data)

    def peek(self):
        if self.is_empty():
            raise ValueError("Cannot peek from an empty tree")
        return self.root.data

    def size(self):
        return self._size(self.root)

    def _size(self, current_node):
        if current_node is None:
            return 0
        return 1 + self._size(current_node.left) + self._size(current_node.right)

    def is_empty(self):
        return self.root is None

binary_tree = MyBinaryTree(5)
binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.insert(2)
binary_tree.insert(4)
binary_tree.insert(6)
binary_tree.insert(8)

print("Binary Tree:")
print("  5")
print(" / \\")
print("3   7")
print("/\\  /\\")
print("2 4 6 8")

print("Size:", binary_tree.size())
print("Is empty:", binary_tree.is_empty())
print("Peek:", binary_tree.peek())

print("Search for 6:", binary_tree.search(6))
print("Search for 10:", binary_tree.search(10))

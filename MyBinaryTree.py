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
        self._size = 1 if data is not None else 0

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            self._size += 1
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
                self._size += 1
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
                self._size += 1
            else:
                self._insert_recursive(node.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def peek(self):
        if self.root:
            return self.root.data
        return None

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

# Example Usage
binary_tree = MyBinaryTree()

print("Is the tree empty?", binary_tree.is_empty())  # Output: True

binary_tree.insert(10)
binary_tree.insert(5)
binary_tree.insert(15)

print("Size of the binary tree:", binary_tree.size())  # Output: 3
print("Root node of the binary tree:", binary_tree.peek())  # Output: 10

print("Is 5 present in the binary tree?", binary_tree.search(5))  # Output: True
print("Is 20 present in the binary tree?", binary_tree.search(20))  # Output: False

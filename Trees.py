class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MyBinaryTree:
    def __init__(self, data=None):
        self.root = None
        self.node_count = 0
        if data is not None:
            self.root = TreeNode(data)
            self.node_count = 1

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
        self.node_count += 1

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left:
                self._insert_recursive(current_node.left, data)
            else:
                current_node.left = TreeNode(data)
        else:
            if current_node.right:
                self._insert_recursive(current_node.right, data)
            else:
                current_node.right = TreeNode(data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current_node, data):
        if not current_node:
            return False
        if current_node.data == data:
            return True
        elif data < current_node.data:
            return self._search_recursive(current_node.left, data)
        else:
            return self._search_recursive(current_node.right, data)

    def peek(self):
        if self.root:
            return self.root.data
        else:
            return None

    def size(self):
        return self.node_count

    def is_empty(self):
        return self.node_count == 0


# Case Study
tree = MyBinaryTree()

print("Is Empty:", tree.is_empty())  # Output: True

tree.insert(5)
tree.insert(3)
tree.insert(7)

print("Peek:", tree.peek())  # Output: 5
print("Size:", tree.size())  # Output: 3
print("Is Empty:", tree.is_empty())  # Output: False

print("Search 3:", tree.search(3))  # Output: True
print("Search 6:", tree.search(6))  # Output: False

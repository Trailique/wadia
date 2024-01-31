class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MyBinaryTree:
    def __init__(self, data):
        self.root = TreeNode(data)

    def insert(self, data):
        self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self._insert_recursive(current_node.left, data)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self._insert_recursive(current_node.right, data)


    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current_node, data):
        if current_node is None:
            return False
        if data == current_node.data:
            return True
        elif data < current_node.data:
            return self._search_recursive(current_node.left, data)
        else:
            return self._search_recursive(current_node.right, data)

    def peek(self):
        if self.root is None:
            return None
        return self.root.data

    def size(self):
        return self._size_recursive(self.root)

    def _size_recursive(self, current_node):
        if current_node is None:
            return 0
        return 1 + self._size_recursive(current_node.left) + self._size_recursive(current_node.right)

    def is_empty(self):
        return self.root is None

my_binary_tree = MyBinaryTree(10)
my_binary_tree.insert(5)
my_binary_tree.insert(15)
my_binary_tree.insert(3)

print("Size:", my_binary_tree.size())
print("Search for 5:", my_binary_tree.search(5))
print("Root node data:", my_binary_tree.peek())
print("Is empty:", my_binary_tree.is_empty())

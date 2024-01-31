class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class MyBinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)
        else:
            # Handle the case where the data already exists (optional)
            pass

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current, data):
        if current is None or current.data == data:
            return current
        elif data < current.data:
            return self._search_recursive(current.left, data)
        else:
            return self._search_recursive(current.right, data)

    def peek(self):
        if self.root:
            return self.root.data
        else:
            return None

    def size(self):
        return self._size_recursive(self.root)

    def _size_recursive(self, current):
        if current is None:
            return 0
        return 1 + self._size_recursive(current.left) + self._size_recursive(current.right)

    def is_empty(self):
        return self.root is None


# Example Usage:
binary_tree = MyBinaryTree(5)

binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.insert(2)
binary_tree.insert(4)
binary_tree.insert(6)
binary_tree.insert(8)

print("Peek:", binary_tree.peek())
print("Size:", binary_tree.size())
print("Is Empty:", binary_tree.is_empty())

search_result = binary_tree.search(4)
if search_result:
    print("Node with data 4 found in the tree.")
else:
    print("Node with data 4 not found in the tree.")

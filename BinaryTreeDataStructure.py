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
        if data == current_node.data:
            return True
        elif data < current_node.data:
            return self._search_recursive(current_node.left, data)
        else:
            return self._search_recursive(current_node.right, data)

    def peek(self):
        if self.root:
            return self.root.data
        else:
            print("Error: Cannot peek from an empty tree.")
            return None

    def size(self):
        return self._size_recursive(self.root)

    def _size_recursive(self, current_node):
        if not current_node:
            return 0
        return 1 + self._size_recursive(current_node.left) + self._size_recursive(current_node.right)

    def is_empty(self):
        return self.root is None

    def print_tree(self):
        self._print_tree_recursive(self.root)

    def _print_tree_recursive(self, current_node):
        if not current_node:
            return
        self._print_tree_recursive(current_node.left)
        print(current_node.data, end=' ')
        self._print_tree_recursive(current_node.right)

binary_tree = MyBinaryTree(10)

#Inserts a new node with the given data into the tree with current node 
binary_tree.insert(6)
binary_tree.insert(15)
binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.insert(12)
binary_tree.insert(8)

#Returns the current number of nodes in the tree.
print("Binary tree size:", binary_tree.size())
print("Is binary tree empty?", binary_tree.is_empty())

#Returns the data of the root node without removing it.
print("Peek at the root node:", binary_tree.peek())

#Searches for a node with the given data in the tree.
data_to_search = 7
if binary_tree.search(data_to_search):
    print(f"Node with data {data_to_search} found in the tree.")
else:
    print(f"Node with data {data_to_search} not found in the tree.")

print("Binary tree in-order traversal:")
binary_tree.print_tree()

print("\nBinary Tree:")
print("  6")
print(" / \\")
print("15   3")
print("/\\  /")
print("7 12 8")

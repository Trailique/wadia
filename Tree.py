class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MyBinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = new_node
                return
            elif current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.left)
                queue.append(current.right)

    def search(self, data):
        if self.root is None:
            return False
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.data == data:
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False

    def peek(self):
        if self.root is None:
            raise ValueError("Cannot peek from an empty tree")
        return self.root.data

    def size(self):
        if self.root is None:
            return 0
        queue = [self.root]
        count = 0
        while queue:
            current = queue.pop(0)
            count += 1
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return count

    def is_empty(self):
        return self.root is None

# Example usage:
binary_tree = MyBinaryTree(5)
binary_tree.insert(3)
binary_tree.insert(8)

print(binary_tree.size())  # Output: 3
print(binary_tree.peek())  # Output: 5
print(binary_tree.search(3))  # Output: True
print(binary_tree.search(10))  # Output: False

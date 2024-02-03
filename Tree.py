class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class MyBinaryTree:
    def __init__(self, data):
        self.root = TreeNode(data)
        self.size = 1

    def insert(self, data):
        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
            self.size += 1
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = new_node
                self.size += 1
                return
            elif not node.right:
                node.right = new_node
                self.size += 1
                return
            else:
                queue.append(node.left)
                queue.append(node.right)

    def search(self, data):
        if not self.root:
            return False

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.data == data:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def peek(self):
        if not self.root:
            return None
        return self.root.data

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0


# Testing the MyBinaryTree class
if __name__ == "__main__":
    binary_tree = MyBinaryTree(1)

    print("Is empty?", binary_tree.is_empty())  # False
    print("Peek:", binary_tree.peek())  # 1
    print("Size:", binary_tree.size())  # 1

    binary_tree.insert(2)
    binary_tree.insert(3)
    binary_tree.insert(4)

    print("Is empty?", binary_tree.is_empty())  # False
    print("Peek:", binary_tree.peek())  # 1
    print("Size:", binary_tree

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def delete_node(self, data):
        if not self.head:
            raise Exception("Cannot delete from an empty list")

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return

        prev = self.head
        current = self.head.next
        while current:
            if current.data == data:
                prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

        raise ValueError("Node with data '{}' not found".format(data))

    def peek(self):
        if not self.head:
            return None
        return self.head.data

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0


# Testing the MyLinkedList class
if __name__ == "__main__":
    linked_list = MyLinkedList()

    print("Is empty?", linked_list.is_empty())  # True
    # print(linked_list.peek())  # Should return None
    # linked_list.delete_node(5)  # Should raise an exception

    linked_list.add_node(5)
    linked_list.add_node(10)
    linked_list.add_node(15)

    print("Is empty?", linked_list.is_empty())  # False
    print("Size:", linked_list.size())  # 3
    print("Peek:", linked_list.peek())  # 5

    linked_list.delete_node(10)
    print("Size after deleting 10:", linked_list.size())  # 2

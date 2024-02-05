class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_node(self, data):
        if self.head is None:
            raise ValueError("Cannot delete from an empty list")
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError(f"Node with data {data} not found")

    def peek(self):
        if self.head is None:
            raise ValueError("Cannot peek from an empty list")
        return self.head.data

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None

# Example usage:
linked_list = MyLinkedList()
print(linked_list.is_empty())  # Output: True

linked_list.add_node(5)
linked_list.add_node(10)
linked_list.add_node(15)

print(linked_list.size())  # Output: 3
print(linked_list.peek())  # Output: 5

linked_list.delete_node(10)
print(linked_list.size())  # Output: 2
print(linked_list.is_empty())  # Output: False

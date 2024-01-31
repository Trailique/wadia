class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_node(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next

    def peek(self):
        if self.head:
            return self.head.data
        else:
            return None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None


# Case Study:
linked_list = MyLinkedList()

# Adding nodes
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)

# Printing the size and elements
print("Size:", linked_list.size())      # Output: 3
print("Is Empty:", linked_list.is_empty())  # Output: False
print("Peek:", linked_list.peek())      # Output: 1

# Deleting a node
linked_list.delete_node(2)

# Printing the size and elements after deletion
print("Size after deletion:", linked_list.size())  # Output: 2
print("Is Empty after deletion:", linked_list.is_empty())  # Output: False
print("Peek after deletion:", linked_list.peek())  # Output: 1

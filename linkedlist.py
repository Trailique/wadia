class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_node(self, data):
        if not self.head:
            print("Error: List is empty. Cannot delete from an empty list.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print(f"Error: Node with data '{data}' not found in the list.")

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


# Example Usage:
linked_list = MyLinkedList()

linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)

print("Current Linked List:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

print("Peek:", linked_list.peek())
print("Size:", linked_list.size())
print("Is Empty:", linked_list.is_empty())

linked_list.delete_node(2)
linked_list.delete_node(1)
linked_list.delete_node(3)

print("After Deletions:")
print("Peek:", linked_list.peek())
print("Size:", linked_list.size())
print("Is Empty:", linked_list.is_empty())

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
            print("Error: List is empty. Cannot delete.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            print(f"Error: Node with data '{data}' not found.")

    def peek(self):
        if not self.head:
            print("Error: List is empty. Cannot peek.")
            return None
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


linked_list = MyLinkedList()

#Adds a new node with the given data to the end of the list
linked_list.add_node(4)
linked_list.add_node(5)
linked_list.add_node(6)
linked_list.add_node(7)

print("Current Linked List:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

#Returns the current number of nodes in the linked list.
print("Linked list size:", linked_list.size())
print("Is linked list empty?", linked_list.is_empty())

#Returns the data of the first node without removing it.
print("Peek at the first node:", linked_list.peek())

#Deletes the first occurrence of a node with the given data.
linked_list.delete_node(4)
linked_list.delete_node(7)

#Prints the linked list size after deleting nodes
print("Linked list size after deletion:", linked_list.size())


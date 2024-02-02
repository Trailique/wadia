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
            raise Exception("Cannot delete from an empty linked list")

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            raise ValueError(f"Node with data {data} not found")

    def peek(self):
        if not self.head:
            raise Exception("Cannot peek into an empty linked list")
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
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)

print("Linked list size:", linked_list.size())  
print("Data of the first node:", linked_list.peek()) 

linked_list.delete_node(2)
print("Updated linked list size:", linked_list.size()) 
print("Is linked list empty?", linked_list.is_empty())  

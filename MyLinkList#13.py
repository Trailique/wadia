class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = Node(None) 
        self.tail = self.head
        self._size = 0 

    def add_node(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self._size += 1

    def delete_node(self, data):
        prev = self.head
        current = self.head.next
        while current:
            if current.data == data:
                prev.next = current.next
                if current == self.tail:
                    self.tail = prev
                del current
                self._size -= 1
                return
            prev = current
            current = current.next

    def peek(self):
        if self.head.next:
            return self.head.next.data
        return None

    def get_size(self): 
        return self._size

    def is_empty(self):
        return self._size == 0

# Example Usage
linked_list = MyLinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)

print("Size of the linked list:", linked_list.get_size())  
print("First element of the linked list:", linked_list.peek()) 

linked_list.delete_node(2)

print("Size of the linked list after deletion:", linked_list.get_size()) 
print("First element of the linked list after deletion:", linked_list.peek())  
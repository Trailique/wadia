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
            print("List is empty. Cannot delete.")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if not current.next:
            print(f"Node with data {data} not found.")
            return

        current.next = current.next.next

    def peek(self):
        if self.head:
            return self.head.data
        else:
            print("List is empty.")
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


linked_list = MyLinkedList()
print("Linked list is empty : ",linked_list.is_empty())  

linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)
print("Linked list size : ",linked_list.size())  
print("is linked list empty : ",linked_list.is_empty()) 
print("peek data value : ",linked_list.peek())  

linked_list.delete_node(2)
print("Size after delet 1 node : ",linked_list.size())  
print("Peek data value : ",linked_list.peek())  

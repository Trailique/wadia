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
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

        print(f"Node with data {data} not found.")

    def peek(self):
        if not self.head:
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
    
my_linked_list = MyLinkedList()
my_linked_list.add_node(1)
my_linked_list.add_node(2)
my_linked_list.add_node(3)

print("Size:", my_linked_list.size())
print("First node data:", my_linked_list.peek())

my_linked_list.delete_node(2)
print("Is empty:", my_linked_list.is_empty())
print("Size after deletion:", my_linked_list.size())

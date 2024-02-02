class MyQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue underflow: cannot dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise ValueError("Cannot peek from an empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.items)
print("Size:", queue.size())
print("Peek:", queue.peek())

dequeued_item = queue.dequeue()
print("Dequeued:", dequeued_item)
print("Queue after dequeue:", queue.items)
print("Is empty:", queue.is_empty())

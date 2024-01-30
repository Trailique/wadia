class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            raise IndexError("dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0] if self.queue else None

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return not self.queue



queue = MyQueue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Current Queue:", queue.queue)
print("Peek:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Size:", queue.size())
print("Is Empty:", queue.is_empty())

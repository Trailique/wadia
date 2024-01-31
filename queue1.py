class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


queue = MyQueue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Current Queue:", queue.queue)
print("Peek:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Size:", queue.size())
print("Is Empty:", queue.is_empty())

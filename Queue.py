class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek from an empty queue")
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

# Example usage:
queue = MyQueue()
print(queue.is_empty())  # True

queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)

print(queue.size())  # 3
print(queue.peek())  # 5

print(queue.dequeue())  # 5
print(queue.size())  # 2
print(queue.is_empty())  # False

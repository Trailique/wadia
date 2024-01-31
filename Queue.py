class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue underflow: Cannot dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty: Cannot peek at an empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage:
my_queue = MyQueue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue size:", my_queue.size())  # Output: 3

print("Peek:", my_queue.peek())  # Output: 1

print("Dequeue:", my_queue.dequeue())  # Output: 1

print("Is empty?", my_queue.is_empty())  # Output: False

print("Queue size:", my_queue.size())  # Output: 2

# Trying to dequeue from an empty queue (queue underflow)
empty_queue = MyQueue()
try:
    empty_queue.dequeue()
except IndexError as e:
    print(e)  # Output: Queue underflow: Cannot dequeue from an empty queue

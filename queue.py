class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue underflow: cannot dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0


# Testing the MyQueue class
if __name__ == "__main__":
    queue = MyQueue()

    # Test operations on an empty queue
    print("Is empty?", queue.is_empty())  # True
    # print(queue.dequeue())  # Should raise an exception
    # print(queue.peek())  # Should return None

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Is empty?", queue.is_empty())  # False
    print("Size:", queue.size())  # 3
    print("Peek:", queue.peek())  # 1

    print("Dequeueing elements:")
    while not queue.is_empty():
        print(queue.dequeue())

    print("Is empty?", queue.is_empty())  # True

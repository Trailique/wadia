class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


queue = MyQueue()


queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)


print("Queue:", queue.queue)


print("Peek:", queue.peek()) 


print("Dequeue:", queue.dequeue())  


print("Updated Queue:", queue.queue)


print("Size:", queue.size()) 


print("Is Empty:", queue.is_empty())  


print("Dequeue:", queue.dequeue()) 
print("Dequeue:", queue.dequeue()) 


print("Is Empty:", queue.is_empty())  

#Edge case
# print("Dequeue:", queue.dequeue())

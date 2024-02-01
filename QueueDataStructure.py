class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: Cannot dequeue from an empty queue.")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek from an empty queue.")
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

queue = MyQueue()

#Adding items
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

#Prints the current number of items in th queue 
print("Queue size:", queue.size())
print("Is queue empty?", queue.is_empty())

#Returning the item at the front of the queue
front_item = queue.peek()
print("Front item:", front_item)

#Removing and returning the item from the front of the queue.
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)

#Returning the current number of items in the queue after dequeuing
print("Queue size after dequeue:", queue.size())
print("Is queue empty after dequeue?", queue.is_empty())

class Queue:
    def __init__(self):
        self.arr=[]
        
    def enqueue(self,item):
        self.arr.append(item)
    
    def dequeue(self):
        if len(self.arr) >0:
            return self.arr.pop(0)
        else:
            return None
    
    def peek(self):
        if len(self.arr) >0:
            return self.arr[0]
        else:
            return None
    
    def size(self):
        return len(self.arr)

    def is_empty(self):
        return len(self.arr) == 0

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size()) 
print("Front of the queue:", queue.peek()) 

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)  
print("Updated queue size:", queue.size()) 
print("Is queue empty?", queue.is_empty())
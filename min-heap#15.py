class MyMinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up()

    def extract_min(self):
        if not self.is_empty():
            # Swap the root (minimum element) with the last element
            self._swap(0, len(self.heap) - 1)
            # Pop the last element (original root)
            min_element = self.heap.pop()
            # Restore the heap property
            self._heapify_down()
            return min_element
        else:
            raise IndexError("extract_min from an empty heap")

    def peek(self):
        if not self.is_empty():
            return self.heap[0]
        else:
            raise IndexError("peek from an empty heap")

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self):
        current_index = len(self.heap) - 1
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if self.heap[current_index] < self.heap[parent_index]:
                self._swap(current_index, parent_index)
                current_index = parent_index
            else:
                break

    def _heapify_down(self):
        current_index = 0
        while True:
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
            smallest = current_index

            if (left_child_index < len(self.heap) and
                    self.heap[left_child_index] < self.heap[smallest]):
                smallest = left_child_index

            if (right_child_index < len(self.heap) and
                    self.heap[right_child_index] < self.heap[smallest]):
                smallest = right_child_index

            if smallest != current_index:
                self._swap(current_index, smallest)
                current_index = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Example usage:
min_heap = MyMinHeap()

print("Is min-heap empty?", min_heap.is_empty())  

min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(4)
min_heap.insert(2)

print("Min element in the heap:", min_heap.peek())  
print("Size of the heap:", min_heap.size())  

min_element = min_heap.extract_min()
print("Extracted min element:", min_element) 
print("Is min-heap empty?", min_heap.is_empty())  
print("Size of the heap:", min_heap.size())  

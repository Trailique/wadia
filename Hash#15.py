
class MyMinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if self.is_empty():
            print("Error: Heap underflow. Cannot extract from an empty heap.")
            return None

       
        self._swap(0, len(self.heap) - 1)
        min_item = self.heap.pop()  
        self._heapify_down(0)  
        return min_item

    def peek(self):
        if self.is_empty():
            print("Error: Cannot peek from an empty heap.")
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

min_heap = MyMinHeap()

min_heap.insert(4)
min_heap.insert(2)
min_heap.insert(7)
min_heap.insert(1)
min_heap.insert(9)

print("Min-heap size:", min_heap.size())
print("Is min-heap empty?", min_heap.is_empty())

print("Peek at the smallest item:", min_heap.peek())


extracted_min = min_heap.extract_min()
print("Extracted min:", extracted_min)


print("Min-heap size after extraction:", min_heap.size())
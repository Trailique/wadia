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

        # Swap the root (min element) with the last element
        self._swap(0, len(self.heap) - 1)
        min_item = self.heap.pop()  # Remove the min element
        self._heapify_down(0)  # Restore heap property
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

# Example usage:
min_heap = MyMinHeap()

#Inserts an item into the min-heap.
min_heap.insert(4)
min_heap.insert(2)
min_heap.insert(7)
min_heap.insert(1)
min_heap.insert(9)

#Returns the current number of elements in the min-heap.
print("Min-heap size:", min_heap.size())
print("Is min-heap empty?", min_heap.is_empty())

#Returns the smallest item in the min-heap without removing it.
print("Peek at the smallest item:", min_heap.peek())

#Removes and returns the smallest item in the min-heap.
extracted_min = min_heap.extract_min()
print("Extracted min:", extracted_min)

#Prints the min heap size after extraction
print("Min-heap size after extraction:", min_heap.size())

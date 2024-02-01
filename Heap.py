class MyMinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._percolate_up(len(self.heap) - 1)

    def _percolate_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Cannot extract from an empty heap")
        min_item = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self._percolate_down(0)
        return min_item

    def _percolate_down(self, index):
        while 2 * index + 1 < len(self.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            min_child_index = left_child_index
            if (right_child_index < len(self.heap) and
                    self.heap[right_child_index] < self.heap[left_child_index]):
                min_child_index = right_child_index
            if self.heap[index] > self.heap[min_child_index]:
                self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]
                index = min_child_index
            else:
                break

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek from an empty heap")
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

# Example usage:
heap = MyMinHeap()
print(heap.is_empty())  # Output: True

heap.insert(5)
heap.insert(10)
heap.insert(3)

print(heap.size())  # Output: 3
print(heap.peek())  # Output: 3

print(heap.extract_min())  # Output: 3
print(heap.size())  # Output: 2
print(heap.is_empty())  # Output: False

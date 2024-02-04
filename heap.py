class MyMinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up()

    def extract_min(self):
        if self.is_empty():
            raise IndexError(
                "Heap underflow: cannot extract from an empty heap")

        min_item = self.heap[0]
        last_item = self.heap.pop()

        if not self.is_empty():
            self.heap[0] = last_item
            self._heapify_down()

        return min_item

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self):
        index = len(self.heap) - 1

        while index > 0:
            parent_index = (index - 1) // 2

            if self.heap[index] < self.heap[parent_index]:

                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:

                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break


min_heap = MyMinHeap()

min_heap.insert(3)
min_heap.insert(5)
min_heap.insert(1)
min_heap.insert(8)
min_heap.insert(2)

print("Current Min Heap:", min_heap.heap)

print("Extract Min:", min_heap.extract_min())
print("Peek:", min_heap.peek())
print("Size:", min_heap.size())
print("Is Empty:", min_heap.is_empty())
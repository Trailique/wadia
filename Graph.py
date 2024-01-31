from collections import defaultdict, deque

class MyGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.vertices += 1
        if v2 not in self.adj_list:
            self.vertices += 1
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def peek(self):
        if self.vertices == 0:
            return None
        return next(iter(self.adj_list))

    def size(self):
        return self.vertices

    def is_empty(self):
        return self.vertices == 0

# Example Usage
graph = MyGraph(0)

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)

print("DFS:", end=' ')
graph.dfs(1)  # Output: 1 2 4 3 5

print("\nBFS:", end=' ')
graph.bfs(1)  # Output: 1 2 3 4 5

print("\nPeek vertex:", graph.peek())  # Output: 1
print("Size of the graph:", graph.size())  # Output: 5

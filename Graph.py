from collections import defaultdict, deque

class MyGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def dfs(self, start):
        if start not in self.adj_list:
            raise ValueError("Starting vertex not in the graph")
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start):
        if start not in self.adj_list:
            raise ValueError("Starting vertex not in the graph")
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def peek(self):
        if not self.vertices:
            raise ValueError("Graph is empty")
        return next(iter(self.adj_list))

    def size(self):
        return len(self.vertices)

    def is_empty(self):
        return len(self.vertices) == 0

# Example usage:
graph = MyGraph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

print("DFS:", end=' ')
graph.dfs(0)
print()

print("BFS:", end=' ')
graph.bfs(0)
print()

print("Peek:", graph.peek())  # Output: 0
print("Size:", graph.size())  # Output: 5
print("Is Empty:", graph.is_empty())  # Output: False

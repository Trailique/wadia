from collections import defaultdict, deque

class MyGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def dfs(self, start):
        if self.is_empty():
            raise ValueError("Cannot perform DFS on an empty graph")

        visited = set()
        self._dfs(start, visited)

    def _dfs(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)

    def bfs(self, start):
        if self.is_empty():
            raise ValueError("Cannot perform BFS on an empty graph")

        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(neighbor for neighbor in self.graph[vertex] if neighbor not in visited)

    def peek(self):
        if self.is_empty():
            raise ValueError("Cannot peek from an empty graph")
        return next(iter(self.graph))

    def size(self):
        return len(self.graph)

    def is_empty(self):
        return self.size() == 0


graph = MyGraph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

print("Graph:")
print("0 - 1 - 3")
print("|")
print("2 - 4")

print("Size:", graph.size())
print("Is empty:", graph.is_empty())
print("Peek:", graph.peek())

print("DFS starting from vertex 0:")
graph.dfs(0)
print("\nBFS starting from vertex 0:")
graph.bfs(0)
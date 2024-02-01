from collections import defaultdict

class MyGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=' ')

            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def peek(self):
        if self.vertices == 0:
            print("Graph is empty.")
            return None
        for vertex in self.graph:
            return vertex

    def size(self):
        return self.vertices

    def is_empty(self):
        return self.vertices == 0


graph = MyGraph(4)


graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)


print("DFS:")
graph.dfs(0)
print("\n")


print("BFS:")
graph.bfs(0)
print("\n")


print("Peek:", graph.peek())


print("Size:", graph.size())


print("Is Empty:", graph.is_empty())

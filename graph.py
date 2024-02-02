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

    def _dfs_recursive(self, current, visited):
        visited.add(current)
        print(current, end=" ")

        for neighbor in self.graph[current]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            current = queue.pop(0)
            print(current, end=" ")

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def peek(self):
        if self.is_empty():
            return None
        return list(self.graph.keys())[0]

    def size(self):
        return len(self.graph)

    def is_empty(self):
        return self.size() == 0


# Example Usage:
graph = MyGraph(5)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

print("DFS:")
graph.dfs(0)
print("\nBFS:")
graph.bfs(0)

print("\nPeek:", graph.peek())
print("Size:", graph.size())
print("Is Empty:", graph.is_empty())

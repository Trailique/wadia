from collections import defaultdict, deque

class MyGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def dfs(self, start):
        if not self.graph:
            print("Error: Cannot perform DFS on an empty graph.")
            return []

        if start not in self.graph:
            print(f"Error: Starting vertex '{start}' not found in the graph.")
            return []

        visited = set()
        result = []
        self._dfs_helper(start, visited, result)
        return result

    def _dfs_helper(self, vertex, visited, result):
        visited.add(vertex)
        result.append(vertex)

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited, result)

    def bfs(self, start):
        if not self.graph:
            print("Error: Cannot perform BFS on an empty graph.")
            return []

        if start not in self.graph:
            print(f"Error: Starting vertex '{start}' not found in the graph.")
            return []

        visited = set()
        result = []
        queue = deque([start])

        while queue:
            current_vertex = queue.popleft()
            if current_vertex not in visited:
                visited.add(current_vertex)
                result.append(current_vertex)
                queue.extend(neighbor for neighbor in self.graph[current_vertex] if neighbor not in visited)

        return result

    def peek(self):
        if not self.graph:
            print("Error: Cannot peek from an empty graph.")
            return None

        first_vertex = next(iter(self.graph))
        return first_vertex

    def size(self):
        return len(self.graph)

    def is_empty(self):
        return len(self.graph) == 0


graph = MyGraph(5)

#Adds an edge between vertices v1 and v2.
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

#Returns the current number of vertices in the graph.
print("Graph size:", graph.size()) # Output:5
print("Is graph empty?", graph.is_empty())  #Output: false

#Returns the data of the first vertex without removing it.
print("Peek at the first vertex:", graph.peek()) #Output:0

#Performs depth-first search starting from the given vertex.
print("DFS starting from vertex 0:", graph.dfs(0)) #Output:[0, 1, 3, 2, 4]

#Performs breadth-first search starting from the given vertex.
print("BFS starting from vertex 0:", graph.bfs(0)) #Output:[0, 1, 3, 2, 4]

class MyGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def dfs(self, start):
        visited = set()
        self._dfs_util(start, visited)

    def _dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque()

        queue.append(start)
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def peek(self):
        if not self.is_empty():
            return next(iter(self.graph))

    def size(self):
        return len(self.graph)

    def is_empty(self):
        return len(self.graph) == 0


# Testing the MyGraph class
if __name__ == "__main__":
    # Create a graph with 5 vertices
    graph = MyGraph(5)

    # Add edges
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)

    print("DFS traversal starting from vertex 0:")
    graph.dfs(0)
    print("\nBFS traversal starting from vertex 0:")
    graph.bfs(0)

    print("\nPeek:", graph.peek())
    print("Size:", graph.size())
    print("Is empty?", graph.is_empty())
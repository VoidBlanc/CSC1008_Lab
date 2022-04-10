class Graph:
    def __init__(self):
        self.graph = {
            'A': {'B': 2, 'C': 4},
            'B': {'A': 2, 'C': 3, 'D': 8},
            'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
            'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
            'E': {'C': 5, 'D': 11, 'F': 1},
            'F': {'D': 22, 'E': 1}
        }
        self.num_vertices = 0

    def addNode(self, node):
        self.graph[node] = {}

    def addEdge(self, src, dest, distance=0):
        if src not in self.graph:
            self.graph[src] = {}

        self.graph[src][dest] = distance

    def getNodes(self):
        return self.graph.keys()

    def getEdges(self, node):
        return self.graph[node]


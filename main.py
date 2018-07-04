class Graph:

    def __init__(self, n):
        self.graph = {}
        for i in range(n):
            self.graph[i] = []

    def load():
        "Loads graph into a dict"

    def addEdge(self,a , b):
        "Adds edge to the graph"
        self.graph[a].append(b)
        self.graph[a].sort()
        self.graph[b].append(a)
        self.graph[b].sort()

    def getCommon(self, node1, node2):
        "Return list of common nodes"
        return list(set(self.graph[node1]).intersection(self.graph[node2]))
        
graph = Graph(5)
graph.addEdge(0,4)
print(graph.graph)

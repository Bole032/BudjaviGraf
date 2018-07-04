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

    def getUnion(self, node1, node2):
        "Return list of union nodes"
        return list(set().intersection(self.graph[node1], self.graph[node2]))

class Chance:
    def __init__(self, node1, node2, chance):
        self.node1 = node1
        self.node2 = node2
        self.chance = chance

    def getChance(self):
        return self.chance

def calculateChance_1(graph):
    chances = []
    for i in range(len(graph.graph)):
        for j in range(i, i + 1):
            if j not in graph.graph[i]:
                chances.append(Chance(i, j, graph.getCommon(i, j)))


graph = Graph(5)
graph.addEdge(0,4)
print(graph.graph)

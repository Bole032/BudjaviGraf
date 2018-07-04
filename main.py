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

def calculateChance_1(graph: Graph):
    "Method 1"
    chances = []
    for i in range(len(graph.graph)):
        for j in range(i + 1, len(graph.graph)):
            if j not in graph.graph[i]:
                chances.append(Chance(i, j, len(graph.getCommon(i, j))))

    chances.sort(key=lambda x: x.chance, reverse=True)
    return chances

def calculateChance_2(graph: Graph):
    "Method 2"
    chances = []
    for i in range(len(graph.graph)):
        for j in range(i + 1, len(graph.graph)):
            if j not in graph.graph[i]:
                chances.append(Chance(i, j, len(graph.getCommon(i, j)) / len(graph.getUnion(i, j))))

    chances.sort(key=lambda x: x.chance, reverse=True)
    return chances

def calculateChance_3(graph: Graph):
    "Method 3"
    chances = []
    for i in range(len(graph.graph)):
        for j in range(i + 1, len(graph.graph)):
            if j not in graph.graph[i]:
                chances.append(Chance(i, j, len(graph.graph[i]) * len(graph.graph[j])))

    chances.sort(key=lambda x: x.chance, reverse=True)
    return chances



graph = Graph(5)

graph.addEdge(0,4)
print(graph.graph)

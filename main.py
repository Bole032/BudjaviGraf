import dictionary

class Graph:

    def __init__(self, file, maxLines):
        lines = int(maxLines*0.7)

        ceoFajl = dictionary.takeFromCSV(file)
        self.graph = dictionary.sedamdesetPosto(ceoFajl[1: lines])
        

    def load(self):
        "Loads graph into a dict"

    def addEdge(self,a , b):
        "Adds edge to the graph"
        self.graph[a].append(b)
        # self.graph[a].sort()
        self.graph[b].append(a)
        # self.graph[b].sort()

    def getCommon(self, node1, node2):
        "Return list of common nodes"
        return list(set(self.graph[node1]).intersection(self.graph[node2]))

    def getUnion(self, node1, node2):
        "Return list of union nodes"
        union=self.graph[node1]+self.graph[node2]
        return list(set(union))

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
    for i in range(1, len(graph.graph)):
        for j in range(i + 1, len(graph.graph)):
            if j not in graph.graph[i]:
                chances.append(Chance(i, j, len(graph.getCommon(i, j))))

    chances.sort(key=lambda x: x.chance, reverse=True)
    return chances

def calculateChance_2(graph: Graph):
    "Method 2"
    chances = []
    for i in range(1, len(graph.graph)):
        for j in range(i + 1, len(graph.graph)):
            if j not in graph.graph[i]:
                if not(len(graph.getUnion(i, j)) == 0):
                    chances.append(Chance(i, j, len(graph.getCommon(i, j)) / len(graph.getUnion(i, j))))

    chances.sort(key=lambda x: x.chance, reverse=True)
    return chances

def calculateChance_3(graph: Graph):
    "Method 3"
    chances = []
    for i in range(1, len(graph.graph)):
        for j in range(i + 1, len(graph.graph)):
            if j not in graph.graph[i]:
                chances.append(Chance(i, j, len(graph.graph[i]) * len(graph.graph[j])))

    chances.sort(key=lambda x: x.chance, reverse=True)
    return chances



graph = Graph('cleaned.csv', 13839)

#print(graph.graph)
for chance in calculateChance_3(graph):
    print([chance.node1, chance.node2, chance.chance])
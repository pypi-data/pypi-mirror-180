#graph

#vertices are labelled 0-(n-1), pass this as an integer n

#edges is a list of lists length 3 containing the starting vertices, the ending vertices and the weights, use weight of 1 for unweighted graphs

#connectFrom and connectTo both specify where any connections come from or to and their weights as a list of lists length 2

#find shortest path finds the shortest path between two vertices (passed through as parameters) and returns a list 
#of vertices which are the shortest path followed by its weight in a tuple 

class inf:
    
    def __eq__(self, o):
        return False
    
    def __lt__(self, o):
        return False
    
    def __gt__(self, o):
        return True
    
    def __add__(self, o):
        return self
    
    def __sub__(self, o):
        return self
    
    def __rsub__(self, o):
        return self
    
    def __radd__(self,o):
        return self
        

class Vertex:
    def __init__(self,n):
        self.connectTo = []
        self.connectFrom = []
        self.number = n
    
class Graph:
    def __init__(self,edges,oneWayEdges=True):
        self.vertices = []
        self.length = 0
        self.oneWay = oneWayEdges
        self.edges = edges
        self.namesToNumbers = {}
        self.numbersToNames = {}
        
        for i in edges:
            if i[0] not in self.namesToNumbers.keys():
                self.addVertex(i[0])
            if i[1] not in self.namesToNumbers.keys():
                self.addVertex(i[1])
            
            self.addEdge(i)
            
    def findShortestPath(self,start,end,searchType = 'Ford'):
        if searchType == 'Ford':
            if not (start in self.namesToNumbers.keys() and end in self.namesToNumbers.keys()):
                raise Exception("Start or end not in graph")
            start = self.namesToNumbers[start]
            end = self.namesToNumbers[end]
            vertices = [[i,inf()] for i in range(self.length)]
            vertices[start] = [0,0]
            changes = 1
            while changes != 0:
                changes = 0
                for i in range(self.length):
                    for j in self.vertices[i].connectFrom:
                        if vertices[i][1] > (vertices[j[0]][1]+j[1]):
                            vertices[i][1] = (vertices[j[0]][1]+j[1])
                            changes += 1
            if isinstance(vertices[end][1], inf):
                return None, None
            currentPoint = end
            path = [end]
            count = 0
            while currentPoint != start and count <= self.length:
                for i in self.vertices[currentPoint].connectFrom:
                    if i[1] == (vertices[currentPoint][1] - vertices[i[0]][1]):
                        path.append(i[0])
                        currentPoint = i[0]
                        break
                count += 1
            if count == (self.length+1):
                raise Exception("Path does not exist")
            else:
                path = [self.numbersToNames[i] for i in path[::-1]]
                return path, vertices[end][1]
            
            
        if searchType == 'Djikstra':
            if not (start in self.namesToNumbers.keys() and end in self.namesToNumbers.keys()):
                raise Exception("Start or end not in graph")
            start = self.namesToNumbers[start]
            end = self.namesToNumbers[end]
            unvisited = [i for i in range(self.length)]
            tentDist = {i:inf() for i in range(self.length)}
            tentDist[start] = 0
            currentNode = start
            while currentNode != end:
                neighbours = sorted(self.vertices[currentNode].connectTo, key = lambda x:x[1])
                unvisited.remove(currentNode)
                for i in neighbours:
                    if tentDist[i[0]] > tentDist[currentNode]+i[1]:
                        tentDist[i[0]] = tentDist[currentNode]+i[1]
                nextNode = unvisited[0]
                for i in unvisited:
                    if tentDist[i] < tentDist[nextNode]:
                        nextNode = i
                if nextNode == currentNode:
                    raise Exception("Path does not exist")
                
                currentNode = nextNode
            
            if isinstance(tentDist[end], inf):
                return None, None
            path = [end]
            while currentNode != start:
                for i in self.vertices[currentNode].connectFrom:
                    if i[1] == tentDist[currentNode] - tentDist[i[0]]:
                        path.append(i[0])
                        currentNode = i[0]
            return [self.numbersToNames[i] for i in path[::-1]], tentDist[end]
    
    def DFS(self, Vertex):
        stack = [self.namesToNumbers[Vertex]]
        visited = []
        while stack != []:
            nextNode = stack.pop()
            if nextNode not in visited:
                visited.append(nextNode)
                for i in self.vertices[nextNode].connectTo:
                    stack.append(i[0])
                    
        return [self.numbersToNames[i] for i in visited]
                
    def BFS(self, Vertex):
        queue = [self.namesToNumbers[Vertex]]
        visited = []
        while queue != []:
            nextNode = queue.pop(0)
            if nextNode not in visited:
                visited.append(nextNode)
                for i in self.vertices[nextNode].connectTo:
                    queue.append(i[0])
        
        return [self.numbersToNames[i] for i in visited]
    
    def addVertex(self, v, raiseError = True):
        if v in self.namesToNumbers.keys():
            if raiseError:
                raise Exception("Vertex already exists")
            return self.namesToNumbers[v]
        else:
            self.vertices.append(Vertex(self.length))
            self.namesToNumbers[v] = self.length
            self.numbersToNames[self.length] = v
            self.length += 1
            return (self.length-1)
    
    def addEdge(self, e, oneWay=True , raiseError = True):
        if e[0] not in self.namesToNumbers.keys():
            if raiseError:
                raise Exception("First node not in graph")
            self.addVertex(e[0])
        if e[1] not in self.namesToNumbers.keys():
            if raiseError:
                raise Exception("Second node not in graph")
            self.addVertex(e[1])
        if oneWay and not self.oneWay:
            oneWay = self.oneWay 
        
        self.vertices[self.namesToNumbers[e[0]]].connectTo.append([self.namesToNumbers[e[1]], e[2]])
        self.vertices[self.namesToNumbers[e[1]]].connectFrom.append([self.namesToNumbers[e[0]], e[2]])
        if not oneWay:
            self.vertices[self.namesToNumbers[e[1]]].connectTo.append([self.namesToNumbers[e[0]], e[2]])
            self.vertices[self.namesToNumbers[e[0]]].connectFrom.append([self.namesToNumbers[e[1]], e[2]])


if __name__ == '__main__':
    a = [["A","B",3],["A","C",5],["A","D",7],["B","D",1],["B","E",7],["C","D",3],["C","F",2],["D","E",2],["D","G",4],["D","F",3],["E","G",2],["E","H",1],["F","G",3],["F","I",4],["G","H",3],["G","I",100],["H","I",5], ["X", "Y", 7], ["Z", "Y", 6]]
    b = [[0,1,3],[0,2,6],[0,3,4],[1,5,11],[1,2,4],[2,3,1],[2,4,2],[2,5,8],[3,4,4],[4,5,5]]
    h = Graph(edges=a,oneWayEdges=True)
    '''
    for i in range(8):
        print(h.vertices[i].connectTo)
        print(h.vertices[i].connectFrom)
    '''
    print(h.findShortestPath("A","I", searchType = 'Djikstra'))
    print(h.BFS("A"))
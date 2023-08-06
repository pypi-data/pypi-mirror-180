from random import randrange

class Stack:
    def __init__(self):
        self.stackarray = []
        self.length = len(self.stackarray)
    
    def append(self, value):
        self.stackarray.insert(0, value)
        self.length = len(self.stackarray)
        return value
    
    def pop(self):
        if (self.length <= 0):
            raise Exception('Stack is empty')
        
        poped = self.stackarray.pop(0)
        self.length = len(self.stackarray)
        return poped
    
    def view(self):
        return self.stackarray

class Queues:
    def __init__(self):
        self.queuearray = []
        self.length = len(self.queuearray)

    def append(self, value):
        self.queuearray.append(value)
        self.length = len(self.queuearray)

        return value
    
    def pop(self):
        if (self.length <= 0):
            raise Exception('Queue is empty')
        
        poped = self.queuearray.pop(0)
        self.length = len(self.queuearray)
        return poped

    def view(self):
        return self.queuearray
    

class Node:
    def __init__(self, data):
        self.d = set([data])
        self.visited = False

class UGraph:
    def __init__(self, vertices):
        self.v = vertices
        self.AdjList = dict()
        self.length = 0
    
    def add(self, v, dv): #dv | destination vertices
        if(v == dv): return 0
        if(v in self.AdjList):
            self.AdjList.get(v).d.add(dv)
        else:
            if(self.length >= self.v): return 0
            self.AdjList[v] = Node(dv)
            self.length += 1
        
        if(dv in self.AdjList):
            self.AdjList.get(dv).d.add(v)
        else:
            if(self.length >= self.v): return 0
            self.AdjList[dv] = Node(v)
            self.length += 1
        
    
    def adjacent(self, v1, v2):
        return (v2 in self.AdjList.get(v1).d)
    
    def neighbors(self, v1):
        return self.AdjList.get(v1).d
    
    def remove(self, v, dv=False): # if dv is given then remove the destination instead of main vertex(v)
        if(dv is False):
            self.AdjList.pop(v)
        else:
            self.AdjList.get(v).d.discard(dv)
 





# maze create start
def create(width: int=3, height: int=3, cellSize: int=1):
    if (width is False or height is False or cellSize is False):
        raise Exception("please make) sure that (width || height || cellSize) is not (None || 0)")

    w = width
    h = height
    cs = cellSize

    if(w%cs):
        raise Exception("please make) sure that (width % cellSize == 0)")
    
    if(h%cs):
        raise Exception("please make) sure that (height % cellSize == 0)")
    
    
    # reset the old stacks/arrays, and start maze generation
    return createMaze(width, height, cellSize)

def createMaze(width, height, cellSize):
    maxW = width/cellSize-1
    n = width/cellSize*height/cellSize
    graph = UGraph(n)
    count = 0
    for i in range(0, height, cellSize):
        for j in range(0, width, cellSize):
            if(count+1 <= maxW):
                graph.add(count, count+1)
            
            if(count+(width/cellSize) <= n-1):
                graph.add(count, count+(width/cellSize))
            
            count += 1
        
        maxW += width/cellSize
    
    return DFS(graph, 0)
    

# return the neighbours which are not visited yet
def visitedNeighbours(graph, c):
    nArray = list(graph.neighbors(c))
    remains = []
    for i in nArray:
        if(graph.AdjList.get(i).visited is False):
            remains.append(i)

    return remains;

# use DFS to traverse the graph(maze) and return the traversed nodes(cells/numbers) 
def DFS(graph, root):
    stk = Stack()
    mazeArr = []
    mazeGraph = UGraph(graph.v)

    graph.AdjList.get(root).visited = True
    stk.append(root)

    while(stk.length):
        curr = stk.pop()
        mazeArr.append(curr) # stores backtracked node/number/cells as well

        available = visitedNeighbours(graph, curr)
        if(len(available)):
            stk.append(curr)
            chosen = available[randrange(len(available))]
            graph.AdjList.get(chosen).visited = True
            mazeGraph.add(curr, chosen)
            stk.append(chosen)
    
    return {"mazeArr": mazeArr, "mazeGraph": mazeGraph}


# search algorithm: dijkstra
# target is always the last cell/node in the graph
def search(graph, root, target, searchAlgoId=1):
    if(graph is False):
        Exception("graph is undefined")
    if (root is None or target is None):
        Exception("(root || target) is (None)")

    if(searchAlgoId == 1):
        return dijkstra(graph, root, target)
    else:
        Exception("no search search algorithm with id "+searchAlgoId)
    
# need working
def dijkstra(graph, root, target):
    prev = [None] * int(graph.v)
    dist = [None] * int(graph.v)

    q = set();
    iterator = graph.AdjList.keys();
    
    for z in iterator:
        dist[int(z)] = 99999;
        prev[int(z)] = None;
        q.add(z);

    dist[root] = 0;
    #console.log(q.values().next().value);
    #curr = g.list[i];

    while(len(q) >= 1):
        u = dist.index(min(dist))

        if (u == target):
            break;

        if (u in q):
            q.discard(u)

        sathi = list(graph.AdjList.get(u).d)
        
        for i in range(len(sathi)):
            if(sathi[i] in q):
                alt = dist[u]+1
                tempIndex = int(sathi[i])
                if(alt < dist[tempIndex]):
                    dist[tempIndex] = alt;
                    prev[tempIndex] = u;
        
        dist[u] = 99999999;

    stk = Stack();
    ta = target;

    if (prev[ta] != None or ta == root):
        while(ta != None):
            stk.append(ta)
            ta = prev[ta]
   
    return stk

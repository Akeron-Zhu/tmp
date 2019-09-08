from collections import defaultdict 
from queue import PriorityQueue 

class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    
    def TopoSortBFS(self):
        #indegree=dict((node,0) for node in self.graph)
        indegree=defaultdict(int)
        for key in self.graph:
            for node in self.graph[key]:
                indegree[node]+=1

        # Although graph not include all nodes, but it must contain all zero indegree node when the graph is a valid DAG.
        # But if it is not a valid DAG, it must check all nodes, cause there may be lonely node. 
        baseNode=[node for node in self.graph if indegree[node]==0] 
        res=[]
        while baseNode:
            node=baseNode.pop(0)
            res.append(node)
            for childNode in self.graph[node]:
                indegree[childNode]-=1
                if indegree[childNode]==0:
                    baseNode.append(childNode)
        return res
    
    def TopoSortBFSLexicographic(self):
        indegree=defaultdict(int)
        for key in self.graph:
            for node in self.graph[key]:
                indegree[node]+=1

        baseNode=PriorityQueue()
        for node in self.graph:
            if indegree[node] == 0:
                baseNode.put(node)
        res=[]
        while not baseNode.empty(): 
            node=baseNode.get()
            res.append(node)
            for childNode in self.graph[node]:
                indegree[childNode]-=1
                if indegree[childNode]==0:
                    baseNode.put(childNode)
        return res

  
    def TopoDFS(self,node,visited,res):

        visited[node] = True
        for i in self.graph[node]:
            if visited[i] == False: 
                self.TopoDFS(i,visited,res) 
        res.insert(0,node) 
  
    def TopoSortDFS(self): 
        visited = [False]*self.V 
        res =[] 
  
        for node in range(self.V): 
            if visited[node] == False:
                self.TopoDFS(node,visited,res) 
        return res

# 有向图数据
datas = [
    [0, 1],
    [0, 2],
    [1, 2],
    [1, 3],
    [2, 3],
    [2, 5],
    [3, 4],
    [7, 6],
]

g = Graph(len(datas))
for beg,end in datas:
    #print(beg,end)
    g.addEdge(beg,end)

print(g.graph)

'''
g= Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
'''
print(g.TopoSortBFS())
print(g.TopoSortBFSLexicographic())
print(g.TopoSortDFS())
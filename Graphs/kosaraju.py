def reverseGraph(graph, n):
    revGraph = [ [] for _ in range(n) ]
    for i in range(n):
        edgeList = graph[i]
        for j in edgeList:
            revGraph[j].append(i)
            
    return revGraph
        

def finishingSort(graph, n):
    
    order = []
    visited = [0]*n
    def dfs(i):
        if visited[i]:
            return 
        
        visited[i] = 1
        
        for edge in graph[i]:
            if visited[edge] == 0:
                dfs(edge)
                order.insert(0, edge)
    
    dfs(0)
    order.insert(0, 0)
    
    return order

def kosaraju(graph, n):
    """
    An algorithm that helps us find out all the strongly connected components in a given directed graph. 
    The algorithm follows 3 steps: 
    1. Sort all the edges by their finishing time
    2. Reverse all the edges in the graph
    3. Do a DFS on the sorted order of nodes, where the SCC (strongly connected components) will turn out separated from the whole graph.
    """
    
    revGraph = reverseGraph(graph, n)
    order = finishingSort(graph, n)
    
    scc = 0
    visited = [0]*n
    
    def dfs(i):
        if visited[i]:
            return
        
        visited[i] = 1
        
        for edge in revGraph[i]:
            dfs(edge)
    
    for i in order:
        if not visited[i]:
            dfs(i)
            scc += 1
        
    return scc
    
    
graph = [
    [1],
    [2],
    [0, 3],
    [4],
    [5, 7],
    [6],
    [4, 7],
    []
]

print(kosaraju(graph, len(graph)))
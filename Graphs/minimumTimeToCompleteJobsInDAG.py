def minTimeInDAG(graph):
    n = len(graph)
    
    visited = [False] * n
    time = [0] * n
    
    def dfs(i, unit):
        if visited[i] and unit <= time[i]:
            return
        visited[i] = True
        time[i] = unit
        for neighbor in graph[i]:
            dfs(neighbor, unit+1)
            
    for i in range(n):
        dfs(i, 1)
        
    return time

graph = [
    [2, 3, 4],
    [2, 7, 8],
    [5],
    [5, 7],
    [7],
    [6],
    [7],
    [9],
    [],
    []
]

print(minTimeInDAG(graph))
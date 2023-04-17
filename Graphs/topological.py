def topologicalSort(graph):
    N = len(graph)
    visited = [False] * (N)
    stack = []
    def dfs(i):
        if visited[i]:
            return 
        
        visited[i] = True
        
        for n in graph[i]:
            dfs(n)
            
        stack.append(i)
        
    for i in range(N):
        dfs(i)
        
    return stack

graph = [[1, 2], [5, 6], [3, 4], [], [], [8], [7], [], [], []]
print(topologicalSort(graph))
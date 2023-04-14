def detectCycle(graph):
    def recursiveDFS(current, stack, visited):
        visited[current] = True
        stack[current] = True
        neighbors = graph[current]
        for n in neighbors:
            if not visited[n]:
                if recursiveDFS(n, stack, visited) == True:
                    return True
            elif stack[n] == True:
                return True
        
        stack[current] = False
        return False
    
    visited = [False] * (len(graph))
    stack = [False] * (len(graph))  
    for i in range(len(graph)):
        res = recursiveDFS(i, stack, visited)
        if res:  
            return True
    
    return False

graph = [
    [],
    [],
    [],
    [0, 1, 2, 4],
    [5],
    [3]
]

print(detectCycle(graph))
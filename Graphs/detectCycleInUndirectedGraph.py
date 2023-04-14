def detectCycle(graph):
    stack = [0]
    traversed = []
    visited = [False] * (len(graph) + 1)
    
    while len(stack) > 0:
        node = stack.pop(0)
        traversed.append(node)
        if visited[node]:
            return True
        visited[node] = True
        neighbors = graph[node]
        for n in neighbors:
                stack.insert(0, n)

    return False

graph = [
    [],
    [2],
    [1, 3],
    [2]
]

print(detectCycle(graph))
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
    [1, 2],
    [2],
    [0, 3],
    [3]
]

print(detectCycle(graph))
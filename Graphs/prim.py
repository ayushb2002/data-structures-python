def prim(graph):
    n = len(graph)
    visited = [0] * n
    pQ = [(0, 0, -1)] # (weight, current, parent)
    spanning = []
    sum = 0
    while len(pQ) > 0:
        pQ.sort()
        node = pQ.pop(0)
        if visited[node[1]]:
            continue
        
        visited[node[1]] = 1
        if node[2] != -1:
            spanning.append((node[2], node[1]))
            sum += node[0]
        for n in range(len(graph[node[1]])):
            if graph[node[1]][n] != 0 and graph[node[1]][n] != float('inf'):
                pQ.append((graph[node[1]][n], n, node[1]))
    
    print(spanning)
    return sum

graph = [
    [0, 2, 1, float('inf'), float('inf')],
    [2, 0, 1, float('inf'), float('inf')],
    [1, 1, 0, 2, 2],
    [float('inf'), float('inf'), 2, 0, 1],
    [float('inf'), float('inf'), 2, 1, 0]
]

print(prim(graph))
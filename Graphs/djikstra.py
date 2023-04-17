def shortest_path(graph, start):
    distances = [float('inf') for _ in range(len(graph))]
    visited = [False]*len(graph)
    distances[start] = 0
    def dijkstra(i):
        if visited[i]:
            return
        
        visited[i] = True
        neighbors = graph[i]
        next, nextIndex = float('inf'), float('inf')
        for j in range(len(neighbors)):
            if neighbors[j] != 0:
                distances[j] = min(distances[j], neighbors[j]+ distances[i])
                if not visited[j]:
                    next = min(next, distances[j])
                    if next == distances[j]:
                        nextIndex = j
                        
        return nextIndex
    
    count = 0
    i = start
    while count < len(graph)-2:
        i = dijkstra(i)
        count += 1
        
    return distances
    


graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

print(shortest_path(graph, 0))
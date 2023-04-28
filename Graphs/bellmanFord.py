def bellmanFord(graph):
    n = len(graph)
    dist = [float('inf') for _ in range(n)]
    dist[0] = 0
    
    for _ in range(n-1):
        for i in range(n):
            for edge in graph[i]:
                if dist[i] + edge[1] < dist[edge[0]]:
                    dist[edge[0]] = dist[i] + edge[1]
                    
    return dist

graph = [
    [(1, 5)],
    [(2, -2), (5, -3)],
    [(4, 3)],
    [(2, 6), (4, -2)],
    [],
    [(3, 1)]
]

print(bellmanFord(graph))
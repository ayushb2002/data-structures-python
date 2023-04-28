import copy

def floydWarshall(graph):
    """
    Multi source shortest path algorithm
    """
    dist = copy.deepcopy(graph)
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i!=k and j!=k:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
    return dist
        


graph = [
    [0, 2, float('inf'), float('inf')],
    [1, 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, float('inf')],
    [3, 5, 4, 0]
]

print(floydWarshall(graph))
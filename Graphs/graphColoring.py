def conditionCheck(node, graph, selected):
    n = len(graph)
    for i in range(n):
        if node in graph[i] and selected[node] == selected[i]:
            return False
            
    return True

def graphColoring(graph):
    n = len(graph)
    colors = ['Red', 'Green', 'Yellow', 'Blue']
    selected = ['' for _ in range(n)]
    selected[0] = colors[0]
        
    def backtrack(node, selected):
        if not conditionCheck(node-1, graph, selected):
            selected[node-1] = ''
            return selected, False
        
        if node >= n:
            return selected, True
        
        for i in range(4):
            selected[node] = colors[i]  
            selected, status = backtrack(node+1, selected)
            if status:
                return selected, True
            
    selected, status = backtrack(0, selected)
    
    return selected

graph = [
    [1, 4],
    [0, 2],
    [1, 3],
    [2, 4],
    [0, 3]
]

print(graphColoring(graph))
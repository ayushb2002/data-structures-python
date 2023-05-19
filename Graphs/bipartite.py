class Solution:
    def bipartite(self, graph):
        """
        A graph is said to be a bipartite graph if it can be colored with at max 2 colors, such that no two adjacent nodes will have the same color. Another simpler definition is that a bipartite graph is a graph which contains a cycle of odd number of nodes. 
        
        To check if a graph is a bipartite graph, we use breadth-first search to color each node with 0 or 1, and at the same time, we check if the neighbors of each node have different colors or not. If not, we return false.
        """
    
        n = len(graph)
        colors = [-1] * n
        def bfs(start):
            colors[start] = 0
            queue = [start]
            while len(queue) > 0:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if colors[neighbor] == colors[node]:
                        return False
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 if colors[node] == 0 else 0
                        queue.append(neighbor)
                        
            return True
        
        for i in range(n):
            if colors[i] == -1:
                res = bfs(i)
                if not res:
                    return False

        return True
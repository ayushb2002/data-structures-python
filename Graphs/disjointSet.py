class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*(n+1)
        self.parent = []
        for i in range(n+1):
            self.parent.append(i)
        
    def findUPar(self, node):
        """Finding the ultimate parent of a node"""
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def unionByRank(self, u, v):
        ult_u = self.findUPar(u)
        ult_v = self.findUPar(v)
        if ult_u == ult_v:
            return
        
        if self.rank[ult_u] < self.rank[ult_v]:
            self.parent[ult_u] = ult_v
        elif self.rank[ult_v] < self.rank[ult_u]:
            self.parent[ult_v] = ult_u
        else:
            self.parent[ult_v] = ult_u
            self.rank[ult_u] += 1
            
def main():
    ds = DisjointSet(7)
    ds.unionByRank(1, 2)
    ds.unionByRank(2, 3)
    ds.unionByRank(4, 5)
    ds.unionByRank(6, 7)
    ds.unionByRank(5, 6)
    # check if 3 and 7 belong to the same set or not
    if ds.findUPar(3) == ds.findUPar(7):
        print("Same set")
    else:
        print("Not same set")
    ds.unionByRank(3, 7)
    # check if 3 and 7 belong to the same set or not
    if ds.findUPar(3) == ds.findUPar(7):
        print("Same set")
    else:
        print("Not same set")

if __name__ == "__main__":
    main()
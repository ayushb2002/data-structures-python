def topView(root):
        view = {}
        queue = [(root, 0)]
        
        while len(queue) > 0:
            node, line = queue.pop(0)
            if line not in view.keys():
                view[line] = node.data
                
            if node.left:
                queue.append((node.left, line-1))
            if node.right:
                queue.append((node.right, line+1))
                
        sortedView = []
        for key, val in view.items():
            sortedView.append((key, val))
        
        sortedView.sort()
        res = []
        for i, j in sortedView:
            res.append(j)
            
        return res
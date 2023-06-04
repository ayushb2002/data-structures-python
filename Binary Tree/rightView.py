def RightView(root):
    if not root:
        return []
    res = []
    
    def traverse(node, level):
        if level == len(res):
            res.append(node.data)
            
        if node.right:
            traverse(node.right, level+1)
        if node.left:
            traverse(node.left, level+1)
            
    traverse(root, 0)
    return res
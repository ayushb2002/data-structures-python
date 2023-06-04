def zigZagTraversal(root):
        res = []
        queue = [root]
        flag = 0
        
        while len(queue) > 0:
            temp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            if flag == 0:
                res += temp
                flag = 1
            else:
                res += temp[::-1]
                flag = 0
                
        return res
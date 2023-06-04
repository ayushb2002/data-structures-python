def maxHeight(root):
    if not root:
        return 0
    return 1+max(maxHeight(root.left), maxHeight(root.right))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
root = TreeNode(1, TreeNode(2, TreeNode( 3, None, None),  TreeNode( 4,  None,  None)),  TreeNode( 5,  None,  TreeNode( 6,  None,  None)))
print(maxHeight(root))
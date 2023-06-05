class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    """
    left root right
    """
    if root.left:
        inorder(root.left)
    
    if root:
        print(root.val, end=" ")
    
    if root.right:
        inorder(root.right)
        
    return
    
def preorder(root):
    """
    root left right
    """
    if root:
        print(root.val, end=" ")
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)
        
    return
    
def postorder(root):
    """
    right left root
    """
    
    if root.right:
        postorder(root.right)
    if root.left:
        postorder(root.left)
    if root:
        print(root.val, end=" ")
        
    return
    
root = TreeNode(1, TreeNode(2, TreeNode( 3, None, None),  TreeNode( 4,  None,  None)),  TreeNode( 5,  None,  TreeNode( 6,  None,  None)))

print('')
inorder(root)
print('')
postorder(root)
print('')
preorder(root)
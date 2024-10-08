class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    if not root:
        return True
    
    def is_mirror(left, right):
        # Base cases
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root.left, root.right)

# Example usage
root1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(is_symmetric(root1))  

root2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(is_symmetric(root2))  

root3 = TreeNode(1)
print(is_symmetric(root3))  

root4 = None
print(is_symmetric(root4))  

root5 = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(is_symmetric(root5))  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        inorder=[]
        
        def getInorder(node):
            
            if not node:
                return
            
            getInorder(node.left)
            inorder.append(node.val)
            getInorder(node.right)
        
        getInorder(root)
        return inorder[k-1]
            
        
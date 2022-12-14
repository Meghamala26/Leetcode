# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def calDepth(self, node)-> int:
        
        if node==None:
            return 0
        
        return 1+ max(self.calDepth(node.left), self.calDepth(node.right))
        
        
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.calDepth(root)
        
        
    
        
        
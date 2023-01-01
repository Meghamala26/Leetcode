# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxPath=float('-inf')
        
        def sumPath(node):
            nonlocal maxPath
            if not node:
                return 0
            
            leftPath=sumPath(node.left)
            rightPath=sumPath(node.right)
            curPath=max(node.val,node.val+leftPath,node.val+rightPath)
            maxPath=max(maxPath,curPath,node.val+leftPath+rightPath)
            return curPath
            
        
        
        sumPath(root)
        return maxPath
        
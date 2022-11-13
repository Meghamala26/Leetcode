# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxSum=float('-inf')
        def getMaxPath(node):
            nonlocal maxSum
            if not node.left and not node.right:
                maxSum=max(maxSum,node.val)
                return node.val
            
            leftMax,rightMax=0,0
            
            if node.left:
                leftMax=getMaxPath(node.left)
            if node.right:
                rightMax=getMaxPath(node.right)
            
            maxSum=max(maxSum, leftMax+node.val,rightMax+node.val,leftMax+rightMax+node.val, node.val)
            
            return max(leftMax+node.val,rightMax+node.val, node.val)
        
        
        getMaxPath(root)
        return maxSum
        
        
            
        
        
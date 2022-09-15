# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxSum=[float('-inf')]
        
        def findMaxPath(node):
            if not node:
                return 0
            
            leftSubTree= findMaxPath(node.left)
            rightSubTree= findMaxPath(node.right)
            
            maxPath=max(node.val, node.val+leftSubTree, node.val+rightSubTree,  node.val+leftSubTree+rightSubTree)
            
            maxSum[0]=max(maxSum[0], maxPath)
            
            return max(node.val, node.val+leftSubTree, node.val+rightSubTree)
            
            
            
        
        
        findMaxPath(root)
        return maxSum[0]
 
        
        
        
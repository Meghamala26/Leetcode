# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        minDiff=abs(root.val-target)     
        closest=root.val
        
        def findClosest(node):
            nonlocal minDiff, closest
            if abs(node.val-target)<minDiff:
                minDiff=abs(node.val-target)
                closest=node.val
            if target>node.val and node.right:
                findClosest(node.right)
            if target<node.val and node.left:
                findClosest(node.left)
            return
            
            
        
        
        
        findClosest(root)
        return closest
        
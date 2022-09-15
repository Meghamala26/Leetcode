# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverse(self,node):
        
        if not node:
            return
        
        temp=node.left
        node.left=node.right
        node.right=temp
        
        self.reverse(node.left)
        self.reverse(node.right)
        
        return
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverse(root)
        return root
        
        
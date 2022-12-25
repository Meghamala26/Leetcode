# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        def invertChildren(node):
            if not node:
                return
            if node.left==None and node.right==None:
                return
            
            node.left,node.right=node.right,node.left
            invertChildren(node.left)
            invertChildren(node.right)
        
        
        invertChildren(root)
        return root
        
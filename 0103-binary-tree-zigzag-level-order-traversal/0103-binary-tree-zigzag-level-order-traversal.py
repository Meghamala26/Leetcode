# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        levels=[]
        def levelOrder(node,level):
            if len(levels)==level:
                levels.append([])
            
            if level%2==0:
                levels[level].append(node.val)
            else:
                levels[level].insert(0,node.val)
            
            if node.left:
                levelOrder(node.left,level+1)
            if node.right:
                levelOrder(node.right,level+1)
            
            return
                
            
            
        
        levelOrder(root,0)
        return levels
            
            
        
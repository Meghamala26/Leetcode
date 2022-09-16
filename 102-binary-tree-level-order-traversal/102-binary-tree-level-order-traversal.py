# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res=[]
        
        def getLevel(node,level):
            
            if len(res)==level:
                res.append([])
            
            res[level].append(node.val)
            
            if node.left:
                getLevel(node.left,level+1)
            if node.right:
                getLevel(node.right,level+1)
            
            
                
            
        
        if not root:
            return []
        
        getLevel(root,0)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res=[]
        
        def findLevel(node,level):
            if not node:
                return
            if len(res)==level:
                res.append([])
            res[level].append(node.val)
            findLevel(node.left,level+1)
            findLevel(node.right,level+1)
            
            
            
        
        
        findLevel(root,0)
        return res
                
        
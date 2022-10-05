# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        res=[]
        levels=[[root.val]]

        def levelOrder(node,level, res):
            if len(levels)==level:
                levels.append([])
                
            
            levels[level].append(node.val)
            
            if node.left:
                levelOrder(node.left,level+1,res)
            if node.right:
                levelOrder(node.right,level+1,res)
        
        if root.left:
            levelOrder(root.left,1,res)
        if root.right:
            levelOrder(root.right,1,res)
                
        print(levels)
        
        for i in range(len(levels)):
            res.append(levels[i][-1])
            
        return res
       
            
            
                
            
           
            
                
        
            
           
        
        
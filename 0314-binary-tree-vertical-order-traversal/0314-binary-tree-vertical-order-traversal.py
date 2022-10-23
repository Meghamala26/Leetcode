# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res=collections.defaultdict(list)
        levels=[]
        
        def traverse(node, col, row):
            if not node:
                return
            
            if node.left:
                res[col-1].append((row+1,node.left.val))
            if node.right:
                res[col+1].append((row+1,node.right.val))
                
            traverse(node.left,col-1, row+1)
            traverse(node.right,col+1, row+1)
            
            
            
        
        
        
    
       
        res[0].append((0,root.val))
        traverse(root,0,0)
        print(res)
        
        mincol,maxcol=min(res), max(res)
        for key in range(mincol, maxcol+1,1):
            res[key].sort(key=lambda x:x[0])
            colLevels=[val for row,val in res[key] ]
            levels.append(colLevels)
        return levels
        
        
        